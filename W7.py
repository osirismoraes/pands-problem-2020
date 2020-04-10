# Write a program that reads in a text file and outputs the number of e's it contains.


from collections import Counter

letter = 'e'
with open('moby-dick.txt') as f:
    occurrences = f.read().count(letter)
print(occurrences)

with open('moby-dick.txt') as f:
    occurrences = Counter(f.read())
print(occurrences)
print()