with open('py.txt') as f:
  text = f.read().splitlines() # list of lines

lines = len(text) # length of the list = number of lines
words = sum(len(line.split()) for line in text) # split each line on spaces, sum up the lengths of the lists of words
characters = sum(len(line) for line in text) # sum up the length of each line

print(lines)
print(words)
print(characters)

