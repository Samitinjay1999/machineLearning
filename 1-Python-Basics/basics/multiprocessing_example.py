import multiprocessing

import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square of {i} is {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube of {i} is {i*i*i}")

if __name__ == "__main__":
    # Create 2 processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    start_time = time.time()
    
    # Start the processes
    p1.start()
    p2.start()

    # Wait for completion of processes
    p1.join()
    p2.join()
    
    end_time = time.time()
    finished_time = end_time - start_time
    
    print(f"Time taken: {finished_time:.2f} seconds")
