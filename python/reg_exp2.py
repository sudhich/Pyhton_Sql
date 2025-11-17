import re


# val=re.findall(r"(ab)+", "ababab hdfhdh ab ab")
# print(val)

# val=re.findall(r"(?:ab)+", "ababab hdfhdh ab ab")
# print(val)

result = re.findall(r"a(?=b)", "abc ac ab aab abb")
print(result)