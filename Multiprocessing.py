import multiprocessing
import time

# Function to simulate a time-consuming task
def task(name, duration):
    print(f"Process {name}: Starting")
    time.sleep(duration)
    print(f"Process {name}: Completed after {duration} seconds")

# 1. Creating and starting processes
process1 = multiprocessing.Process(target=task, args=("Process-1", 2))
process2 = multiprocessing.Process(target=task, args=("Process-2", 3))

process1.start()
process2.start()

# 2. Waiting for processes to finish
process1.join()
process2.join()

# 3. Pool of processes
def square_number(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
with multiprocessing.Pool(processes=3) as pool:
    result = pool.map(square_number, numbers)

print("Squared Numbers:", result)

# 4. Sharing state between processes with Value and Array
shared_value = multiprocessing.Value('i', 0)  # 'i' represents signed integer

def increment_shared_value():
    for _ in range(1000000):
        with shared_value.get_lock():
            shared_value.value += 1

# Create and start two processes to increment the shared value
process3 = multiprocessing.Process(target=increment_shared_value)
process4 = multiprocessing.Process(target=increment_shared_value)

process3.start()
process4.start()

process3.join()
process4.join()

print(f"Final Shared Value: {shared_value.value}")

# Note: Ensure you have a clear understanding of the multiprocessing concepts and differences between multiprocessing and multithreading in Python.
