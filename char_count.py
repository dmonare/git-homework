def char_count(s):
    count_dict = {}
    for char in s:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict


print(char_count("level"))
print(char_count("dito"))