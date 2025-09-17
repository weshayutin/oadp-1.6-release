
#!/usr/bin/env python3
"""
OADP Jira Issues to Upstream Velero Issues Report Generator

This script queries Jira for OADP issues and generates a markdown report
with their associated upstream Velero GitHub issues and labels.
"""

import os
import sys
import json
import requests
import re
import argparse
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from urllib.parse import urlparse

# Import content checker for duplicate detection
try:
    from content_checker import MarkdownContentChecker, ParsedRow
except ImportError:
    print("Warning: content_checker.py not found. Duplicate checking will be disabled.")
    MarkdownContentChecker = None
    ParsedRow = None

@dataclass
class GitHubIssue:
    """Represents a GitHub issue with its details"""
    number: int
    title: str
    state: str
    labels: List[str]
    url: str

@dataclass
class JiraIssue:
    """Represents a Jira issue with its GitHub associations"""
    key: str
    summary: str
    status: str
    priority: str
    issue_type: str
    assignee: str
    github_issues: List[GitHubIssue]
    url: str

class JiraGitHubReporter:
    """Main class for generating the OADP to Velero issues report"""
    
    def __init__(self, jira_token: str, github_token: Optional[str] = None):
        self.jira_base_url = "https://issues.redhat.com"
        self.jira_token = jira_token
        self.github_token = github_token
        
        # Setup session with authentication
        self.jira_session = requests.Session()
        self.jira_session.headers.update({
            'Authorization': f'Bearer {jira_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
        
        self.github_session = requests.Session()
        if github_token:
            self.github_session.headers.update({
                'Authorization': f'token {github_token}',
                'Accept': 'application/vnd.github.v3+json'
            })
    
    def search_jira_issues(self, jql: str) -> List[Dict]:
        """Search for Jira issues using JQL"""
        url = f"{self.jira_base_url}/rest/api/2/search"
        
        params = {
            'jql': jql,
            'fields': 'summary,status,priority,issuetype,issuelinks,assignee',
            'expand': 'changelog',
            'maxResults': 50
        }
        
        print(f"Searching Jira with JQL: {jql}")
        response = self.jira_session.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        print(f"Found {data['total']} issues")
        return data['issues']
    
    def get_issue_details(self, issue_key: str) -> Dict:
        """Get detailed information for a specific Jira issue"""
        url = f"{self.jira_base_url}/rest/api/2/issue/{issue_key}"
        
        params = {
            'fields': '*all',
            'expand': 'changelog'
        }
        
        response = self.jira_session.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_remote_issue_links(self, issue_key: str) -> List[Dict]:
        """Get remote issue links for a Jira issue"""
        url = f"{self.jira_base_url}/rest/api/2/issue/{issue_key}/remotelink"
        
        try:
            response = self.jira_session.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Warning: Could not fetch remote links for {issue_key}: {e}")
            return []
    
    def extract_github_references(self, issue_data: Dict, remote_links: List[Dict]) -> List[str]:
        """Extract GitHub issue URLs from Jira issue data and remote links"""
        github_urls = set()
        
        # Check issue links (internal Jira links)
        issue_links = issue_data.get('fields', {}).get('issuelinks', [])
        for link in issue_links:
            # Check outward and inward issues for GitHub references
            for direction in ['outwardIssue', 'inwardIssue']:
                if direction in link:
                    linked_issue = link[direction]
                    # Sometimes GitHub URLs are in the summary or description
                    summary = linked_issue.get('fields', {}).get('summary', '')
                    urls = self._extract_github_urls_from_text(summary)
                    github_urls.update(urls)
        
        # Check remote links
        for remote_link in remote_links:
            if 'object' in remote_link and 'url' in remote_link['object']:
                url = remote_link['object']['url']
                if 'github.com/vmware-tanzu/velero' in url:
                    github_urls.add(url)
            
            # Also check title and summary for GitHub references
            if 'object' in remote_link:
                obj = remote_link['object']
                for field in ['title', 'summary']:
                    if field in obj:
                        urls = self._extract_github_urls_from_text(obj[field])
                        github_urls.update(urls)
        
        # Check description and comments for GitHub URLs
        description = issue_data.get('fields', {}).get('description', '') or ''
        urls = self._extract_github_urls_from_text(description)
        github_urls.update(urls)
        
        # Check changelog for GitHub references
        changelog = issue_data.get('changelog', {}).get('histories', [])
        for history in changelog:
            for item in history.get('items', []):
                for field in ['toString', 'fromString']:
                    if field in item and item[field]:
                        urls = self._extract_github_urls_from_text(item[field])
                        github_urls.update(urls)
        
        return list(github_urls)
    
    def _extract_github_urls_from_text(self, text: str) -> List[str]:
        """Extract GitHub URLs from text using regex"""
        if not text:
            return []
        
        # Pattern for GitHub URLs
        github_pattern = r'https://github\.com/vmware-tanzu/velero/(?:issues|pull)/(\d+)'
        matches = re.findall(github_pattern, text)
        
        # Also look for issue/PR numbers mentioned without full URLs
        number_pattern = r'(?:issue|pr|pull|#)\s*:?\s*(\d+)'
        number_matches = re.findall(number_pattern, text, re.IGNORECASE)
        
        urls = []
        
        # Add full URLs
        for match in matches:
            urls.append(f'https://github.com/vmware-tanzu/velero/issues/{match}')
        
        # Add URLs constructed from issue numbers (if they look like Velero issue numbers)
        for number in number_matches:
            if int(number) > 1000:  # Velero issues are typically 4+ digits
                urls.append(f'https://github.com/vmware-tanzu/velero/issues/{number}')
        
        return list(set(urls))  # Remove duplicates
    
    def get_github_issue_details(self, github_url: str) -> Optional[GitHubIssue]:
        """Get details for a GitHub issue"""
        # Extract issue number from URL
        match = re.search(r'/issues/(\d+)', github_url)
        if not match:
            return None
        
        issue_number = int(match.group(1))
        api_url = f'https://api.github.com/repos/vmware-tanzu/velero/issues/{issue_number}'
        
        try:
            response = self.github_session.get(api_url)
            response.raise_for_status()
            data = response.json()
            
            labels = [label['name'] for label in data.get('labels', [])]
            
            return GitHubIssue(
                number=data['number'],
                title=data['title'],
                state=data['state'],
                labels=labels,
                url=data['html_url']
            )
        except requests.exceptions.RequestException as e:
            print(f"Warning: Could not fetch GitHub issue {issue_number}: {e}")
            return None
    
    def get_velero_milestone_issues(self, milestone: str) -> List[GitHubIssue]:
        """Get all issues from a specific Velero milestone using GitHub search API"""
        print(f"\nFetching Velero milestone {milestone} issues...")
        
        # Use GitHub search API to find issues by milestone
        api_url = 'https://api.github.com/search/issues'
        query = f'repo:vmware-tanzu/velero milestone:{milestone} is:issue'
        params = {
            'q': query,
            'per_page': 100,
            'sort': 'created',
            'order': 'desc'
        }
        
        all_issues = []
        page = 1
        
        while True:
            params['page'] = page
            try:
                response = self.github_session.get(api_url, params=params)
                response.raise_for_status()
                data = response.json()
                
                issues = data.get('items', [])
                if not issues:
                    break
                
                for issue_data in issues:
                    # Skip pull requests (they appear in search results)
                    if 'pull_request' in issue_data:
                        continue
                    
                    labels = [label['name'] for label in issue_data.get('labels', [])]
                    github_issue = GitHubIssue(
                        number=issue_data['number'],
                        title=issue_data['title'],
                        state=issue_data['state'],
                        labels=labels,
                        url=issue_data['html_url']
                    )
                    all_issues.append(github_issue)
                
                # Check if we have more pages
                if len(issues) < params['per_page']:
                    break
                
                page += 1
                
            except requests.exceptions.RequestException as e:
                print(f"Warning: Could not fetch milestone issues: {e}")
                break
        
        print(f"Found {len(all_issues)} issues in Velero {milestone} milestone")
        return all_issues

    def get_migtools_project_issues(self, org: str = "migtools", project_number: int = 7) -> List[str]:
        """Get issues from GitHub project board using GraphQL API"""
        print(f"\nFetching {org} project {project_number} issues...")
        
        if not self.github_token:
            print("Warning: GitHub token required for Projects v2 API access")
            return []
        
        # GraphQL query for Projects v2
        graphql_query = """
        query($org: String!, $projectNumber: Int!) {
          organization(login: $org) {
            projectV2(number: $projectNumber) {
              title
              items(first: 100) {
                nodes {
                  content {
                    ... on Issue {
                      number
                      title
                      repository {
                        name
                        owner {
                          login
                        }
                      }
                    }
                    ... on PullRequest {
                      number
                      title
                      repository {
                        name
                        owner {
                          login
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
        """
        
        variables = {
            "org": org,
            "projectNumber": project_number
        }
        
        try:
            response = self.github_session.post(
                'https://api.github.com/graphql',
                json={
                    'query': graphql_query,
                    'variables': variables
                }
            )
            response.raise_for_status()
            data = response.json()
            
            if 'errors' in data:
                print(f"GraphQL errors: {data['errors']}")
                return []
            
            project_items = []
            project_data = data.get('data', {}).get('organization', {}).get('projectV2', {})
            
            if not project_data:
                print("Warning: Could not access migtools project data (may require permissions)")
                return []
            
            items = project_data.get('items', {}).get('nodes', [])
            
            for item in items:
                content = item.get('content', {})
                if content:
                    repo_info = content.get('repository', {})
                    owner = repo_info.get('owner', {}).get('login', '')
                    repo_name = repo_info.get('name', '')
                    number = content.get('number', '')
                    
                    if owner and repo_name and number:
                        project_items.append(f"{owner}/{repo_name}#{number}")
            
            print(f"Found {len(project_items)} issues in {org} project {project_number}")
            return project_items
            
        except requests.exceptions.RequestException as e:
            print(f"Warning: Could not fetch {org} project {project_number} issues: {e}")
            print("Falling back to manual population - update the script with issue numbers")
            return []

    def generate_report(self, jql: str) -> str:
        """Generate the complete markdown report"""
        print("Starting OADP to Velero issues report generation...")
        
        # Search for Jira issues
        jira_issues_data = self.search_jira_issues(jql)
        
        processed_issues = []
        
        for issue_data in jira_issues_data:
            issue_key = issue_data['key']
            print(f"\nProcessing {issue_key}...")
            
            # Get detailed issue information
            detailed_issue = self.get_issue_details(issue_key)
            
            # Get remote issue links
            remote_links = self.get_remote_issue_links(issue_key)
            
            # Extract GitHub references
            github_urls = self.extract_github_references(detailed_issue, remote_links)
            
            # Get GitHub issue details
            github_issues = []
            for url in github_urls:
                github_issue = self.get_github_issue_details(url)
                if github_issue:
                    github_issues.append(github_issue)
                    print(f"  Found GitHub issue: #{github_issue.number} - {github_issue.title}")
            
            # Create Jira issue object
            fields = detailed_issue['fields']
            assignee_info = fields.get('assignee')
            assignee = assignee_info.get('displayName', 'Unassigned') if assignee_info else 'Unassigned'
            
            jira_issue = JiraIssue(
                key=issue_key,
                summary=fields.get('summary', ''),
                status=fields.get('status', {}).get('name', 'Unknown'),
                priority=fields.get('priority', {}).get('name', 'Unknown'),
                issue_type=fields.get('issuetype', {}).get('name', 'Unknown'),
                assignee=assignee,
                github_issues=github_issues,
                url=f"https://issues.redhat.com/browse/{issue_key}"
            )
            
            processed_issues.append(jira_issue)
        
        # Check for content changes
        print("\n" + "-"*50)
        print("Checking for content changes...")
        new_issues, updated_issues, unchanged_issues = self._check_content_changes(processed_issues, "oadp_velero_issues.md")
        
        # Get Velero 1.18 milestone issues
        velero_milestone_issues = self.get_velero_milestone_issues('v1.18')
        
        # Generate markdown report
        return self._generate_markdown(processed_issues, jql, velero_milestone_issues)
    
    def _check_content_changes(self, issues: List[JiraIssue], output_file: str = "oadp_velero_issues.md") -> Tuple[List[JiraIssue], List[JiraIssue], List[JiraIssue]]:
        """
        Check for content changes and categorize issues into new, updated, and unchanged.
        
        Returns:
            (new_issues, updated_issues, unchanged_issues)
        """
        if not MarkdownContentChecker:
            print("Content checker not available. All issues will be treated as new.")
            return issues, [], []
        
        # Load existing content
        checker = MarkdownContentChecker(output_file)
        checker.load_existing_content()
        
        new_issues = []
        updated_issues = []
        unchanged_issues = []
        
        for issue in issues:
            github_numbers = [gh.number for gh in issue.github_issues]
            
            is_duplicate, existing_row = checker.check_for_duplicates(issue.key, github_numbers)
            should_update, _ = checker.should_update_row(issue.key, github_numbers)
            
            if is_duplicate:
                unchanged_issues.append(issue)
                print(f"✓ {issue.key}: Content unchanged (same GitHub issues: {github_numbers})")
            elif should_update:
                updated_issues.append(issue)
                existing_github = existing_row.github_issues if existing_row else []
                print(f"⚠ {issue.key}: GitHub issues changed from {existing_github} to {github_numbers}")
            else:
                new_issues.append(issue)
                print(f"+ {issue.key}: New issue (GitHub issues: {github_numbers})")
        
        print(f"\nContent Analysis Summary:")
        print(f"- New issues: {len(new_issues)}")
        print(f"- Updated issues: {len(updated_issues)}")
        print(f"- Unchanged issues: {len(unchanged_issues)}")
        
        return new_issues, updated_issues, unchanged_issues

    def _generate_markdown(self, issues: List[JiraIssue], jql: str, velero_milestone_issues: List[GitHubIssue]) -> str:
        """Generate the markdown report from processed issues"""
        
        # First, identify which OADP issues are referenced by milestone issues
        milestone_github_numbers = {issue.number for issue in velero_milestone_issues}
        issues_in_milestone = set()
        
        for oadp_issue in issues:
            for gh_issue in oadp_issue.github_issues:
                if gh_issue.number in milestone_github_numbers:
                    issues_in_milestone.add(oadp_issue.key)
                    break
        
        # Filter out issues that appear in milestone section
        candidate_issues = [issue for issue in issues if issue.key not in issues_in_milestone]
        
        # Load existing content to preserve order and row numbers
        existing_candidate_table = self._load_existing_candidate_table()
        existing_milestone_table = self._load_existing_milestone_table()
        
        markdown_lines = [
            "# OADP Issues and Upstream Velero Issue Mapping",
            "",
            "This document contains a mapping of OADP Jira issues to their associated upstream Velero GitHub issues and labels.",
            "",
            f"**Query Used:** `{jql}`",
            "",
            "## Jira to Upstream Candidate",
            "",
            "*Note: OADP issues that reference Velero v1.18 milestone issues are shown in the milestone cross-reference section below.*",
            "",
            "| Row # | Jira Issue | Jira Assignee | Upstream Velero Issue(s) | Upstream Velero Issue Labels |",
            "|-------|------------|---------------|---------------------------|------------------------------|"
        ]
        
        issues_with_github = 0
        issues_without_github = 0
        
        # Generate ordered candidate table with row numbers
        ordered_candidate_rows = self._generate_ordered_candidate_table(candidate_issues, existing_candidate_table)
        
        for row_num, issue in ordered_candidate_rows:
            # Format Jira issue cell
            jira_cell = f"[{issue.key}]({issue.url}) - {issue.summary}"
            
            # Format GitHub issues cell
            if issue.github_issues:
                github_parts = []
                for gh_issue in issue.github_issues:
                    state_info = f" ({gh_issue.state})"
                    github_link_text = f"[#{gh_issue.number}]({gh_issue.url}) - {gh_issue.title}{state_info}"
                    
                    # Apply formatting for closed issues (GitHub markdown doesn't support custom colors)
                    if gh_issue.state.lower() == "closed":
                        github_link_text = f"✅ **{github_link_text}**"
                    
                    github_parts.append(github_link_text)
                github_cell = "<br>".join(github_parts)
                issues_with_github += 1
            else:
                github_cell = "*No upstream GitHub issue found*"
                issues_without_github += 1
            
            # Format labels cell
            if issue.github_issues:
                label_parts = []
                for gh_issue in issue.github_issues:
                    if gh_issue.labels:
                        labels_str = ", ".join(gh_issue.labels)
                        label_parts.append(f"**#{gh_issue.number}**: {labels_str}")
                    else:
                        label_parts.append(f"**#{gh_issue.number}**: *No labels*")
                labels_cell = "<br>".join(label_parts) if label_parts else "*N/A*"
            else:
                labels_cell = "*N/A*"
            
            markdown_lines.append(f"| {row_num} | {jira_cell} | {issue.assignee} | {github_cell} | {labels_cell} |")
        
        # Add summary
        milestone_referenced_count = len(issues_in_milestone)
        markdown_lines.extend([
            "",
            "## Summary",
            "",
            f"- **Total Issues**: {len(issues)}",
            f"- **Issues in Candidate Table**: {len(candidate_issues)}",
            f"- **Issues Referenced in Milestone Section**: {milestone_referenced_count}",
            f"- **Issues with Upstream GitHub Issues**: {issues_with_github}",
            f"- **Issues without Upstream GitHub Issues**: {issues_without_github}",
            ""
        ])
        
        # Add Velero 1.18 Milestone Cross-Reference
        markdown_lines.extend(self._generate_velero_milestone_section(issues, velero_milestone_issues))
        
        return "\n".join(markdown_lines)
    
    def _load_existing_candidate_table(self) -> Dict[str, int]:
        """Load existing candidate table and return mapping of Jira key to row number"""
        existing_rows = {}
        try:
            with open("oadp_velero_issues.md", 'r', encoding='utf-8') as f:
                content = f.read()
            
            lines = content.split('\n')
            in_candidate_table = False
            current_row = 1
            
            for line in lines:
                # Identify candidate table section
                if "| Row # | Jira Issue | Jira Assignee | Upstream Velero Issue(s) | Upstream Velero Issue Labels |" in line:
                    in_candidate_table = True
                    current_row = 1
                    continue
                elif line.startswith('|-------|'):
                    continue
                elif in_candidate_table and line.startswith('|') and '|' in line[1:]:
                    # Parse row to extract Jira key
                    parts = [part.strip() for part in line.split('|')]
                    if len(parts) >= 3:
                        # Skip if this is a header row or separator
                        if parts[1].isdigit() or parts[1] == 'Row #':
                            if parts[1].isdigit():
                                # Extract Jira key from the third column (index 2)
                                jira_part = parts[2]
                                jira_match = re.search(r'\[([^]]+)\]', jira_part)
                                if jira_match:
                                    jira_key = jira_match.group(1)
                                    existing_rows[jira_key] = int(parts[1])
                                    current_row = max(current_row, int(parts[1]) + 1)
                elif in_candidate_table and not line.startswith('|'):
                    # End of candidate table
                    break
                    
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Warning: Error loading existing candidate table: {e}")
        
        return existing_rows
    
    def _load_existing_milestone_table(self) -> Dict[int, int]:
        """Load existing milestone table and return mapping of GitHub issue number to row number"""
        existing_rows = {}
        try:
            with open("oadp_velero_issues.md", 'r', encoding='utf-8') as f:
                content = f.read()
            
            lines = content.split('\n')
            in_milestone_table = False
            current_row = 1
            
            for line in lines:
                # Identify milestone table section
                if "| Row # | Velero Issue | Status | Labels | Associated OADP Issue(s) | Jira Assignee |" in line:
                    in_milestone_table = True
                    current_row = 1
                    continue
                elif line.startswith('|-------|'):
                    continue
                elif in_milestone_table and line.startswith('|') and '|' in line[1:]:
                    # Parse row to extract GitHub issue number
                    parts = [part.strip() for part in line.split('|')]
                    if len(parts) >= 3:
                        if parts[1].isdigit() or parts[1] == 'Row #':
                            if parts[1].isdigit():
                                # Extract GitHub issue number from the second column (index 2)
                                velero_part = parts[2]
                                github_match = re.search(r'#(\d+)', velero_part)
                                if github_match:
                                    github_number = int(github_match.group(1))
                                    existing_rows[github_number] = int(parts[1])
                                    current_row = max(current_row, int(parts[1]) + 1)
                elif in_milestone_table and not line.startswith('|'):
                    # End of milestone table
                    break
                    
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Warning: Error loading existing milestone table: {e}")
        
        return existing_rows
    
    def _generate_ordered_candidate_table(self, issues: List[JiraIssue], existing_table: Dict[str, int]) -> List[Tuple[int, JiraIssue]]:
        """Generate ordered table rows preserving existing row numbers and appending new ones"""
        ordered_rows = []
        used_row_numbers = set(existing_table.values())
        next_row_number = max(used_row_numbers) + 1 if used_row_numbers else 1
        
        # First, add existing issues in their original order
        existing_issues = []
        new_issues = []
        
        for issue in issues:
            if issue.key in existing_table:
                row_num = existing_table[issue.key]
                ordered_rows.append((row_num, issue))
                existing_issues.append(issue)
            else:
                new_issues.append(issue)
        
        # Sort existing issues by their row numbers
        ordered_rows.sort(key=lambda x: x[0])
        
        # Append new issues at the end
        for issue in new_issues:
            ordered_rows.append((next_row_number, issue))
            next_row_number += 1
        
        return ordered_rows
    
    def _generate_ordered_milestone_table(self, milestone_issues: List[GitHubIssue], existing_table: Dict[int, int]) -> List[Tuple[int, GitHubIssue]]:
        """Generate ordered milestone table rows preserving existing row numbers and appending new ones"""
        ordered_rows = []
        used_row_numbers = set(existing_table.values())
        next_row_number = max(used_row_numbers) + 1 if used_row_numbers else 1
        
        # First, add existing issues in their original order
        existing_issues = []
        new_issues = []
        
        for issue in milestone_issues:
            if issue.number in existing_table:
                row_num = existing_table[issue.number]
                ordered_rows.append((row_num, issue))
                existing_issues.append(issue)
            else:
                new_issues.append(issue)
        
        # Sort existing issues by their row numbers
        ordered_rows.sort(key=lambda x: x[0])
        
        # Append new issues at the end
        for issue in new_issues:
            ordered_rows.append((next_row_number, issue))
            next_row_number += 1
        
        return ordered_rows
    
    def _generate_velero_milestone_section(self, oadp_issues: List[JiraIssue], milestone_issues: List[GitHubIssue]) -> List[str]:
        """Generate the Velero 1.18 milestone cross-reference section"""
        
        # Create a mapping of GitHub issue numbers to OADP issues
        github_to_oadp = {}
        for oadp_issue in oadp_issues:
            for gh_issue in oadp_issue.github_issues:
                if gh_issue.number not in github_to_oadp:
                    github_to_oadp[gh_issue.number] = []
                github_to_oadp[gh_issue.number].append(oadp_issue)
        
        # Load existing milestone table to preserve order and row numbers
        existing_milestone_table = self._load_existing_milestone_table()
        
        markdown_lines = [
            "## Velero v1.18 Milestone Issues Cross-Reference",
            "",
            "This section lists all issues in the [Velero v1.18 milestone](https://github.com/vmware-tanzu/velero/issues?q=is%3Aissue%20milestone%3Av1.18) and identifies which ones are also referenced by OADP issues above.",
            "",
            "| Row # | Velero Issue | Status | Labels | Associated OADP Issue(s) | Jira Assignee |",
            "|-------|--------------|--------|--------|-------------------------|---------------|"
        ]
        
        matched_issues = 0
        
        # Generate ordered milestone table with row numbers
        ordered_milestone_rows = self._generate_ordered_milestone_table(milestone_issues, existing_milestone_table)
        
        for row_num, milestone_issue in ordered_milestone_rows:
            # Format Velero issue cell
            state_info = f" ({milestone_issue.state})"
            velero_cell = f"[#{milestone_issue.number}]({milestone_issue.url}) - {milestone_issue.title}{state_info}"
            
            # Apply formatting for closed issues (GitHub markdown doesn't support custom colors)
            if milestone_issue.state.lower() == "closed":
                velero_cell = f"✅ **{velero_cell}**"
            
            # Format status cell
            status_cell = milestone_issue.state.capitalize()
            
            # Format labels cell
            if milestone_issue.labels:
                labels_cell = ", ".join(milestone_issue.labels[:5])  # Limit to first 5 labels
                if len(milestone_issue.labels) > 5:
                    labels_cell += f" (+{len(milestone_issue.labels) - 5} more)"
            else:
                labels_cell = "*No labels*"
            
            # Check if this milestone issue is referenced by any OADP issue
            if milestone_issue.number in github_to_oadp:
                oadp_refs = github_to_oadp[milestone_issue.number]
                oadp_parts = []
                assignee_parts = []
                for oadp_issue in oadp_refs:
                    oadp_parts.append(f"[{oadp_issue.key}]({oadp_issue.url})")
                    assignee_parts.append(oadp_issue.assignee)
                oadp_cell = "<br>".join(oadp_parts)
                # Remove duplicates but preserve order
                unique_assignees = []
                seen = set()
                for assignee in assignee_parts:
                    if assignee not in seen:
                        unique_assignees.append(assignee)
                        seen.add(assignee)
                assignee_cell = "<br>".join(unique_assignees)
                matched_issues += 1
            else:
                oadp_cell = "*Not referenced by OADP issues*"
                assignee_cell = "*N/A*"
            
            markdown_lines.append(f"| {row_num} | {velero_cell} | {status_cell} | {labels_cell} | {oadp_cell} | {assignee_cell} |")
        
        # Add milestone summary
        markdown_lines.extend([
            "",
            "### Velero v1.18 Milestone Summary",
            "",
            f"- **Total Velero v1.18 Issues**: {len(milestone_issues)}",
            f"- **Issues Referenced by OADP**: {matched_issues}",
            f"- **Issues Not Referenced by OADP**: {len(milestone_issues) - matched_issues}",
            ""
        ])
        
        return markdown_lines
    
    def _generate_migtools_section(self, migtools_issues: List[str], github_org: str, github_project_num: int) -> List[str]:
        """Generate the GitHub project section"""
        
        project_url = f"https://github.com/orgs/{github_org}/projects/{github_project_num}"
        
        markdown_lines = [
            f"## {github_org.title()} Project {github_project_num}",
            "",
            f"This section lists issues from the [{github_org} project {github_project_num}]({project_url}).",
            "",
        ]
        
        if migtools_issues:
            markdown_lines.extend([
                "| Issue/PR Number | Repository |",
                "|-----------------|------------|"
            ])
            
            for issue in migtools_issues:
                # Parse issue format like "migtools/oadp-operator#123"
                if "/" in issue and "#" in issue:
                    repo_part, issue_number = issue.split("#")
                    repo_name = repo_part.split("/")[-1] if "/" in repo_part else repo_part
                    issue_url = f"https://github.com/{repo_part}/issues/{issue_number}"
                    markdown_lines.append(f"| [{issue}]({issue_url}) | {repo_name} |")
                else:
                    # Simple format, just show the issue
                    markdown_lines.append(f"| {issue} | Unknown |")
                    
            markdown_lines.extend([
                "",
                f"**Total {github_org.title()} Issues**: {len(migtools_issues)}",
                ""
            ])
        else:
            markdown_lines.extend([
                f"*No {github_org} project issues available. This section requires manual population or GitHub GraphQL API access.*",
                "",
                "**To populate this section:**",
                f"1. Access the [{github_org} project {github_project_num}]({project_url})",
                "2. Export or manually list the issue/PR numbers",
                "3. Update the `get_migtools_project_issues()` method in the script",
                "4. Or set environment variables: `GITHUB_PROJECT_ORG` and `GITHUB_PROJECT_NUMBER`",
                ""
            ])
        
        return markdown_lines

def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description='Generate OADP to Velero issues mapping report',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s
  %(prog)s --output my_report.md
  %(prog)s --jql "project = OADP AND status != Closed"
  %(prog)s --dry-run
  
Environment Variables:
  JIRA_TOKEN              Required: Jira authentication token
  GITHUB_TOKEN            Optional: GitHub personal access token (recommended)
        """
    )
    
    parser.add_argument(
        '--output', '-o',
        default='oadp_velero_issues.md',
        help='Output markdown file name (default: oadp_velero_issues.md)'
    )
    
    parser.add_argument(
        '--jql',
        default=('project = OADP AND status not in (Closed) AND '
                 '(fixVersion = "OADP 1.6.0" OR fixVersion = "OADP 1.6.0") AND '
                 '(labels = oadp_upstream_bug_fix ) ORDER BY priority DESC, Rank ASC'),
        help='Custom JQL query to search for Jira issues'
    )
    
    
    parser.add_argument(
        '--check-duplicates',
        action='store_true',
        default=True,
        help='Check for duplicate content before writing new rows (default: enabled)'
    )
    
    parser.add_argument(
        '--no-check-duplicates',
        action='store_true',
        help='Disable duplicate content checking (overwrite all content)'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Print configuration and exit without generating report'
    )
    
    args = parser.parse_args()
    
    # Get authentication tokens from environment variables
    jira_token = os.getenv('JIRA_TOKEN')
    github_token = os.getenv('GITHUB_TOKEN')  # Optional
    
    if not jira_token:
        print("Error: JIRA_TOKEN environment variable is required")
        print("Set it with: export JIRA_TOKEN='your_jira_token_here'")
        sys.exit(1)
    
    if not github_token:
        print("Warning: GITHUB_TOKEN not set. GitHub API calls will be rate-limited.")
        print("For better performance, set: export GITHUB_TOKEN='your_github_token_here'")
    
    # Print configuration if dry run
    if args.dry_run:
        print("Configuration:")
        print(f"  Output file: {args.output}")
        print(f"  JQL query: {args.jql}")
        print(f"  Jira token: {'✓ Set' if jira_token else '✗ Not set'}")
        print(f"  GitHub token: {'✓ Set' if github_token else '✗ Not set'}")
        return
    
    try:
        # Create reporter and generate report
        reporter = JiraGitHubReporter(jira_token, github_token)
        markdown_content = reporter.generate_report(args.jql)
        
        # Write to file
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"\nReport generated successfully: {args.output}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
