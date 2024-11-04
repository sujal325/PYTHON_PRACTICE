
# wrong code

class prime:
    def __init__(self, value):
        self.value = value

    def prime_number(self):
        for i in range(2, ((self.value) - 1)):
            if self.value % i == 0:
                print("Not prime")
                break
            else:
                return "prime"

    def hundredth_prime(self):
        num = self.value
        i = 2
        count = 2
        while True:
            for i in range(2, num - 1):
                if num % i == 0:
                    break
                else:
                    count += 1
                if count == 100:
                    return num


number = prime(12)
number.prime_number()
number.hundredth_prime()
