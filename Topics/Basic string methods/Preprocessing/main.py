raw = input()
clean = raw.replace(",", "").replace("!", "").replace(".", "").replace("?", "")
print(clean.lower())
