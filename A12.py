def detach_file_example(file_path):
    with open(file_path, 'wb') as file:
        buffer = file.detach()
        return buffer
