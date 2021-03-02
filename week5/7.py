s=input()
print(len(list(filter(lambda x: x.isupper(),s))))
print(len(list(filter(lambda x: x.islower(),s))))