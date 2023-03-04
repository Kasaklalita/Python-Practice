m = ""
s =

for i in range(len(s)):
    # iterating through the string from the last
    for j in range(len(s), i, -1):
        # ensuring that we do not iterate through more than half of
        # the string
        if len(m) >= j-i:
            break
        elif s[i:j] == s[i:j][::-1]:
            m = s[i:j]

print(m)
