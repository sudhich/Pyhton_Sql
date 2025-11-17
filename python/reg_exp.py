import re
target_string = "The price of PINEAPPLE ice cream is 20Itismumber"

# two groups enclosed in separate ( and ) bracket
result = re.search(r"(\b[A-Z]+\b).+(\b\d+)", target_string)

# Extract matching values of all groups
print(result.group())
print(result.group(2))
# # Output ('PINEAPPLE', '20')

# # Extract match value of group 1
# print(result.group(1))
# # Output 'PINEAPPLE'

# # Extract match value of group 2
# print(result.group(2))
# #Check if something exists ahead
# #a(?=b)👉 Meaning: “Match a only if it is followed by b.”
# #❌ In the string "ac", it won’t match, because a is not followed by b.
# #(?=.*[0-9])===Hello2 ✅ Matches (because there is 2 ahead).
# #If string = "Hello", ❌ no match (because there’s no digit ahead).

# #^(?=.*[A-Z])(?=.*[0-9])==(?=.*[A-Z]) → there must be at least one capital letter
# #(?=.*[0-9]) → there must be at least one number 
# #✅ "Hello2" → has both
# #❌ "hello2" → no uppercase
# #❌ "HELLO" → no digit
# #| Pattern       | Meaning                                    | Example Match  |
# #| ------------- | ------------------------------------------ | -------------- |
# #| `a(?=b)`      | `a` only if followed by `b`                | `ab` ✅, `ac` ❌ |
# #| `(?=abc)`     | position before `abc`                      | `abcdef` ✅     |
# #| `(?=.*\d)`    | must contain at least one digit            | `abc1` ✅       |
# #| `(?=.*[A-Z])` | must contain at least one uppercase letter | `abC` ✅        |
