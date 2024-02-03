import re

# 1. Matching patterns
pattern = r"\d{3}-\d{2}-\d{4}"
text = "Social Security Number: 123-45-6789"

match = re.search(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match found")

# 2. Finding all matches
emails = "alice@example.com, bob@gmail.com, charlie@yahoo.com"
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

all_matches = re.findall(email_pattern, emails)
print("All email addresses:", all_matches)

# 3. Splitting based on a pattern
sentence = "This is a sample sentence, split by spaces."
words = re.split(r"\s+", sentence)
print("Words in the sentence:", words)

# 4. Substituting patterns
phone_numbers = "Contact us at 123-456-7890 or 987-654-3210"
masked_numbers = re.sub(r"\d{3}-\d{3}-\d{4}", "XXX-XXX-XXXX", phone_numbers)
print("Masked phone numbers:", masked_numbers)

# 5. Grouping and extracting
date_string = "Date: 2023-01-01"
date_pattern = r"Date: (\d{4}-\d{2}-\d{2})"

date_match = re.search(date_pattern, date_string)
if date_match:
    print("Extracted date:", date_match.group(1))

# Note: Regular expressions are a powerful tool, and this example covers only a small portion of their functionality. You can explore more complex patterns and use cases in the documentation.
