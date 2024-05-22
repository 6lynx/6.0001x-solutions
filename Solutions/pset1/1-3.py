longest_substring = ''
current_substring = s[0]

for i in range(1, len(s)):
    if s[i] >= s[i-1]:
        current_substring += s[i]
    else:
        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring
        current_substring = s[i]

if len(current_substring) > len(longest_substring):
    longest_substring = current_substring

print("Longest substring in alphabetical order is:", longest_substring)