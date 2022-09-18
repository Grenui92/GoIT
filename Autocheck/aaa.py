first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))
print(first, second)
while first!=second:
   if first > second:
      first -= 1
   else:
      second -= 1
gcd=first
print(gcd)