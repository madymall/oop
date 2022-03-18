import re

text = "Hello!! My name is Jack."

"""
    re.search  первый попавшийся
"""

# result = re.search('l', text)
# print(result)
# print(text[result.start()])

"""
    re.findall
"""
# result = re.findall('l', text)
# print(result)

"""
    re.match
    Is Valid Phone Number?
"""

# phone = input("Phone number: ")
# result = re.match(r"\+([0-9]{1,3})-")