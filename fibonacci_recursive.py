def fibonacci(num) :
    if num == 0 :
        return 0
    
    elif num == 1 :
        return 1
    
    else :
        return fibonacci(num - 1) + fibonacci(num - 2)
    
print(fibonacci(7))
print(fibonacci(5))
print(fibonacci(3))
print(fibonacci(30))