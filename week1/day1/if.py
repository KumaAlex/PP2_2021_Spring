a = 50
b = 10
if a > b:
  print("Hello World")

a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")

a = 50
b = 10
if a == b:
  print("1")
elif a > b: #else if
  print("2")
else:
  print("3")

#and --> and
#or --> or

if 5 > 2: print("Five is greater than two!") 
#можно на 1 строке

print("Yes") if 5 > 2 else print("No")
#можно на 1 строке но структура другая

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
#=