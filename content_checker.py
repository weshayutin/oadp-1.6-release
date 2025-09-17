#!/usr/bin/env python3
"""
Content checker for OADP Velero Issues markdown file.
Checks for existing content before adding new rows to prevent duplicates.
"""

import re
from typing import Dict, List, Set, Tuple, Optional
from dataclasses import dataclass


@dataclass
class ParsedRow:
    """Represents a parsed row from the markdown table"""
    jira_key: str
    jira_summary: str
    assignee: str
    github_issues: List[int]  # List of GitHub issue numbers
    github_labels: str
    raw_content: str
    line_number: int


class MarkdownContentChecker:
    """Checks for existing content in OADP Velero Issues markdown file"""
    
    def __init__(self, markdown_file_path: str):
        self.markdown_file_path = markdown_file_path
        self.existing_rows: List[ParsedRow] = []
        self.jira_to_github_map: Dict[str, Set[int]] = {}
        
    def load_existing_content(self) -> None:
        """Load and parse existing markdown content"""
        try:
            with open(self.markdown_file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            self._parse_content(content)
            print(f"Loaded {len(self.existing_rows)} existing rows from {self.markdown_file_path}")
            
        except FileNotFoundError:
            print(f"File {self.markdown_file_path} not found. Starting with empty content.")
        except Exception as e:
            print(f"Error loading content: {e}")
    
    def _parse_content(self, content: str) -> None:
        """Parse the markdown content to extract existing rows"""
        lines = content.split('\n')
        in_main_table = False
        in_cross_ref_table = False
        
        for i, line in enumerate(lines, 1):
            # Identify main table section - check for both old and new formats
            if ("| Jira Issue | Jira Assignee | Upstream Velero Issue(s) | Upstream Velero Issue Labels |" in line or
                "| Row # | Jira Issue | Jira Assignee | Upstream Velero Issue(s) | Upstream Velero Issue Labels |" in line):
                in_main_table = True
                in_cross_ref_table = False
                continue
            # Identify cross-reference table section - check for both old and new formats
            elif ("| Velero Issue | Status | Labels | Associated OADP Issue(s) | Jira Assignee |" in line or
                  "| Row # | Velero Issue | Status | Labels | Associated OADP Issue(s) | Jira Assignee |" in line):
                in_main_table = False
                in_cross_ref_table = True
                continue
            elif line.startswith('|-------|') or line.startswith('|------------|'):
                # Skip separator lines for both old and new formats
                continue
            elif in_main_table and line.startswith('|') and '|' in line[1:]:
                # Parse main table row
                parsed_row = self._parse_main_table_row(line, i)
                if parsed_row:
                    self.existing_rows.append(parsed_row)
                    self._update_mapping(parsed_row)
            elif in_cross_ref_table and line.startswith('|') and '|' in line[1:]:
                # Parse cross-reference table row
                parsed_row = self._parse_cross_ref_table_row(line, i)
                if parsed_row:
                    self.existing_rows.append(parsed_row)
                    self._update_mapping(parsed_row)
            elif (in_main_table or in_cross_ref_table) and not line.startswith('|'):
                # End of current table
                in_main_table = False
                in_cross_ref_table = False
    
    def _parse_main_table_row(self, line: str, line_number: int) -> Optional[ParsedRow]:
        """Parse a main table row (format: | Row # | Jira Issue | Jira Assignee | Upstream Velero Issue(s) | Labels |)"""
        # Split by | and clean up
        parts = [part.strip() for part in line.split('|')]
        
        # Detect if this is old format (4 columns after first empty) or new format (5 columns after first empty)
        if len(parts) < 5:
            return None
        
        # Check if first column contains a row number (new format) or is the Jira issue (old format)
        has_row_number = False
        if len(parts) >= 6 and parts[1].isdigit():
            # New format with Row # column
            has_row_number = True
            jira_part = parts[2]
            assignee_part = parts[3]
            github_part = parts[4]
            labels_part = parts[5]
        else:
            # Old format without Row # column
            jira_part = parts[1]
            assignee_part = parts[2]
            github_part = parts[3]
            labels_part = parts[4]
        
        # Extract Jira key and summary
        jira_match = re.search(r'\[([^]]+)\]\([^)]+\)\s*-\s*(.+)', jira_part)
        if not jira_match:
            return None
            
        jira_key = jira_match.group(1)
        jira_summary = jira_match.group(2)
        
        # Extract GitHub issue numbers
        github_issues = []
        github_pattern = r'#(\d+)'
        github_matches = re.findall(github_pattern, github_part)
        github_issues = [int(match) for match in github_matches]
        
        return ParsedRow(
            jira_key=jira_key,
            jira_summary=jira_summary,
            assignee=assignee_part,
            github_issues=github_issues,
            github_labels=labels_part,
            raw_content=line,
            line_number=line_number
        )
    
    def _parse_cross_ref_table_row(self, line: str, line_number: int) -> Optional[ParsedRow]:
        """Parse a cross-reference table row (format: | Row # | Velero Issue | Status | Labels | Associated OADP Issue(s) | Jira Assignee |)"""
        # Split by | and clean up
        parts = [part.strip() for part in line.split('|')]
        
        # Detect if this is old format (5 columns after first empty) or new format (6 columns after first empty)
        if len(parts) < 6:
            return None
        
        # Check if first column contains a row number (new format) or is the Velero issue (old format)
        has_row_number = False
        if len(parts) >= 7 and parts[1].isdigit():
            # New format with Row # column
            has_row_number = True
            velero_part = parts[2]      # Velero Issue
            status_part = parts[3]      # Status
            labels_part = parts[4]      # Labels
            oadp_part = parts[5]        # Associated OADP Issue(s)
            assignee_part = parts[6]    # Jira Assignee
        else:
            # Old format without Row # column
            velero_part = parts[1]      # Velero Issue
            status_part = parts[2]      # Status
            labels_part = parts[3]      # Labels
            oadp_part = parts[4]        # Associated OADP Issue(s)
            assignee_part = parts[5]    # Jira Assignee
        
        # Extract OADP issue key from the OADP column
        oadp_match = re.search(r'\[([^]]+)\]\([^)]+\)\s*-?\s*(.*)', oadp_part)
        if not oadp_match:
            # Skip rows that don't reference OADP issues (like "*Not referenced by OADP issues*")
            return None
            
        jira_key = oadp_match.group(1)
        jira_summary = oadp_match.group(2) if oadp_match.group(2) else "Cross-referenced issue"
        
        # Extract GitHub issue number from Velero issue column
        github_issues = []
        github_pattern = r'#(\d+)'
        github_matches = re.findall(github_pattern, velero_part)
        github_issues = [int(match) for match in github_matches]
        
        return ParsedRow(
            jira_key=jira_key,
            jira_summary=jira_summary,
            assignee=assignee_part,
            github_issues=github_issues,
            github_labels=labels_part,
            raw_content=line,
            line_number=line_number
        )
    
    def _update_mapping(self, parsed_row: ParsedRow) -> None:
        """Update the Jira to GitHub mapping with a parsed row"""
        if parsed_row.jira_key not in self.jira_to_github_map:
            self.jira_to_github_map[parsed_row.jira_key] = set()
        self.jira_to_github_map[parsed_row.jira_key].update(parsed_row.github_issues)
    
    def check_for_duplicates(self, jira_key: str, github_issues: List[int]) -> Tuple[bool, Optional[ParsedRow]]:
        """
        Check if content already exists with same or different GitHub issues
        
        Returns:
            (is_duplicate, existing_row_if_found)
        """
        # Check if Jira key already exists
        existing_row = None
        for row in self.existing_rows:
            if row.jira_key == jira_key:
                existing_row = row
                break
        
        if not existing_row:
            return False, None
        
        # Compare GitHub issues as sets (order doesn't matter)
        existing_github_set = set(existing_row.github_issues)
        new_github_set = set(github_issues)
        
        # If GitHub issue sets are exactly the same, it's a duplicate (order doesn't matter)
        if existing_github_set == new_github_set:
            return True, existing_row
        
        # If GitHub issue sets are different, it's not a duplicate (should be updated)
        return False, existing_row
    
    def should_update_row(self, jira_key: str, github_issues: List[int]) -> Tuple[bool, Optional[ParsedRow]]:
        """
        Determine if a row should be updated based on different GitHub issue numbers
        
        Returns:
            (should_update, existing_row_if_found)
        """
        is_duplicate, existing_row = self.check_for_duplicates(jira_key, github_issues)
        
        if existing_row and not is_duplicate:
            # Row exists but with different GitHub issues - should update
            return True, existing_row
        
        return False, existing_row
    
    def get_content_summary(self) -> Dict:
        """Get summary of existing content"""
        summary = {
            'total_rows': len(self.existing_rows),
            'jira_issues': list(self.jira_to_github_map.keys()),
            'github_issues_count': sum(len(issues) for issues in self.jira_to_github_map.values()),
            'unique_github_issues': len(set().union(*self.jira_to_github_map.values()) if self.jira_to_github_map else set())
        }
        return summary
    
    def print_content_analysis(self) -> None:
        """Print analysis of existing content"""
        summary = self.get_content_summary()
        
        print("\n=== Content Analysis ===")
        print(f"Total rows: {summary['total_rows']}")
        print(f"Unique Jira issues: {len(summary['jira_issues'])}")
        print(f"Total GitHub issue references: {summary['github_issues_count']}")
        print(f"Unique GitHub issues: {summary['unique_github_issues']}")
        
        print("\n=== Jira to GitHub Mapping ===")
        for jira_key, github_issues in sorted(self.jira_to_github_map.items()):
            github_list = ', '.join(f"#{issue}" for issue in sorted(github_issues))
            print(f"{jira_key}: {github_list}")


def main():
    """Test the content checker"""
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python content_checker.py <markdown_file_path>")
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    
    checker = MarkdownContentChecker(markdown_file)
    checker.load_existing_content()
    checker.print_content_analysis()
    
    # Example usage - check for duplicates
    test_cases = [
        ("OADP-3971", [8692, 7767]),  # Should be duplicate
        ("OADP-3971", [8692]),        # Should need update (different GitHub issues)
        ("OADP-9999", [1234]),        # Should be new
    ]
    
    print("\n=== Duplicate Check Tests ===")
    for jira_key, github_issues in test_cases:
        is_duplicate, existing_row = checker.check_for_duplicates(jira_key, github_issues)
        should_update, _ = checker.should_update_row(jira_key, github_issues)
        
        print(f"\nTest: {jira_key} with GitHub issues {github_issues}")
        print(f"  Is duplicate: {is_duplicate}")
        print(f"  Should update: {should_update}")
        if existing_row:
            print(f"  Existing GitHub issues: {existing_row.github_issues}")


if __name__ == "__main__":
    main()
