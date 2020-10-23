'''
Question------------------------------------------------------------------
The program will recieve 3 English words inputs from STDIN

These three words will be read one at a time, in three separate line
The first word should be changed like all vowels should be replaced by *
The second word should be changed like all consonants should be replaced by @
The third word should be changed like all char should be converted to upper case
Then concatenate the three words and print them
Other than these concatenated word, no other characters/string should or message should be written to STDOUT

For example if you print how are you then output should be h*wa@eYOU.

You can assume that input of each word will not exceed more than 5 chars
Case 1
Input

-how
-are
-you

Expected Output : h*wa@eYOU
'''
#Code----------------------------------------------------------------------
import re
s1 = raw_input()
s2 = raw_input()
s3 = raw_input()
a = re.sub("[aeiouAEIOU]","*",s1)
b = re.sub("[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]","@",s2)
c = s3.upper()
d =[]
d.append(re.sub(" \r","",a))
d.append(re.sub("\r","",b))
d.append(re.sub("\r","",c))
var3 = "".join(d)
print var3

