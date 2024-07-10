import threading

def thread_function():
    print("Thread is running.")

thread = threading.Thread(target=thread_function)
thread.start()
