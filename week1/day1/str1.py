a = "Hello, World!"
print(a[1])
#e

for x in "banana":
  print(x)
#b a n a n a

a = "Hello, World!"
print(len(a))
#like a.size() in c++
#13

txt = "The best things in life are free!"
print("free" in txt)
print("Free" in txt)
print("T" in txt)
#True
#false
#True
#words in str

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)
#True

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")
#Yes, 'expensive' is NOT present.

