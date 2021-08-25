class Solution:
    def solve(self, n):

        fizzBuzz = []

        for i in range(1, n + 1):

            if i % 15 == 0:
                fizzBuzz.append('FizzBuzz')
            elif i % 3 == 0:
                fizzBuzz.append('Fizz')
            elif i % 5 == 0:
                fizzBuzz.append('Buzz')
            else:
                fizzBuzz.append(str(i))
        
        return fizzBuzz
            