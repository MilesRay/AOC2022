f = open("Day2.txt")
r = f.read()
s = r.split('\n')
a = []
total = 0
for column in range(len(s)-1):
    temp = s[column].split(' ')
    if (temp[1] == 'X'):
        temp[1] = 'A' 
        total += 1
    if (temp[1] == 'Y'):
        temp[1] = 'B' 
        total += 2
    if (temp[1] == 'Z'):
        temp[1] = 'C' 
        total += 3
    if (temp[0] == temp [1]):
        total += 3    
    if(temp[1] == 'A' and temp[0] == 'C'):
        total += 6
    if(temp[1] == 'B' and temp[0] == 'A'):
        total += 6 
    if(temp[1] == 'C' and temp[0] == 'B'):
        total += 6

print(total)

#part 2 

total = 0
for column in range(len(s)-1):
    temp = s[column].split(' ')
    if (temp[1] == 'X'):
        temp[1] = 'L' 
    if (temp[1] == 'Y'):
        temp[1] = 'D' 
        total += 3
    if (temp[1] == 'Z'):
        temp[1] = 'W' 
        total += 6
    if (temp[0] == temp [1]):
        total += 3    
    if(temp[1] == 'L' and temp[0] == 'C'):
        total += 2
    if(temp[1] == 'L' and temp[0] == 'B'):
        total += 1
    if(temp[1] == 'L' and temp[0] == 'A'):
        total += 3
    if(temp[1] == 'W' and temp[0] == 'A'):
        total += 2 
    if(temp[1] == 'W' and temp[0] == 'B'):
        total += 3 
    if(temp[1] == 'W' and temp[0] == 'C'):
        total += 1 
    if(temp[1] == 'D' and temp[0] == 'B'):
        total += 2
    if(temp[1] == 'D' and temp[0] == 'A'):
        total += 1
    if(temp[1] == 'D' and temp[0] == 'C'):
        total += 3
        
print(total)

#If it aint broke. Dont fix it