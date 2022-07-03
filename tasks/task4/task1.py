# Task-1 :-
# Question & Answer Sets ( 15th May,2022 )
# s = "this is My First Python programming class and i am learNING python string and its function"
# 1 . Try to extract data from index one to index 300 with a jump of 3
# 2. Try to reverse a string without using reverse function
# 3. Try to split a string after conversion of entire string in uppercase
# 4. try to convert the whole string into lower case
# 5 . Try to capitalize the whole string
# 6 . Write a diference between isalnum() and isalpha()
# 7. Try to give an example of expand tab
# 8 . Give an example of strip , lstrip and rstrip
# 9. Replace a string charecter by another charector by taking your own example
# "sudhanshu"

import custom_module.allfunc as a

s1 = a.stringz("a book or other written or printed work, regarded in terms of its content rather than its physical form.")
print(s1.s)
print(s1.extract(1,20))
print(s1.extract_jump(1,20,5))
print(s1.reverse())
print(s1.upp())
print(s1.loww())
print(s1.splitt(' '))
print(s1.stripp('s'))
print(s1.replacee("book", "car"))