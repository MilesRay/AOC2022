f = open("Day1.txt")
r = f.read()
s = r.split('\n')
highest = 0
count = 0

#part 1

for cell in range(len(s)):
    if not s[cell]:
        if(count > highest):
            highest = count
        count = 0
    else:
        count += int(s[cell])

# print(highest)


# Part 2

count = 0
highest = 0
second = 0
third = 0

for cell in range(len(s)):
    if not s[cell]:
        if(count > highest):
            third = second
            second = highest
            highest = count
            count = 0
        elif(count > second):
            third = second
            second = count
            count = 0
        elif(count > third):
            third = count
            count = 0
        count = 0
    else:
        count += int(s[cell])

total = highest + second + third

print(highest)
print(second)
print(third)
print(total)