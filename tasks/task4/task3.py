# Q.1)
# ineuron
# ineuron ineuron
# ineuron ineuron ineuron
# ineuron ineuron ineuron ineuron
# q.2)
# .....*.....*ineuron.....*.....*
# .....*ineuron.....*ineuron.....*
# ineuron.....*ineuron.....*ineuron
# .....*ineuron.....*ineuron.....*
# .....*.....*ineuron.....*.....*
# l =[[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]),{'k1' : "sudh" , 'k2' :
# "ineuron", 'k3' : "kumar", 3:6, 7:8}, ["ineuron", "data science"]]
# q.3) Try to extract all the list entity.
# q.4) Try to extract all the dict entity.
# q.5) Try to extract all the Tuples entity.
# q.6) Try to extract all the Numeric data it may be a part of dict key and values.
# q.7) Try to give summation of all the numeric data.
# q.8) Try to filter out all the odd values out all numeric datawhich is a part of a list.
# q.9) Try to extract "ineuron" out of this dataset.
# q.10) Try to find out a number of occurance of all the data.
# q.11) Try to find out a number of keys in dict element.
# q.12) Try to filter out all the string data.
# q.13) Try to find out alphanum in data.
# q.14) Try to find out multiplication of all numeric value in the individual collection inside dataset.
# q.15) Try to unwrape all the collection inside collection and create a flat list.

import custom_module.allfunc as a

s = a.pattern("ineuron")
print(s.p1(10))
l = a.lisst([[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7), set([23, 4 , 5, 45, 4, 4, 5, 45, 45, 4, 5]),{'k1': "sudh", 'k2': "ineuron", 'k3' : "kumar", 3:6, 7:8}, ["ineuron", "data science"]])
print(l.onlylist())
print(l.onlydict())
print(l.onlytuple())
print(l.onlynumeric())
print(l.odds())
print(l.searchh("ineuron"))
print(l.occurance())
print(l.onlykeys())
print(l.onlystr())
print(l.onlyalnum())
print(l.mult())
print(l.unwrap())