#!/usr/bin/env python3
"""
Test script for the undo functionality of FileOrganizer
"""

import os
import tempfile
import shutil
from backend.file_organizer import FileOrganizer

def create_test_files(test_dir):
    """Create test files in different categories."""
    test_files = [
        "test1.txt",      # Documents
        "test2.pdf",      # Documents
        "test3.jpg",      # Images
        "test4.png",      # Images
        "test5.py",       # Code Files
        "test6.js"        # Code Files
    ]
    
    for file_name in test_files:
        file_path = os.path.join(test_dir, file_name)
        with open(file_path, 'w') as f:
            f.write(f"Test content for {file_name}")
    
    print(f"Created {len(test_files)} test files in {test_dir}")

def test_undo_functionality():
    """Test the undo functionality."""
    # Create temporary directories
    with tempfile.TemporaryDirectory() as temp_dir:
        source_dir = os.path.join(temp_dir, "source")
        dest_dir = os.path.join(temp_dir, "destination")
        
        os.makedirs(source_dir)
        os.makedirs(dest_dir)
        
        print(f"Testing with source: {source_dir}")
        print(f"Testing with destination: {dest_dir}")
        
        # Create test files
        create_test_files(source_dir)
        
        # List files before organization
        print("\nFiles before organization:")
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                print(f"  {os.path.join(root, file)}")
        
        # Create organizer and organize files
        print("\nOrganizing files...")
        organizer = FileOrganizer(source_dir, dest_dir)
        organizer.organize()
        
        # Check if undo is available
        print(f"\nCan undo: {organizer.can_undo()}")
        undo_info = organizer.get_undo_info()
        if undo_info:
            print(f"Undo info: {undo_info}")
        
        # List files after organization
        print("\nFiles after organization:")
        for root, dirs, files in os.walk(dest_dir):
            for file in files:
                print(f"  {os.path.join(root, file)}")
        
        # Test undo functionality
        print("\nTesting undo...")
        success = organizer.undo()
        print(f"Undo success: {success}")
        
        # List files after undo
        print("\nFiles after undo:")
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                print(f"  {os.path.join(root, file)}")
        
        # Check if undo is still available
        print(f"\nCan undo after undo: {organizer.can_undo()}")

if __name__ == "__main__":
    test_undo_functionality()
