""" 
Random - For Randomize the chars for password.
Sys - For exit the program with error messages
GC - Garbage Collect, to delete the variable values from DRAM.
"""
import random
import sys
import gc

# Calling all dictionary. Putting number as keys to recursively use with a function
Chars ={
    1:"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+}{",
    2:"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
    3:"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+}{",
    4:"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    5:"0123456789",
}

""" 
[passwdGenerator - Going to generate a random password.]    
@param  {[int]} choose [Option choosen by user for selected chars]
@param  {[int]} passwd_lenght [Lenght of the password]
@return {[void]}   print   [Only print the password in CLI and after that will destroy every variable in memory.]
"""
def passwdGenerator(choose, passwd_lenght):
    passwd = ""
    for c in range(passwd_lenght):
        passwd += random.choice(Chars[choose])
    print(" --> Your password is: {} <--".format(passwd))
    gc.collect()

#   Check if user input the possible value. 
#   This should be a Natural Number, greater than zero.
#   To be warned, if the password lenght has 7 or less characters, the program will alert it.
passwd_lenght = int(input("Enter lenght: "))
if passwd_lenght <= 0: sys.exit("Lenght should be greater than zero.")
elif passwd_lenght <= 7: print("!!! ALERT - You should reconsider to use a long password (Recommended is lenghtier than 8 characters) !!!")

# Choose for password. The Code will check the dictionary and apply the function 'passwdGenerator'
choose = int(input("\t1. All Chars\n\t2. No Special Chars\n\t3. No Numbers\n\t4. Only Chars\n\t5. Only Numbers\nChoose 1-5: "))
if choose > 0 and choose < 6:
    passwdGenerator(choose, passwd_lenght) 
else: 
    sys.exit("!!! Wrong Parameter - Only Numbers from 1 to 5 !!!")