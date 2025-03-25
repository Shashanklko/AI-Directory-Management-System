import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog
from backend.file_organizer import FileOrganizer

class FileOrganizerGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.selected_directory = None
        self.organizer = None
        self.init_ui()
        self.setAcceptDrops(True)  # ✅ Enable drag & drop

    def init_ui(self):
        self.setWindowTitle("AI Directory Organizer")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Drag & Drop a Folder Here or Choose One", self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.choose_button = QPushButton("Choose Folder", self)
        self.choose_button.clicked.connect(self.choose_folder)
        layout.addWidget(self.choose_button)

        self.organize_btn = QPushButton("Organize Files", self)
        self.organize_btn.clicked.connect(self.organize_files)
        layout.addWidget(self.organize_btn)

        self.undo_btn = QPushButton("Undo Last Organization", self)
        self.undo_btn.clicked.connect(self.undo_last)
        layout.addWidget(self.undo_btn)

        self.setLayout(layout)

    def dragEnterEvent(self, event):
        """Handles drag event."""
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        """Handles file drop event."""
        urls = event.mimeData().urls()
        if urls:
            folder_path = urls[0].toLocalFile()
            if os.path.isdir(folder_path):  # ✅ Ensure it's a folder
                self.selected_directory = folder_path
                self.label.setText(f"Selected: {folder_path}")

    def choose_folder(self):
        """Opens file dialog to select folder."""
        folder = QFileDialog.getExistingDirectory(self, "Select Folder to Organize")
        if folder:
            self.selected_directory = folder
            self.label.setText(f"Selected: {folder}")

    def organize_files(self):
        """Organizes the selected folder."""
        if not self.selected_directory:
            self.label.setText("Please select a folder first.")
            return

        save_directory = QFileDialog.getExistingDirectory(self, "Select Save Directory")
        if not save_directory:
            save_directory = self.selected_directory  # ✅ Default to same folder

        self.organizer = FileOrganizer(self.selected_directory, save_directory)
        self.organizer.organize()
        self.label.setText("Files organized successfully!")

    def undo_last(self):
        """Undo last organization action."""
        if self.organizer:
            self.organizer.undo()
            self.label.setText("Undo completed!")

def main():
    app = QApplication(sys.argv)
    window = FileOrganizerGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
