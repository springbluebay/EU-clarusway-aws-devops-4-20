
def makeBox(n):
  times =0 

  if n==1:
    print('#')
    return
  else:
    top="#"*n
    middle="#" + " "*(n-2) + "#"
    bottom= "#"*n

  print(top)
  while times < n-2:
    print(middle)
    times+=1
  print(bottom)

size = int(input("Please enter the side length of the box: "))

makeBox(size)	
