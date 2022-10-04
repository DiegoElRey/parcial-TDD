

class IsPrimeService:

    def validate_number(self,number: int):
        if number < 2 or number <=0: return False
        remainderCount = self.calculate_is_prime_number(number)
        return True if remainderCount==0 else False

    def calculate_is_prime_number(number: int):
        remainderCount = 0
        for i in range(2, number):
            remainder = number % i
            if remainder == 0: remainderCount+=1
        return remainderCount