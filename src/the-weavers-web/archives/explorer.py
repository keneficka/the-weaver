#!/usr/bin/env python3
"""
Weave Explorer - A command-line interface for traversing the tapestry
Navigate through the weave's directories, list contents, and examine threads...
"""

import os
import sys
from pathlib import Path


class WeaveExplorer:
    """Command-line explorer for navigating the weave structure"""
    
    def __init__(self):
        # The base path is one level up from this script (the 'projects' root)
        self.base_path = Path(__file__).resolve().parent.parent
        
        # The current_dir is what we want to explore - the projects folder itself
        self.current_dir = self.base_path
    
    def list_contents(self, subpath='.'):
        """List contents of a folder within the tapestry"""
        
        target = self.current_dir / subpath
        
        if not target.exists():
            print("Thread broken at: " + subpath)
            return []
        
        contents = []
        
        for item in sorted(target.iterdir()):
            info = {
                'name': item.name,
                'type': 'folder' if item.is_dir() else 'file',
                'size': ''
            }
            
            if item.is_file():
                try:
                    stat = item.stat()
                    info['size'] = str(stat.st_size) + " bytes"
                except:
                    info['size'] = "? bytes"
            
            contents.append(info)
        
        return contents
    
    def explore_recursive(self, subpath='.', depth=0):
        """Recursively explore a folder and its contents"""
        
        indent = "  " * depth
        target = self.current_dir / subpath
        
        if not target.exists():
            print(indent + str(subpath) + ": thread severed")
            return []
        
        print(indent + str(subpath) + "/")
        
        if target.is_file():
            print(indent + "  - [FILE] " + target.name)
            return [target]
        
        contents = list(target.iterdir())
        folder_count = 0
        file_count = 0
        
        for item in sorted(contents):
            if item.is_dir():
                folder_count += 1
                print(indent + "[DIR]  " + item.name + "/")
                # Recurse into folders (limit depth)
                if depth < 3:
                    self.explore_recursive(str(item.relative_to(self.current_dir)), depth + 1)
            else:
                file_count += 1
                try:
                    file_size = item.stat().st_size
                    size_str = " (" + str(file_size) + " bytes)" if file_size < 1_000_000 else ""
                    print(indent + "[FILE]  " + item.name + size_str)
                except:
                    print(indent + "[FILE]  " + item.name)
        
        return contents
    
    def get_project_summary(self):
        """Generate a summary of all projects in the weave"""
        
        total_folders = 0
        total_files = 0
        project_types = []
        
        for item in self.current_dir.iterdir():
            if item.is_dir() and not item.name.startswith('__'):
                folder_name = item.name.replace('_', ' ').title()
                project_types.append(folder_name)
                total_folders += 1
                
                # Count files in this project
                try:
                    file_count = sum(1 for f in item.rglob('*') if f.is_file())
                    total_files += file_count
                except:
                    pass
        
        print("=" * 70)
        print("WEAVE EXPLORER - PROJECT SUMMARY")
        print("=" * 70)
        print("\nTotal Projects: " + str(total_folders))
        print("Total Files: " + str(total_files) + ",")
        
        if project_types:
            print("\nProject Types:")
            for proj_type in sorted(project_types):
                print("  - " + proj_type)
        
        return total_folders, total_files
    
    def navigate(self, path='.'):
        """Navigate to a specific subdirectory within the weave"""
        
        target = self.current_dir / path
        
        if not target.exists():
            print("Thread broken: " + path + " does not exist")
            return False
        
        print("=" * 70)
        print("NAVIGATED TO: " + str(path) + "/")
        print("=" * 70)
        
        contents = self.list_contents(path)
        
        for item in contents:
            status = "[DIR]" if item['type'] == 'folder' else "[FILE]"
            size = item.get('size', '')
            print(status + " " + item['name'] + size)
        
        return True
    
    def show_project_types(self):
        """List all unique project types in the weave"""
        
        project_types = []
        
        for item in self.current_dir.iterdir():
            if item.is_dir() and not item.name.startswith('__'):
                clean_name = item.name
                # Simple title conversion
                display_name = ' '.join(part.capitalize() for part in clean_name.split('_'))
                project_types.append(display_name)
        
        print("=" * 70)
        print("PROJECT TYPES IN THE WEAVE")
        print("=" * 70)
        
        for idx, proj_type in enumerate(sorted(project_types), 1):
            emoji = "DIR" if idx % 2 == 1 else "FILE"
            print(str(idx) + ". DIR  " + proj_type)
        
        return sorted(project_types)


def main():
    """Main CLI interface for the weave explorer"""
    
    explorer = WeaveExplorer()
    
    # Show initial summary
    explorer.get_project_summary()
    
    # Show project types
    print("\n\n")
    explorer.show_project_types()
    
    # Offer to navigate
    print("\n\nTo navigate to a specific directory, provide its name as an argument.")
    print("Or leave empty to show the projects root.")
    
    return 0


if __name__ == '__main__':
    main()
