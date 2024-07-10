from multiprocessing import Process

def process_function():
    print("Process is running.")

process = Process(target=process_function)
process.start()
process.join()
