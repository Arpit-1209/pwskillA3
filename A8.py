def read_file_buffered(file_path):
    with open(file_path, 'r', buffering=8192) as file:
        return file.read()
