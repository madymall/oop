import re

email = "emailkmkmj@mail.com"
result = re.match(r"^([a-zA-Z0-9]{5,30})@(gmail|mail|yandex|icloud|namba).(ru|com|kg)", email)

print(result)