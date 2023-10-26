some_words = ["nightmare", "unforgiven", "wreckage"]

# some_words is a list of values
# In this case, those values are all strings
# We call each value in a list an "element"
# But lists can contain any type of value:

mixed_list = ["mercy", 45, True, ["another", "list"]]

# mixed_list shows that each element can be of any type.
# Lists are ordered, each element has a position and keeps that position unless we modify the list
# We can access a value at any position using square bracket syntax and an index number:

print(mixed_list[0])  # prints the first value in mixed_list which is "mercy"
print(mixed_list[1])  # prints the second value in mixed_list which is 45
print(mixed_list[2])  # prints the third value in mixed_list which is True
print(mixed_list[3])  # prints the forth value in mixed_list which is another list that is nested in mixed_list

# Note that lists start at index 0, not 1

# When we access an element in a list using square brackets, we can treat it as if we have the element in a variable.
# For example mixed_list[0] is a string, so we can treat it like one by using a string method on it

print(mixed_list[0].capitalize())

# Lists are iterable, which means we can iterate or 'loop' through them:

for my_element in some_words:
    print(my_element.capitalize())

# 'my_element' is the variable name I have given to each element in the list in an iteration
# The indented code will execute for each element in the list