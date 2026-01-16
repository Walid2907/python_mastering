# name = input("entre your full name :")
# #len is a function that calculate a string lenght
# lenght = len(name)
# print(lenght)
# #find is a method that returns the index of the first apperance of the giving caracter and it returns -1 if it didn't find nothing
# result = name.find(" ")
# print(result)
# #rfind is a method that returns the index of the last apperance of the giving caracter and it returns -1 if it didn't find nothing
# result2 = name.rfind("r")
# print(result2)
# #capitalize is capitalize the firt character in the string
# name = name.capitalize()
# print(name)
# #upper capitalize the whole string
# name = name.upper()
# print(name)
# #lower lowercase the whole string 
# name = name.lower()
# print(name)
# #isdigit it check if the giving string is digit
# result3 = name.isdigit()
# print(result3)
# #is alpha check if all the strings caracter is digit 
# #count count how many characters are in a string
# name = name.count("a")
# print(name)
# #replace is takes 2 arg what u want to replace and the new character
# name = str(name)
# name = "walid kerdad"
# name = name.replace("a", "o")
# print(name)
#exercice
username = input("entre a username :")
lenght = len(username)
spaces = username.find(" ")
alpha = username.isalpha()
if lenght > 12 or spaces != -1 or alpha == False : 
    print("invalid user")
else:
    print("valid")
#can be devlopped if needed but it's dump to do

#indexing operator [start : end : step]
print(username[0]) #1st character
print(username[3:]) #from 3rd character till last
print(username[::-1]) # which will reverse the str
#etc