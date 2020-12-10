#import primefac
import sys
import math

# checking for prime
def is_prime(n):
   # checking for less than 1
   if n <= 1:
      return False
   # checking for 2
   elif n == 2:
      return True
   elif n > 2 and n % 2 == 0:
      return False
   else:
      # iterating loop till square root of n
      for i in range(3, int(math.sqrt(n)) + 1, 2):
         # checking for factor
         if n % i == 0:
            # return False
            return False
      # returning True
      return True

# This function computes the factor of the argument passed
def print_factors(x):
   print(f'The factors of {x} are (primes are labelled by "*"):')
   for i in range(1, x + 1):
       if x % i == 0:
           if is_prime(i): print(f'{i}*')
           else: print(i)



if len(sys.argv) < 2: n=3
else: n = int( sys.argv[1] )
#factors = list( primefac.primefac(n) )
#print('\n'.join(map(str, factors)))

print_factors(n)
