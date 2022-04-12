
"""
Introduction to Command Shell - coding
"""

"""
How does the shell compare to a desktop interface?
An operating system like Windows, Linux, or Mac OS is a special kind of program. It controls the computer's processor, hard drive, 
and network connection, but its most important job is to run other programs.

Since human beings aren't digital, they need an interface to interact with the operating system. The most common one these days 
is a graphical file explorer, which translates clicks and double-clicks into commands to open files and run programs. Before computers
 had graphical displays, though, people typed instructions into a program called a command-line shell. Each time a command is entered, 
 the shell runs some other programs, prints their output in human-readable form, and then displays a prompt to signal that it's ready 
 to accept the next command. (Its name comes from the notion that it's the "outer shell" of the computer.)

Typing commands instead of clicking and dragging may seem clumsy at first, but as you will see, once you start spelling out what you 
want the computer to do, you can combine old commands to create new ones and automate repetitive operations with just a few keystrokes.

What is the relationship between the graphical file explorer that most people use and the command-line shell?

A: They are both interfaces for issuing commands to the operating system.
"""

#-----------------------------------------------------------------------------------------------------------------#

# Printing Current Working Directory 
# "PWD" (Print Working Direct) - it prints the absolute path of your current working directory 

#-----------------------------------------------------------------------------------------------------------------#

# Listing contents of a path 
# "ls" (short for listing) - ls followed by a folder path, will list all the contents of said path 

#-----------------------------------------------------------------------------------------------------------------#

"""
Relative vs Absolute Paths

An absolute path is like a latitude and longitude: it has the same value no matter where you are. 
A relative path, on the other hand, specifies a location starting from where you are: it's like saying "20 kilometers north".

As examples:

If you are in the directory /home/repl, the relative path seasonal specifies the same directory as the absolute path /home/repl/seasonal.

If you are in the directory /home/repl/seasonal, the relative path winter.csv specifies the same file as the absolute 
path /home/repl/seasonal/winter.csv.

The shell decides if a path is absolute or relative by looking at its first character: If it begins with /, it is absolute. 
If it does not begin with /, it is relative.
"""
#-----------------------------------------------------------------------------------------------------------------#

# Changing Directory
# "cd" (change directory) followed by a path changes the current folder path the command line has you in to the new specified path 

#-----------------------------------------------------------------------------------------------------------------#

"""
Move up in Directory

The parent of a directory is the directory above it. For example, 
    /home is the parent of /home/repl, and /home/repl is the parent of /home/repl/seasonal. 

You can always give the absolute path of your parent directory to commands like cd and ls. 
More often, though, you will take advantage of the fact that the special path .. (two dots with no spaces) means 
"the directory above the one I'm currently in". 

If you are in /home/repl/seasonal, then cd .. moves you up to /home/repl.
 If you use cd .. once again, it puts you in /home. 
 One more cd .. puts you in the root directory /, which is the very top of the filesystem. 
 
 (Remember to put a space between cd and .. - it is a command and a path, not a single four-letter command.)

A single dot on its own, ., always means "the current directory", so ls on its own and ls . do the same thing, while cd . has no 
effect (because it moves you into the directory you're currently in).

One final special path is ~ (the tilde character), which means "your home directory", such as /home/repl. 
No matter where you are, ls ~ will always list the contents of your home directory, and cd ~ will always take you home.
"""

#-----------------------------------------------------------------------------------------------------------------#

"""
Copying Files

You will often want to copy files, move them into other directories to organize them, or rename them. 
One command to do this is cp, which is short for "copy". If original.txt is an existing file, then:

cp original.txt duplicate.txt

creates a copy of original.txt called duplicate.txt. If there already was a file called duplicate.txt, it is overwritten. 
If the last parameter to cp is an existing directory, then a command like:

cp seasonal/autumn.csv seasonal/winter.csv backup

copies all of the files into that directory.
"""

