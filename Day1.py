f = open("Day1.txt")
r = f.read()
s = r.split('\n')
highest = 0
count = 0
for cell in range(len(s)):
    if not s[cell]:
        if(count > highest):
            highest = count
        count = 0
    else:
        count += int(s[cell])

print(highest)
