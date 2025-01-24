def fibonacci_series(n):
    
    if n <= 0:
        print("Please enter a positive integer.")
        return
    elif n == 1:
        print("Fibonacci series: 0")
        return
    elif n == 2:
        print("Fibonacci series: 0, 1")
        return


    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    
    print("Fibonacci series:", ", ".join(map(str, fib)))


n = int(input("Enter the number of terms: "))
fibonacci_series(n)
