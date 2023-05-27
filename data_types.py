def contains_test(str):
    if str.endswith("test"):
        print("found test")
    else:
        print("no test")


str = "Hello World"
str2 = "Bonjour Monde"

contains_test(str)
contains_test(str2)

nums = [1, 100, 200, 2, 9, 12]

for num in nums:
    if num > 10:
        print("number is large", num)
    elif num <= 10:
        print("number is small", num)
