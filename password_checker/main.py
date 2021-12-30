import requests
import hashlib
import sys

password = sys.argv[1]
sha = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
url = 'https://api.pwnedpasswords.com/range/' + sha[0:5]
print(f'Calling {url}')
tail = sha[5:]
resp = requests.get(url)
counter = 0
for returnedHash in resp.text.splitlines():
    if returnedHash.startswith(tail):
        counter = returnedHash.split(":")[1]

if counter:
    print(f'Your password is found {counter} times')
else:
    print('Your password is not found')