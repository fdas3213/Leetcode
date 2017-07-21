    def mySqrt(self, x):
        if x == 0:
            return 0
        
        guess = 1
        quotient = x / guess
        
        while abs(guess * guess - x) > 0.001:
            mean = (guess + quotient) / 2
            guess = mean
            quotient = x / guess
            
        return int(guess)
