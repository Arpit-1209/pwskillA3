def close_file_example(file_path):
    file = open(file_path, 'w')
    file.write('Writing to the file.')
    file.close()
