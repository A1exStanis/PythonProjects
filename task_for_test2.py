# You have a list of dictionaries where each dictionary contains information about a user.
# Your task is to create a function that filters users by age
# and counts the number of users in each age category.

users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 25},
    {"name": "Eve", "age": 40},
]


def count_users_by_age_category(users):
    age_categorise = {}
    for user in users:
        age = user['age']
        category_start = (age // 10) * 10
        category_end = category_start + 9
        category_name = f'{category_start}-{category_end}'

        if category_name in age_categorise:
            age_categorise[category_name] += 1
        else:
            age_categorise[category_name] = 1
    return age_categorise


# print(count_users_by_age_category(users))


# You need to implement a function that processes a list of strings,
# where each string is a list of words. Your task is to sort the words
# in each line alphabetically and return a list of lines
# where the words in each line are already sorted.


lines = [
    "banana apple cherry",
    "dog cat",
    "zebra lion tiger",
]


def sort_words_in_lines(lines):
    list_ = []
    for row in lines:
        row = row.split()
        row.sort()
        row = ' '.join(row)
        list_.append(row)
    return list_


# result = sort_words_in_lines(lines)
# print(result)


# You need to implement a function that replaces all occurrences of one character in
# a string with another character. Note that the replacement must be case sensitive.
#
# Incoming data:
#
# The text line in which you need to make a replacement.
# The old_char character to replace.
# The new_char character to replace with.


text = "Hello World"
old_char = "o"
new_char = "0"


def replace_character(text, old_char, new_char):
    if old_char in text:
        text = text.replace(old_char, new_char)
    return text


# result = replace_character(text, old_char, new_char)
# print(result)
