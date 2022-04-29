#int
#float
#str
#bool
#list
#dict
#tuples
#set

a=10
b=20
sum=a+b
print(sum)


c=1.2
d=20.3

name="sam"
designation="tester"

#this is snake casing
is_valid_user=True
is_valid_user=False

#in java we use camel casing ->boolean is_Valid_User=true

#variable names cannot have white spaces
#cant't use special characters
#good to have lowercase
#avoid using built in keywords->list,int,float
#variables names are case sensitive
#use snakecasing to define variable names
#python is indented language

def sum():
    a=10
    b=20
    print(a+b)

print("hello")#this is not part of def sum() becaus it is not indented

sum()


area=10
print(type(area))

area="10"
print(type(area))

area=True
print(type(area))

area=10.2
print(type(area))
#python is a dynamically typesd language where as java is statically typed language


#pgm to calculate tax
income=1000
tax_percentage=0.2
tax=income*tax_percentage
print(tax)


#strings have many methods ->string means ordered sequence of characters
name="sam"
first_name="smith"
#indexing and slicing
print(name[1])
print(name[2])
#print(name[3])

name="sam"#0 -2 -1  #012
first_name="smith" #01234  #-4 -3 -2 -1 0

print(first_name[-3])

#find length of string
print(len(first_name))
print(len(name))

#indexing 012   0-2-1

#slicing
str_alphabets="abcdefg"
print(str_alphabets[0:3])
print(str_alphabets[0:4])


#syntax for slicing string[start:stop]
print(str_alphabets[:4])
print(str_alphabets[1:4])
print(str_alphabets[2:])
print(str_alphabets[:7])

#string(start:stop:stop)
print(str_alphabets[0:7])
print(str_alphabets[0:7:3])
print(str_alphabets[0:7:1])
print(str_alphabets[0::-1])
print(str_alphabets[::-1])
print(str_alphabets[::1])
print(str_alphabets[-1])

#string is immutable
#to change tim to tom
name="tim"
name1=name[0]+"o"+name[-1]
print(name1)

#below code gives error
#name="tim"
#name[1]="o"

#or we can entirely change string
name="tim"
name="tom"
print(name)