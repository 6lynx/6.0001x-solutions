vowels = ['a','e','i','o','u']
count = 0

for letter in s:
    if letter in vowels:
        count = count + 1
 
print("Number of vowels: ", count)