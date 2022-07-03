# l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" ,
# 234:[23,45,656]}]
# 1 . Try to reverse a list
# 2. try to access 234 out of this list
# 3 . try to access 456
# 4 . Try to extract only a list collection form list l
# 5 . Try to extract "sudh"
# 6 . Try to list all the key in dict element avaible in list
# 7 . Try to extract all the value element form dict available in list

import custom_module.allfunc as a

l = a.lisst([3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" ,
234:[23,45,656]}])

print(l.reversee())
print(l.searchh(456))
print(l.onlylist())
print(l.dicts('sudh'))
print(l.onlykeys())
print(l.onlyvalues())