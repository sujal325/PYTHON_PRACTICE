def prime():
    n = int(input("Give number: "))
    for i in range(2, n):
        if n % i == 0:
            print("This number is not prime number.")
            break
    else:
        print("It is a prime number.")


prime()