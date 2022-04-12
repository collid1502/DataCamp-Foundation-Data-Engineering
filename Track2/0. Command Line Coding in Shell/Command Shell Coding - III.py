
"""
Command Shell Coding - Part III
"""

#-----------------------------------------------------------------------------------------------------#

"""
How does the shell store information?

Like other programs, the shell stores information in variables. Some of these, called environment variables, are available all the time. 
Environment variables' names are conventionally written in upper case, and a few of the more commonly-used ones are shown below.

 Variable       Purpose                        Value (example)
----------     ---------                      --------

HOME          Users home directory             /home/repl
PWD          Present Working Directory         same as "pwd" command
SHELL        which shell program being used    /bin/bash
USER         User's ID                         repl 

to get a complete list (which is quite long) you can type "set" in the shell.

"""

#-----------------------------------------------------------------------------------------------------#

"""
Printing a variables value 

echo hello DataCamp! will print: hello DataCamp!

to get the variable value, of say USER, we would need to use a $ as well:
    
    echo $USER 
    
    echo $OSTYPE   - prints operating system type you are using
"""

#-----------------------------------------------------------------------------------------------------#

"""
How else can the shell store information?

The other kind of variable is called a shell variable, which is like a local variable in a programming language.

To create a shell variable, you simply assign a value to a name:
    
    training=seasonal/summer.csv 
    
    echo $training   prints:    seasonal/summer.csv 
"""
#-----------------------------------------------------------------------------------------------------#

"""
How can i repeat a command many times?

Shell variables are also used in loops, which repeat commands many times. 
If we run this command:

        for filetype in gif jpg png; do echo $filetype; done
        
it produces:
    gif
    jpg
    png
    
Notes on the Loop:
    
1) The structure is for …variable… in …list… ; do …body… ; done
2) The list of things the loop is to process (in our case, the words gif, jpg, and png).
3) The variable that keeps track of which thing the loop is currently processing (in our case, filetype).
4) The body of the loop that does the processing (in our case, echo $filetype).
    
Notice that the body uses $filetype to get the variable's value instead of just filetype, just like it does with any other shell variable.
Also notice where the semi-colons go: 
    the first one comes between the list and the keyword do, and 
    the second comes between the body and the keyword done

"""

#-----------------------------------------------------------------------------------------------------#

"""
Repeat a command once for each file 

You can always type in the names of the files you want to process when writing the loop, but it's usually better to use wildcards. 
Try running this loop in the console:

    for filename in seasonal/*.csv; do echo $filename; done
    
it prints:
    
seasonal/autumn.csv
seasonal/spring.csv
seasonal/summer.csv
seasonal/winter.csv    

because the shell expands seasonal/*.csv to be a list of filenames before it runs the loop
"""

#-----------------------------------------------------------------------------------------------------#

"""
record the names of a set of files 

People often set a variable using a wildcard expression to record a list of filenames. For example, 
if you define datasets like this:

    datasets=seasonal/*.csv 
    
you can display the files names later using:
    
    for filename in $datasets; do echo $filename; done;
    
This saves typing and makes errors less likely.
"""

#-----------------------------------------------------------------------------------------------------#

"""
Run multiple commands in a single loop

printing filenames is useful for debugging, but the real purpose of loops is to do things with multiple files.
This loop prints the second line of each data file:
    
    for file in seasonal/*.csv; do head -n 2 $file | tail -n 1; done
    
it has the same structure as the other loops you have already seen; all thats different is that the body is a pipeline
of two commands instead of a single command.
"""
#-----------------------------------------------------------------------------------------------------#

"""
How can i edit file?


Unix has a bewildering variety of text editors. For this course, we will use a simple one called Nano. If you type nano filename, 
it will open filename for editing (or create it if it doesn't already exist). You can move around with the arrow keys, delete 
characters using backspace, and do other operations with control-key combinations:
    
    Ctrl + K: delete a line.
    Ctrl + U: un-delete a line.
    Ctrl + O: save the file ('O' stands for 'output'). You will also need to press Enter to confirm the filename!
    Ctrl + X: exit the editor.   


"""
#-----------------------------------------------------------------------------------------------------#

