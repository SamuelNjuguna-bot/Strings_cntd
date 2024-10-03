#Sep 25/2024
#The below program check if a String is a palindrome or symmetrical
from list import keylist, uniqueval

is_symmetrical = 'Kenya'
is_symmetrical2 = 'Mum'
S1 = is_symmetrical.lower()
S2 = is_symmetrical2.lower()
if S1[::-1] == S1:
    print("True")
else:
    print("False")

if S2[::-1] ==  S2:
    print("true")
else:
    print("false")

# Ways to remove the i'th character from a String
stringExample = "String"
ith = "S"
indx = stringExample.index(ith)
print(stringExample.replace(stringExample[indx], ' '))
#finding String Length in python
length = "Length"
print(len(length))
#Avoiding Spaces in String
example = "list example"
splited = example.strip(' ').replace(' ', '')
print(splited)
#Program to print even length words in a String
def even(ListtL):
    even_list = []
    print(listL)
    x = ''
    for item in listL:
         x = item[:2]
         even_list.append(x)
    return even_list
even_length_string = 'This is a python script'
listL = list(even_length_string.split(' '))
print(str(even(ListtL=listL)).strip(']['))
#26 sep/2024
#This program Uppercases the latter half of the String
List_uppercase = "Encyclopedia"
length = int(len(List_uppercase)/2)*-1
ln = length * -1
List_uppercase = List_uppercase[:ln] + List_uppercase[length:].upper()
print(List_uppercase)
#This program capitalises the first word and the last word in a String
String_example = 'thisIsCapital'
first = String_example[0].upper()
last = String_example[-1].upper()
String_example=String_example.replace(String_example[0], first)
String_example = String_example.replace(String_example[-1], last)
print(String_example)
#This program checks if a string contains
stringNum = "Ilove254"
flag = False
flag_d = False
for i in stringNum:
    if i.isalpha():
        flag = True
    if i.isdigit():
        flag_d = True

if flag and flag_d:
    print("True")
else:
    print("False")
#This programs accepts a string if it contains a vowel in it
def vowel(vowels_tests):
    vowels = list('aeiou')
    changed = list(vowels_tests)
    iS = [i for i in vowels if i in vowels_tests]
    if vowels == iS:
        print("accepted")
    else:
        print("Not accepted")

vowel(vowels_tests='abracadabraiou')
#This program prints matching characters in two strings
St1 = list("onehundre42di")
St2 = list("2")
new = [i for i in St1 if i in St2]
print(new)
#Oct 2/2024
#The Program counts no of vowels in a String
numString = 'ilovepythonlanguange'
vowels = 'aeiou'
num = list(numString)
count = 0
for i in numString:
    if i in vowels:
        count +=1
print(count)
#The program removes duplicates in a String
duplicated_string =  'abracabradabra'
duplicated_string = list(duplicated_string)
empty = []
for i in duplicated_string:
    if i not in empty:
        empty.append(i)
empty = str(empty)
empty = empty.strip('][')
print(empty)
#The program prints the least occurrent alpahabet in a string
from collections import Counter
Str = 'abracabradabra'
res = Counter(Str)
res = min(res, key = res.get)
print(res)
#maximum character frequency in a String
Str = 'abracabradabra'
Cnt = Counter(Str)
print(max(Cnt, key=Cnt.get))
#This program prints the frequency of certain characters in a string
exampl_e = 'donotrepeatyourself'
cert_char = ['o', 'u', 't']
coun = 0
empty = ''
for item in exampl_e:
    if item == 'o' or item == 'u' or item == 't':
        empty += item
print(Counter(empty))
#Oct 3/2024
#The below program checks if a String contains any special character
e_xample = 'samuelnjuguna@students.dkut.ac.ke?'
special_characters = "!@#$%^&*()-_=+{}[]|:;<>,.?/~`"
special_characters = list(special_characters)
example = list(e_xample)
res = [i for i in example if i in special_characters]
if res:
    print("Special Characters Present")
else:
    print("Special Characters not present")

#This Program generates random Strings
import random
import string
source = string.ascii_lowercase
random_generator = ''
for i in range(10):
   random_generator += random.choice(source)
print(random_generator)
#This program finds word greater than length K
words = 'while I was in campus I coded with python and java languages'
splited_words = words.split(' ')
k = 5
for word in splited_words:
    if len(word) > k:
        print(word)
#This program removes the i'th character from a string
# Removes character at index i
def remove(string, i):
    for j in range(len(string)):
        if j == i:
            string = string.replace(string[i], "", 1)
    return string
string = "helloguys"
i = 5
print(remove(string, i))
#This program splits and joins a string
the_string = 'if coding was horses everyone would ride on it'
the_string = the_string.strip('][').split(' ')
print(f'the splited string is {the_string}')
the_string = ''.join(the_string)
print(f'joined string is {the_string}')
