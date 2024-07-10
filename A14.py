def file_descriptor_example(file_path):
    with open(file_path, 'r') as file:
        return file.fileno()
