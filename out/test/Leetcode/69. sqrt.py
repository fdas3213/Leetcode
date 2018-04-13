    def mySqrt(self, x):
        if x == 0:
        return 0

        guess = x
        while guess * guess > x:
            guess = 1/2 * (guess + x / guess)
        
        return guess
