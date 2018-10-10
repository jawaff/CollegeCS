"""
authors:Jacob Waffle, Carey Stirling
program: Lab 7, #7&8`

Write a negate and sepia conversion function for images
Constants
    There ARE NONE!
Input
    filename
    option
Compute
    sepia()
    inverse()
    blackAndWhite()
Display
    Display a list of the options possible
    The current image, converted or not converted

"""
from images import Image

def sepia(image):
    '''Converts image to a sepia version.'''
    for y in xrange(image.getHeight()):
        for x in xrange(image.getWidth()):
            (red,green,blue) = image.getPixel(x,y)
            if red < 63:
                red = int(red * 1.1)
                blue = int(blue * 0.9)
            elif red < 192:
                red = int(red * 1.15)
            else:
                red = min(int(red * 1.08), 255)
                blue = int(blue * 0.93)
            image.setPixel(x,y,(red,green,blue))

def inverse(image):
    '''Convert each individual picture to its OPPOSITE!'''
    for y in xrange(image.getHeight()):
        for x in xrange(image.getWidth()):
            (r,g,b) = image.getPixel(x,y)
            image.setPixel(x,y,(250-r,250-g,250-b))
   
def blackAndWhite(image):
    """Converts the argument image to black and white."""
    blackPixel = (0,0,0)
    whitePixel = (255,255,255)
    for y in xrange(image.getHeight()):
        for x in xrange(image.getWidth()):
            (r,g,b) = image.getPixel(x,y)
            average = (r + g +b) / 3
            if average < 128:
                image.setPixel(x,y, blackPixel)
            else:
                image.setPixel(x,y, whitePixel)

def computeOptions(option, image):
    '''Call the corresponding conversion function that the user specified.'''
    if option == 0:
        blackAndWhite(image)
    elif option == 1:
        inverse(image)
    elif option == 2:
        sepia(image)
                
def main():
    #Asking for an image to use for the conversions
    filename = raw_input("Enter the filename of a gif: ")
    image = Image(filename)
    img = image.clone()
    gewd = False
    while not gewd:
        #Printing and asking for options
        print"%-2d%s" % (0, "black and white conversion")
        print"%-2d%s" % (1, "inverse conversion")
        print"%-2d%s" % (2, "sepia conversion")
        print"%-2d%s" % (3, "reset image")
        print"%-2d%s" % (4, "load new image")
        print"%-2d%s" % (5, "quit")
        print "\n"
        option = raw_input("Enter an option: ")
        correctInput = False
        while correctInput == False:
            #If the option is a number between 0 and 3
            if not option.isalpha() and int(option) >= 0 and int(option) < 6:
                print "Thanks for coherent input bro!"
                correctInput = True
            else:
                option = raw_input("Enter a numerical option BETWEEN 0 and 5: ")
        option = int(option)
        if option != 5:
            #If the user has wished the image to be restored to its initial state
            if option == 3:
                #Cloning the original image and overwriting all previously done conversions
                img = image.clone()
            elif option == 4:
                filename = raw_input("Enter a filename of the image you wish to alter(gif please): ")
                image = Image(filename)
                img = image.clone()
            else:
                #Perform other tasks on the current image
                computeOptions(option, img)
            print "Close the image to continue!"
            img.draw()
        else:
            gewd = True
            print "\nHave a nice day!"

main()
