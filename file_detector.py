from difflib import SequenceMatcher

string1 = 'I am geek'
string2 = 'I am geeks'

# Create SequenceMatcher object
match = SequenceMatcher(None, string1, string2)

# Calculate similarity ratio
result = match.ratio() * 100

print(int(result), "%")
