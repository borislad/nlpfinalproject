import os

def build_file_path(directory, filename):
    # Create the full file path using os.path.join()
    file_path = os.path.abspath(os.getcwd()) + os.path.join(directory, filename)
    return file_path