# Import SequenceMatcher from difflib module
from difflib import SequenceMatcher

# Declare string variables
string1 = 'I am geek'
string2 = 'I am geeks'

# Use the SequenceMatcher()
match = SequenceMatcher(None, string1, string2)

# Convert the output to a percentage
result = match.ratio() * 100

# Display the final result
print(int(result), "%")