"""
How can i record what i just did?

when you are doing a complex analysis, you will often want to keep a record of the commands you used. 
You can do this with the tools you have already seen:
    
1) Run "history"
2) Pipe its output to tail -n 10 (or however many recent steps you want to save)
3) redirect that to a file called something like "figure-5.history"
    
This is better than writing things down in a lab notebook because it is guaranteed not to miss any steps.
It also illustrates the central idea of the shell:
    simple tools that produce and consume lines of text can be combined in a wide variety of ways to solve a broad range of problems
    
"""
#-----------------------------------------------------------------------------------------------------#

"""
How can i save commands to re-run later?

You have been using the shell interactively so far. But since the commands you type in are just text, you can store them in files 
for the shell to run over and over again. To start exploring this powerful capability, put the following command in a file called 
headers.sh:
    
    head -n 1 seasonal/*.csv 
    
this command selects the first row from each of the csv files in the seasonal directory. Once you have created this file, you can run 
it by tying:
    bash headers.sh
    
this tells the shell (which is just a program called bash) to run the commands contained in the file headers.sh which 
produces the same output as running the commands directly.
"""
#-----------------------------------------------------------------------------------------------------#

"""
How can i re-use pipes?

a file full of shell commands is called a "shell script" or soemtimes just a "script" for short.
Scripts dont have to have names ending in .sh, but can be a handy convention to keep track.

scripts can also contain pipes. 
For example, if all-dates.sh contains this line:
    
    cut -d , -f 1 seasonal/*.csv | grep -v Date | sort | uniq 
    
then:
    bash all-dates.sh > dates.out 
    
will extract the uniqe dates from all seasonal data files and save them in dates.out 
"""
#-----------------------------------------------------------------------------------------------------#

"""
How can i pass filenames to scripts?

A script that processes specific files is useful as a record of what you did, but one that allows you to process 
any files you want is more useful. To support this, you can use the special expression 
        $@ (dollar sign immediately followed by at-sign) to mean "all of the command-line parameters given to the script".
        
for example, if "unique-lines.sh" contains sort $@ | uniq , when you run:
    
    bash unique-lines.sh seasonal/summer.csv 
    
the shell replaces $@ with seasonal/summer.csv and processes one file.
if you run:
    
    bash unique-lines.sh seasonal/summer.csv seasonal/autumn.csv 
    
it processes two data files, and so on.

NB ~ As a reminder, to save what you have written in Nano, type Ctrl + O to write the file out, then Enter to confirm the filename, 
    then Ctrl + X to exit the editor.
"""

#-----------------------------------------------------------------------------------------------------#

"""
How can i process a single argument?

As well as $@, the shell lets you use $1, $2, and so on to refer to specific command-line parameters. 
You can use this to write commands that feel simpler or more natural than the shell's. 
For example, you can create a script called column.sh that selects a single column from a CSV file when 
the user provides the filename as the first parameter and the column as the second:

    cut -d , -f $2 $1
    
run it using:
    bash columns.sh seasonal/autumn.csv 1 
    
NB - notice how the script use the two parameters in reverse order.

"""
#-----------------------------------------------------------------------------------------------------#

"""
How can i write loops in a shell script?

Shell scripts can also contain loops. You can write them using semi-colons, or split them across lines without semi-colons to
make them more readable:

    # Print the first and last data records of each file.
    for filename in $@
    do
        head -n 2 $filename | tail -n 1
        tail -n 1 $filename
    done

(You don't have to indent the commands inside the loop, but doing so makes things clearer.)

The first line of this script is a comment to tell readers what the script does. 
Comments start with the # character and run to the end of the line. 
Your future self will thank you for adding brief explanations like the one shown here to every script you write.
"""

