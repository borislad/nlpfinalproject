import os

def build_file_path(directory, filename):
    # Create the full file path using os.path.join()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    file_path = os.path.abspath(parent_directory) + os.path.join(directory, filename)
    print("File Path:", file_path)
    return file_path