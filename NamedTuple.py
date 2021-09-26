# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple

n = int(input()) #takes input of how many objects will be inputed
c_name = input().split() #stores coloum names into a list

mark = namedtuple ("s_mark",c_name) #creates a named tuple that is called "s_mark", its values are taken from c_name
l = [int(mark._make(input().split()).MARKS) for i in range (n)] #creates a list called l. _make creates another namedtuple from mark. Then the MARKS are taken from the named tuple into l. There is a loop that goes through number of objects.

print (sum(l)/(len(l))) #adds up the values of l then divides by the length to get the average

