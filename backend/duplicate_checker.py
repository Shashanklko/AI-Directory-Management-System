import os
import hashlib

class DuplicateChecker:
    def __init__(self, directory):
        self.directory = directory
        self.file_hashes = {}

    def find_duplicates(self):
        duplicates = []
        for root, _, files in os.walk(self.directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_hash = self._get_file_hash(file_path)
                if file_hash in self.file_hashes:
                    duplicates.append(file_path)
                else:
                    self.file_hashes[file_hash] = file_path
        return duplicates

    def _get_file_hash(self, file_path):
        hasher = hashlib.md5()
        with open(file_path, "rb") as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()
