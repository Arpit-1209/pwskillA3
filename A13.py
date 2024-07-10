def seek_example(file_path):
    with open(file_path, 'r') as file:
        file.seek(10)
        return file.read()
