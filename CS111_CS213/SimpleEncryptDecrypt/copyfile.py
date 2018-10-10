'''
program:copyfile.py
authors:Jake Waffle, Greg McAtee, BreAnna Baird

copying one file's contents to another
1.Constants
    none
2.Input
    filename1
    filename2
3.Computation
    open each file, read the contents of the first and write the same string to the second file
4.Display
    none
'''
filename1 = raw_input("First filename")
filename2 = raw_input("Second filename")

f = open(filename1,'r')
contents = f.read()
f.close()

f = open(filename2,'w')
f.write(contents)
f.close()

    
