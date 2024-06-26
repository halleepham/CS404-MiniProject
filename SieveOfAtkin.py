import random
import time

# Source: modified version from GeeksforGeeks
# https://www.geeksforgeeks.org/sieve-of-atkin/
def SieveOfAtkin(limit):
  # 2 and 3 are known to be prime
  if limit > 2:
      print(2, end=" ")
  if limit > 3:
      print(3, end=" ")

  # Initialise the sieve array with False values
  sieve = [False] * (limit + 1)
  for i in range(0, limit + 1):
      sieve[i] = False
  x = 1
  while x * x <= limit:
      y = 1
      while y * y <= limit:

          # Main part of
          # Sieve of Atkin
          n = (4 * x * x) + (y * y)
          if (n <= limit and (n % 12 == 1 or
                              n % 12 == 5)):
              sieve[n] ^= True

          n = (3 * x * x) + (y * y)
          if n <= limit and n % 12 == 7:
              sieve[n] ^= True

          n = (3 * x * x) - (y * y)
          if (x > y and n <= limit and
                  n % 12 == 11):
              sieve[n] ^= True
          y += 1
      x += 1

  # Mark all multiples of squares as non-prime
  r = 5
  while r * r <= limit:
      if sieve[r]:
          for i in range(r * r, limit+1, r * r):
              sieve[i] = False
      r += 1
      # Print primes using sieve[]
  for a in range(5, limit+1):
      if sieve[a]:
          print(a)

# Driver Code
limit = random.randint(100000,999999)
print("Following are the prime numbers smaller")
print("than or equal to", limit, "\n")
start_time = time.time()
SieveOfAtkin(limit)
end_time = time.time()
print("\nTime taken: ", end_time - start_time, " seconds")
