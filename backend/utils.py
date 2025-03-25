import os
import hashlib

def get_file_extension(file_name):
    return os.path.splitext(file_name)[1].lower()

def generate_file_hash(file_path):
    hasher = hashlib.md5()
    with open(file_path, "rb") as f:
        hasher.update(f.read())
    return hasher.hexdigest()
