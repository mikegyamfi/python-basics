name = "Michael Gyamfi"
phone_number = 242442147
age = 12

# print(name)
# print(age)
# print(phone_number)

mikes_info = {
    "name": "Mike",
    "age": 12,
    "hobbies" : {
        "outdoor": ["Football", "Basketball"],
        "indoor": ["Something", "Something"]
    }
}

hobbies = mikes_info["hobbies"]
print(f"My hobbies are {hobbies}")

outdoor = hobbies["outdoor"]
print(f"Outdoor hobbies are {outdoor}")
