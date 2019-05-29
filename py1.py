import re

#x = "From: Using the : character 123 456"
#y = re.findall('^F.+:',x)

'''
This is code for Regular Expressions
You need to import re for using regular expresions
then you need to write a re for finding what you need
format is variable = re.findall('RE for what you want to find, THE data you want to search "')
'''


x= '''Writing programs (or programming) is a very creative
and rewarding activity.  You can write programs for
3036 many reasons, ranging from making your living to solving 7209
a difficult data analysis problem to'''

y = re.findall('[0-9]+\S',x)
print(y)
count = 0
for i in y:
    #print(i)
    j = int(i)
    print(j)
    count += j
print(count)
