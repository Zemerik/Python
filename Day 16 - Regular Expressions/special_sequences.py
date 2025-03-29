import re

# Word boundaries
text = "cat category catapult"
print("Whole words:", re.findall(r"\bcat\b", text))

# Digit matching
log = "Error 404: Not found"
error_code = re.search(r"\d+", log)
print("Error code:", error_code.group())

# Negative lookahead
print("Cat not followed by 'alog':", 
      re.findall(r"cat(?!alog)", "catalog cat"))