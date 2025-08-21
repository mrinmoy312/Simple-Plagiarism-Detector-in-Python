# Import SequenceMatcher from difflib module
from difflib import SequenceMatcher

# Open and read both text files
with open('doc1.txt') as first_file, open('doc2.txt') as second_file:
    file1 = first_file.read()
    file2 = second_file.read()

# Compare both text files
similarity_ratio = SequenceMatcher(None, file1, file2).ratio()

# Convert the decimal output to a percentage
result = int(similarity_ratio * 100)

# Display the final result
print(f"{result}% Plagiarized Content")
