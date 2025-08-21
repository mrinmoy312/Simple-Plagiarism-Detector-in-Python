from difflib import SequenceMatcher

with open('doc1.txt', 'r') as file1, open('doc2.txt', 'r') as file2:
    text1 = file1.read()
    text2 = file2.read()

similarity_ratio = SequenceMatcher(None, text1, text2).ratio()
result = int(similarity_ratio * 100)

print(f"{result}% Plagiarized Content")

