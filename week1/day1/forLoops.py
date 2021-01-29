fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 

#apple
#banana
#cherry

for x in range(2, 30, 3):
  print(x) 
"""
2
5
8
11
14
17
20
23
26
29
"""

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

"""
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry
"""