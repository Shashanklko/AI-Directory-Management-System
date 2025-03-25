import os
import shutil
import json
from backend.utils import get_file_extension  # Ensure this function is defined correctly

class FileOrganizer:
    def __init__(self, directory, save_directory=None):
        self.directory = directory
        self.save_directory = save_directory or directory
        self.original_locations = {}

        # File type categorization
        self.categories = {
            "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
            "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
            "Videos": [".mp4", ".avi", ".mov", ".mkv"],
            "Audio": [".mp3", ".wav", ".aac", ".flac"],
            "Code Files": [".py", ".js", ".html", ".css", ".java", ".cpp", ".cs", "c#", "c++"],
            "Archives": [".zip", ".rar", ".tar", ".7z"],
            "Executables": [".exe", ".msi", ".bat", ".sh"]
        }

    def _categorize_file(self, file_path):
        _, ext = os.path.splitext(file_path)
        for category, extensions in self.categories.items():
            if ext.lower() in extensions:
                return category
        return "Others"

    def organize(self):
        """Organizes files based on detected categories."""
        for root, _, files in os.walk(self.directory):
            for file in files:
                file_path = os.path.join(root, file)
                category = self._categorize_file(file_path)

                # Store original location for undo feature
                self.original_locations[file_path] = file_path

                # Move file
                self._move_file(file_path, category)

        # Save original locations for undo functionality
        self._save_original_locations()

    def _move_file(self, file_path, category):
        """Moves a file to its categorized folder."""
        category_folder = os.path.join(self.save_directory, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        destination_path = os.path.join(category_folder, os.path.basename(file_path))
        shutil.move(file_path, destination_path)
        print(f"Moved {file_path} → {destination_path}")

    def _save_original_locations(self):
        """Stores file paths before organizing, for undo functionality."""
        backup_file = os.path.join(self.save_directory, "backup.json")
        with open(backup_file, "w") as f:
            json.dump(self.original_locations, f)

    def undo(self):
        """Restores files to their original locations."""
        backup_file = os.path.join(self.save_directory, "backup.json")
        if os.path.exists(backup_file):
            with open(backup_file, "r") as f:
                original_locations = json.load(f)

            for new_location, old_location in original_locations.items():
                if os.path.exists(new_location):
                    shutil.move(new_location, old_location)
                    print(f"Restored {new_location} → {old_location}")

            os.remove(backup_file)
            print("Undo successful.")
        else:
            print("No backup found. Undo not possible.")
