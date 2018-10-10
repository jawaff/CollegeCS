'''
program: encryption and decryption
author:Jake Waffle

Encrypt and decrypt lower and uppercase alphabets
1. Constants
    none
2. Input
    filename
    distance
    filename2
    condition
    filename3
3. Computations
    Encrypting a message
    Decrypting a message
4. Display
    encrypted message
    decrypted message
'''
#Gather Input
filename = raw_input("Enter the filename of the file you wish to encrypt: ")
distance = input("How much do you want to shift the message by? ")
filename2= raw_input("Enter the filename of the file you wish to write to.\n(If the file doesn't exist it will be created in the directory of this py file): ")

#Open the file that is to be encrypted, then close it
f = open(filename,'r')
message = f.read()
f.close()

#initialize variable
eMessage = ""

#Encrypt message
for i in message: 
    ordVal = ord(i)
    cipherVal = ordVal + distance
    #Checking to see if newline char
    if ordVal == 10:
        #This char doesn't conform to the range of chars that I wanna deal with
        #So I'm not encrypting it
        cipherVal = 10;
    elif cipherVal > 126:
        cipherVal = 32 + distance - (126 - ordVal + 1)
    eMessage += chr(cipherVal)
    
#Print the altered message and write it to the corresponding file
print "This is your encrypted message:\n" + eMessage
f = open(filename2,'w')
f.write(eMessage)
f.close()

#Ask to decrypt current eMessage or to use another file
condition = raw_input("Would you like to decrypt and display the previous decrypted file?\n" + "(Enter y or n): ")

#If the user chooses to use another file to decrypt, then we need to ask for input, close the current file,
#open the new file with the new filenameand assign the contents to variable eMessage
if condition == 'n':
    filename3 = raw_input("Enter the filename of the file you wish to decrypt: ")
    f.close()
    f = open(filename3,'r')
    eMessage = f.read()
    
#Decrypt
dMessage = ""
for i in eMessage:
    ordVal = ord(i)
    cipherVal = ordVal - distance
    if ordVal == 10:
        cipherVal = 10
    elif cipherVal < 32:
        cipherVal = 126 - (distance - (ordVal - 32 + 1))
    dMessage += chr(cipherVal)
print "Your decrypted message is:\n" + dMessage
