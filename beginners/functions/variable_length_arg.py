
# We can pass a variable number of arguments to a function using special symbols: *args, **kwargs

def numbers(*args):
    for arg in args:
        print(arg)

def words(arg1, *args):
    print(f"First Arg: {arg1}")
    for arg in args:
        print(f"Others: {arg}")


print(numbers(2,3,4,5,6))
print(words("Hello,", "how", "are", "you!"))