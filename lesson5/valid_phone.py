import re

phone = "+996-707-77-77-773"

result = re.match(r"^\+([0-9]{1,3})-([0-9]{1,3})-([0-9]{2})-([0-9]{2})-([0-9]{2})", phone)
print(result)

try:
    if phone[result.start():result.end()] == phone:
        print("Phone Number Valid!")
    else:
        raise "Is not valid phone number!"
except:
    print("Is not valid phone number!")