#-----------------------------------------------------------------------------------------------------------------#

"""
Moving Files 

While cp copies a file, mv moves it from one directory to another, just as if you had dragged it in a graphical file browser. 
It handles its parameters the same way as cp, so the command:

mv autumn.csv winter.csv ..

moves the files autumn.csv and winter.csv from the current working directory up one level to its 
parent directory (because .. always refers to the directory above your current location).

"""

#-----------------------------------------------------------------------------------------------------------------#

"""
Renaming Files 

mv can also be used to rename files. If you run:

mv course.txt old-course.txt

then the file course.txt in the current working directory is "moved" to the file old-course.txt. 
This is different from the way file browsers work, but is often handy.

One warning: just like cp, mv will overwrite existing files. If, for example, you already have a 
file called old-course.txt, then the command shown above will replace it with whatever is in course.txt.
"""
#-----------------------------------------------------------------------------------------------------------------#

"""
Delete Files 

We can copy files and move them around; to delete them, we use rm, which stands for "remove". 
As with cp and mv, you can give rm the names of as many files as you'd like, so:

rm thesis.txt backup/thesis-2017-08.txt

removes both thesis.txt and backup/thesis-2017-08.txt

rm does exactly what its name says, and it does it right away: unlike graphical file browsers, 
the shell doesn't have a trash can, so when you type the command above, your thesis is gone for good.
"""
#-----------------------------------------------------------------------------------------------------------------#

"""
Create & Delete Directories 

mv treats directories the same way it treats files: if you are in your home directory and run 
    mv seasonal by-season
for example, 
mv changes the name of the seasonal directory to by-season. 
However, rm works differently.

If you try to rm a directory, the shell prints an error message telling you it can't do that, primarily to stop you from accidentally 
deleting an entire directory full of work. 

Instead, you can use a separate command called rmdir. 
For added safety, it only works when the directory is empty, so you must delete the files in a directory before you delete the directory. 
(Experienced users can use the -r option to rm to get the same effect)
"""
#-----------------------------------------------------------------------------------------------------------------#

"""
Temp File Space 

You will often create intermediate files when analyzing data. 
Rather than storing them in your home directory, you can put them in /tmp, 
which is where people and programs often keep files they only need briefly. 

(Note that /tmp is immediately below the root directory /, not below your home directory.) 
"""
#-----------------------------------------------------------------------------------------------------------------#

"""
How can I view a file's contents?

Before you rename or delete files, you may want to have a look at their contents. 
The simplest way to do this is with cat, which just prints the contents of files onto the screen. 
(Its name is short for "concatenate", meaning "to link things together", since it will print all the 
files whose names you give it, one after the other.)

Example:  cat agarwal.txt
 
"""

#----------------------#

"""
View a file's contents piece by piece 

You can use cat to print large files and then scroll through the output, but it is usually more convenient to page the output. 
The original command for doing this was called more, but it has been superseded by a more powerful command called less. 
(This kind of naming is what passes for humor in the Unix world.) 

When you less a file, one page is displayed at a time; you can press spacebar to page down or type q to quit.

If you give less the names of several files, you can type :n (colon and a lower-case 'n') to move to the next file, 
:p to go back to the previous one, 
or :q to quit.

"""

#----------------------#

"""
Looking at the start of a file - top rows of data 

The first thing most data scientists do when given a new dataset to analyze is figure out what fields it contains 
and what values those fields have. If the dataset has been exported from a database or spreadsheet, it will often 
be stored as comma-separated values (CSV). A quick way to figure out what it contains is to look at the first few rows.

We can do this in the shell using a command called head. As its name suggests, it prints the first few lines of a 
file (where "a few" means 10), so the command:

    head seasonal/summer.csv

"""

#----------------------#

