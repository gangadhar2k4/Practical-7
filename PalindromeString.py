file=open("palindromestring.txt",'w')
str=input("Enter String: ")
file.write("Enter String:")
file.write(str)
file.write('\n')
Temp=str[::-1]
if str==Temp:
    file.write("Given string is palindrome")
else:
    file.write("Given string is not a palindrome")
