from PyQt5.QtWidgets import QFileDialog
from backend.file_organizer import FileOrganizer

class UiLogic:
    def __init__(self, ui):
        self.ui = ui
        self.ui.selectFolderBtn.clicked.connect(self.select_folder)

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory()
        if folder_path:
            organizer = FileOrganizer(folder_path)
            organizer.organize_files()
