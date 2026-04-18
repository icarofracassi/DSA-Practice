text = input("Text: ")

text = text.lower()

letters = sum(c.isalpha() for c in text)
words = len(text.split())
sentences = sum(((c == '.') or (c =='!') or (c == '?')) for c in text)

L = (letters / words) * 100
S = (sentences / words) * 100

result = (0.0588 * L) - (0.296 * S) - 15.8
result = round(result)

if (result < 1):
    print("Before Grade 1")
elif (result >= 16):
    print("Grade 16+")
else:
    print("Grade", result)
