def fibo():
    z = 0
    n = int(input("n: "))
    fibo = 0
    for i in range(1, n):
        fibo = i + z
        z += 1
        print(fibo)


fibo()
