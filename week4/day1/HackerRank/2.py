regex_pattern = r"[.,]"
import re
print("\n".join(re.split(regex_pattern, input())))
'''
import re
x = re.split(r"[.,]", input())
for i in x:
    print(i)
'''