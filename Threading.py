import threading
import time

# Function to simulate a time-consuming task
def task(name, duration):
    print(f"Thread {name}: Starting")
    time.sleep(duration)
    print(f"Thread {name}: Completed after {duration} seconds")

# 1. Creating and starting threads
thread1 = threading.Thread(target=task, args=("Thread-1", 2))
thread2 = threading.Thread(target=task, args=("Thread-2", 3))

thread1.start()
thread2.start()

# 2. Waiting for threads to finish
thread1.join()
thread2.join()

# 3. Daemon threads (threads that run in the background)
daemon_thread = threading.Thread(target=task, args=("Daemon-Thread", 1))
daemon_thread.daemon = True  # Mark the thread as a daemon thread
daemon_thread.start()

# Main thread continues to execute while daemon thread runs in the background

# 4. Thread synchronization with locks
counter = 0
lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(1000000):
        with lock:
            counter += 1

# Create and start two threads to increment the counter
thread3 = threading.Thread(target=increment_counter)
thread4 = threading.Thread(target=increment_counter)

thread3.start()
thread4.start()

thread3.join()
thread4.join()

print(f"Final Counter Value: {counter}")

# Note: Ensure you have a clear understanding of the threading concepts and the Global Interpreter Lock (GIL) in Python.
