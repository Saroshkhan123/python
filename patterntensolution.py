#Pattern-Ten solution

n = int(input())
spaces = 0


for row in range(n, 0, -1):
   for space in range(spaces):
       print(" ", end = "")
      
   spaces += 1
  
   for star in range(2 * row - 1):
       print("*", end = "")
   print()
