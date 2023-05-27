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
nums2 = [2, -1, 100]


def check_numbers(arr):
    for num in arr:
        if num > 10:
            print("number is large", num)
        elif num <= 10:
            print("number is small", num)


check_numbers(nums)
check_numbers(nums2)

client = {
    "username": "user_one",
    "age": 30,
    "friends": ["friend_one", "friend_two", "friend_three"],
}

print(client["username"], client["age"])

for friend in client["friends"]:
    print(friend)

clients = [
    {
        "username": "user_one",
        "age": 30,
        "friends": ["friend_one", "friend_two", "friend_three"],
    },
    {
        "username": "user_two",
        "age": 25,
        "friends": ["friend_four", "friend_five", "friend_six"],
    },
]

for client in clients:
    print(client["username"], client["age"])
    for friend in client["friends"]:
        print(friend)
