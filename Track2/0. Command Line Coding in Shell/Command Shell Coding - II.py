
"""
Command Shell Coding - Part II
"""

#--------------------------------------------------------------------------------------------------------------------------#
"""
How can i store a command's output in a file?

All of the tools you have seen so far let you name input files. 
Most don't have an option for naming an output file because they don't need one. 
Instead, you can use redirection to save any command's output anywhere you want. 
If you run this command:
    
    head -n 5 seasonal/summer.csv
    
it prints the first 5 lines of the summer data on the screen.

If you run this command instead:

    head -n 5 seasonal/summer.csv > top.csv
    
nothing appears on the screen. Instead, head's output is put in a new file called top.csv
    
The greater-than sign > tells the shell to redirect head's output to a file. 
It isn't part of the head command; instead, it works with every shell command that produces output.
"""

#--------------------------------------------------------------------------------------------------------------------------#

"""
Using a command's output as input

Suppose you want to get lines from the middle of a file. 
More specifically, suppose you want to get lines 3-5 from one of our data files. 
You can start by using head to get the first 5 lines and redirect that to a file, and then use tail to select the last 3:

    head -n 5 seasonal/winter.csv > top.csv
    tail -n 3 top.csv

"""
#--------------------------------------------------------------------------------------------------------------------------#

"""
Better way to combine commands

Using redirection to combine commands has two drawbacks:

It leaves a lot of intermediate files lying around (like top.csv).
The commands to produce your final result are scattered across several lines of history.
The shell provides another tool that solves both of these problems at once called a pipe. 

Example:
        head -n 5 seasonal/summer.csv | tail -n 3
        
The pipe symbol tells the shell to use the output of the command on the left as the input to the command on the right.


Combining MANY commands - through chaining 

You can chain any number of commands together. For example, this command:
    
    cut -d , -f 1 seasonal/spring.csv | grep -v Date | head -n 10
    
will:

select the first column from the spring data;
remove the header line containing the word "Date"; and
select the first 10 lines of actual data.
"""
#--------------------------------------------------------------------------------------------------------------------------#

"""
Counting records in a file 

command "wc" (short for word count) prints number of characters, words, and lines in a file. 
You can make it print only one of these using -c, -w, or -l respectively.

"""
#--------------------------------------------------------------------------------------------------------------------------#

"""
Specifying many files at once 

Most shell commands will work on multiple files if you give them multiple filenames. 
For example, you can get the first column from all of the seasonal data files at once like this:

cut -d , -f 1 seasonal/winter.csv seasonal/spring.csv seasonal/summer.csv seasonal/autumn.csv

But typing the names of many files over and over is a bad idea: it wastes time, and sooner or later 
you will either leave a file out or repeat a file's name. To make your life better, the shell allows you 
to use wildcards to specify a list of files with a single expression. The most common wildcard is *, 
which means "match zero or more characters". 
Using it, we can shorten the cut command above to this:

    cut -d , -f 1 seasonal/*
or
    cut -d , -f 1 seasonal/*.csv
    
NB - the wildcard can be engaged after characters, so say we only wanted spring & summer, we could do:
        cut -d , -f 1 seasonal/s*.csv
"""
#--------------------------------------------------------------------------------------------------------------------------#

"""
Other wildcards the shell can use

? matches a single char, so 201?.txt would match 2017.txt & 2018.txt but NOT 2017-01.txt

[...] matches any one of the chars inside the square brackets, so:
    201[78].txt would match 2017.txt & 2018.txt but NOT 2016.txt 
    
{...} matches any comma separated patterns inside the curly brackets, so:
    {*.txt, *.csv} matches any file whose name ends in .txt or .csv, but NOT .pdf for example
"""
#--------------------------------------------------------------------------------------------------------------------------#

"""
Sorting lines of text 

As its name suggests, sort puts data in order. By default it does this in ascending alphabetical order, but the flags 
    -n and -r can be used to sort numerically and reverse the order of its output, while 
    -b tells it to ignore leading blanks and 
    -f tells it to fold case (i.e., be case-insensitive). 
    
Pipelines often use grep to get rid of unwanted records and then sort to put the remaining records in order.
"""
#--------------------------------------------------------------------------------------------------------------------------#

"""
Removing duplicate lines 

Another command that is often used with sort is uniq, whose job is to remove duplicated lines. 
More specifically, it removes adjacent duplicated lines. If a file contains:
    2017-07-03
    2017-07-03
    2017-08-03
    2017-08-03
    
then "uniq" will produce:
    2017-07-03
    2017-08-03
    
HOWEVER 
    if the original file was:
        2017-07-03
        2017-08-03
        2017-07-03
        2017-08-03        

"uniq" would still print all 4 lines. The reason is that uniq is built to work with very large files. 
In order to remove non-adjacent lines from a file, it would have to keep the whole file in memory 
(or at least, all the unique lines seen so far). By only removing adjacent duplicates, it only has to keep 
the most recent unique line in memory

Example code:
       cut -d , -f 2 seasonal/winter.csv | grep -v Tooth | sort | uniq -c 
       
would collect all teeth data (column 2 from file)
remove any lines with "Tooth" through an invert (so clears heading) 
sorts the column alphabetically 
Takes a unique list of each data point & uses option -c to create a count alongside each one (like a group by in SAS)

"""

#--------------------------------------------------------------------------------------------------------------------------#

"""
Saving the output of a pipe 

The shell lets us redirect the output of a sequence of piped commands:
    
    cut -d , -f 2 seasonal/*.csv | grep -v Tooth > teeth-only.txt

However, > must appear at the end of the pipeline
"""
#--------------------------------------------------------------------------------------------------------------------------#

"""
How can i stop running a program?

type Ctrl + c  to end.  (often written ^C in Unix doc ~ note the c can be lower or upper case)
"""
