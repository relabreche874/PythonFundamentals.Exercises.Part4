def fibonacci(num) :
    
    a = 0
    b = 1
    
    for i in range(1, num) :
        c = a + b
        a = b
        b = c
        
    return c

print(fibonacci(5))
print(fibonacci(7))