# Decorators Guide

# 1. Simple decorator
def simple_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@simple_decorator
def hello():
    print("Hello, world!")

# Calling the decorated function
hello()

# 2. Decorator with parameters
def param_decorator(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix}: Before function execution")
            result = func(*args, **kwargs)
            print(f"{prefix}: After function execution")
            return result
        return wrapper
    return decorator

@param_decorator("LOG")
def greet(name):
    print(f"Hello, {name}!")

# Calling the decorated function with parameters
greet("Alice")

# 3. Class-based decorator
class ClassDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before function execution (class-based)")
        result = self.func(*args, **kwargs)
        print("After function execution (class-based)")
        return result

@ClassDecorator
def example_function():
    print("Inside the function")

# Calling the decorated function (class-based)
example_function()

# 4. Using functools.wraps to preserve function metadata
from functools import wraps

def preserving_metadata_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function docstring"""
        print("Decorator: Before function execution")
        result = func(*args, **kwargs)
        print("Decorator: After function execution")
        return result
    return wrapper

@preserving_metadata_decorator
def function_with_metadata():
    """Original function docstring"""
    print("Inside the function with metadata")

# Calling the decorated function (preserving metadata)
function_with_metadata()
print("Function Docstring:", function_with_metadata.__doc__)

# Note: Decorators are a powerful feature in Python and are commonly used for aspects like logging, authorization, and memoization.