"""
Typing less code? Tab Completion!

One of the shell's power tools is tab completion. If you start typing the name of a file and then press the tab key, 
the shell will do its best to auto-complete the path. For example, if you type sea and press tab, it will fill in 
the directory name seasonal/ (with a trailing slash). If you then type a and tab, it will complete the path as seasonal/autumn.csv.

If the path is ambiguous, such as seasonal/s, pressing tab a second time will display a list of possibilities. 
Typing another character or two to make your path more specific and then pressing tab will fill in the rest of the name.
"""

#----------------------#

"""
Controlling what Commands do

You won't always want to look at the first 10 lines of a file, so the shell lets you change head's behavior by giving it a 
command-line flag (or just "flag" for short). If you run the command:
    
    head -n 3 seasonal/summer.csv 
    
head will only display the first three lines of the file. 
If you run head -n 100, it will display the first 100 (assuming there are that many), and so on.

A flag's name usually indicates its purpose (for example, -n is meant to signal "number of lines").
 Command flags don't have to be a - followed by a single letter, but it's a widely-used convention.

Note: it's considered good style to put all flags before any filenames    
"""

#----------------------#

"""
Listing Everything below a Directory

In order to see everything underneath a directory, no matter how deeply nested it is, you can give ls the flag -R (which means "recursive").
This shows every file and directory in the current level, then everything in each sub-directory, and so on.

To help you know what is what, ls has another flag -F that prints a / after the name of every directory 
and a * after the name of every runnable program. 

"""

#----------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------#

"""
Getting Help for Commands

To find out what commands do, people used to use the man command (short for "manual").
For example:
                man head 
would bring up all the info on command "head"

man automatically invokes less, so you may need to press spacebar to page through the information and :q to quit.

The one-line description under NAME tells you briefly what the command does, and the summary under SYNOPSIS lists 
all the flags it understands. 

Anything that is optional is shown in square brackets [...], 
either/or alternatives are separated by |, 
and things that can be repeated are shown by ..., 

"""
#----------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------#

"""
Selecting Columns from a file 

head and tail let you select rows from a text file. 
If you want to select columns, you can use the command cut. 

It has several options (use man cut to explore them), but the most common is something like:

    cut -f 2-5,8 -d , values.csv
    
which means "select columns 2 through 5 and columns 8, using comma as the separator". 
cut uses -f (meaning "fields") to specify columns and -d (meaning "delimiter") to specify the separator. 
You need to specify the latter because some files may use spaces, tabs, or colons to separate columns.

NOTE - cut is a simple-minded command. In particular, it doesn't understand quoted strings

The SEE ALSO section of the manual page for cut refers to a command called "paste"
that can be used to combine data files instead of cutting them up
"""
#----------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------#

"""
Repeating Commands 

One of the biggest advantages of using the shell is that it makes it easy for you to do things over again. 
If you run some commands, you can then press the up-arrow key to cycle back through them. You can also use the left 
and right arrow keys and the delete key to edit them. Pressing return will then run the modified command.

Even better, history will print a list of commands you have run recently. Each one is preceded by a serial number to 
make it easy to re-run particular commands: just type !55 to re-run the 55th command in your history (if you have that many). 
You can also re-run a command by typing an exclamation mark followed by the command's name, such as !head or !cut, which will 
re-run the most recent use of that command.
"""
#----------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------#

"""
Selecting Lines with specific values

head and tail select rows, cut selects columns, and grep selects lines according to what they contain. 
In its simplest form, grep takes a piece of text followed by one or more filenames and prints all of the lines 
in those files that contain that text. 

For example, grep bicuspid seasonal/winter.csv prints lines from winter.csv that contain "bicuspid".

grep can search for patterns as well. 
What's more important right now is some of grep's more common flags:

-c: print a count of matching lines rather than the lines themselves
-h: do not print the names of files when searching multiple files
-i: ignore case (e.g., treat "Regression" and "regression" as matches)
-l: print the names of files that contain matches, not the matches
-n: print line numbers for matching lines
-v: invert the match, i.e., only show lines that don't match
"""
#----------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------#
