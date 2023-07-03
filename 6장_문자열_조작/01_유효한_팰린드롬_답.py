a = input()

b, c = "", ""

for i in a:
    if i.isalnum():
        b += i.lower()

c = b[::-1]

if b == c:
    print("true")
else:
    print("false")