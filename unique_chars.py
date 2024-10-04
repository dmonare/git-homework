def has_unique_chars(s):
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True


print(has_unique_chars("hello"))
print(has_unique_chars("zangi"))
print(has_unique_chars("level"))
