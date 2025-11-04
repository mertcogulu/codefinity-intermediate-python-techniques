import time

# Step 2: Define the decorator
def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Start time
        result = func(*args, **kwargs)  # Call the function
        end_time = time.time()  # End time
        print(f"{func.__name__} took {end_time - start_time} seconds")
        return result
    return wrapper

# Step 4: Apply the decorator
@time_it
def factorial(n):
    """Function to compute factorial of a number"""
    return 1 if n == 0 else n * factorial(n - 1)

# Step 5: Test the decorator
print(factorial(10))  # Replace with any number to test