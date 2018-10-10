# Makefile for the Stack Project

# Define g++ as the compiler command
CC = g++

DOXYFILE = Doxyfile

# Define the options passed to the compiler
# the default standard for g++ compiling c++ code is -std=gnu++98
CC_OPT = -v -std=c++98 -Wall

# Define the files that should be included in this project when compiling
FILES = Main.cpp

# Define the executable file name as needed for this project
OUT_EXE = Main.bin

# Define the output file option and append the output filename
OPT_OUT_EXE = -o $(OUT_EXE)

doall: build builddocs

# This is the first and default target
# Define the build target as compiling and linking all 
#	files into the declared executable file
build: $(FILES)
	$(CC) $(CC_OPT) $(OPT_OUT_EXE) $(FILES)


# The clean target removes all the object files previously compiled
clean:
	rm --force --verbose *.o


# The cleanall target removes all the object and executable files previously created
cleanall:
	rm --force --verbose *.o
	rm --force --verbose *.exe


# Define a the target rebuild as clean and build
rebuild: clean build

builddocs: $(FILES) $(DOXYFILE)
	doxygen

