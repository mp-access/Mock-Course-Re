In this task, you take your first steps in working with source code, and you learn how to use ACCESS.

### Find your way around ACCESS

Have a look around:

 - At the top left, you navigate to different assignments and tasks
 - On the left, below these instructions you can see the file tree, showing all the files contained in this task
 - On the right, you can see your score, how many attempts you have left, and the history of all your coding activity
 - In the middle, you can see the files you've opened. Only some of the files can be edited.
 - At the top right, you have three buttons "Test", "Run" and "Submit". Don't click them just yet.
 - At the bottom, you have three tabs which corresponds to the buttons at the top right.

To solve assignments in ACCESS, you generally

 1. Read the instructions carefully. For the most part, the instructions contain everything you need to know to solve a task correctly.
 2. Open and edit the files as required in the instructions to implement your solution
 3. Click the "Run" button and observe the output from your script at the bottom in the "Run" tab
 4. Click the "Test" button to run the provided tests. Note that these are very minimal and do not generally determine whether your solution is correct. You will learn how to write your own tests so that you can take advantage of this feature in the future.
 5. Submit your solution by clicking "Submit". It will automatically be graded, and you will receive feedback on how much of your solution is correct and what may be remaining issues with it.
 6. Check the solution hint by looking at the history on the right side. Modify your solution if necessary, re-run, re-test, and re-submit.

You only have a limited number of submission attempts. However, after a set period of time (typically 1 day), you will receive a refill on your attempts. So if you run out, try coming back the next day to continue working on the assignment!

### Hello, World!

Traditionally, the first program learned is "Hello, World!". All it does is _print_ these two words to the command line. "Printing", in the context of programming, has little to do with printers and just means outputting some text on the screen.

Have a look at the file `task/script.py`. It contains one line of code (starting with `print...`) and some comments (starting with `#`).

Select the `script.py` file and press the "Run" button to execute the code. At the bottom, in the "Run" tab, you should see the output the script produces. You can also press the "Test" button to execute the included test suite, which simply checks if your script contains any errors that would make it impossible to execute. Don't worry about the contents of the test suite, yet. Again, you should now see the test output in the "Test" tab, indicating that it passes.

Now, modify the print statement so that your program will output "Hello, World!". Don't forget to first Run and Test your solution before finally submitting it by pressing "Submit".

**Important**: Besides submitting this particular exercise online, you should also download it and attempt to run the code offline on your own machine, as outlined below.

### Downloading the exercise

Click the "⤓" button at the top right of the file tree below and unpack the exercise somewhere or your machine.

### Opening the CLI

For the following steps you will now utilize a Command-Line Interface (CLI), a tool which allows you to interact with your computer in the form of text, rather than a graphical user interface (GUI).

Mainstream Operative Systems (OS), such as Windows, MacOS and Linux, all come with a CLI. Windows comes with "Command Prompt" (cmd) and "PowerShell", and in both MacOS and Linux there's a "Terminal". Note that on Windows, you can also install "Ubuntu" from the app store, which is a Linux-environment inside your Windows installation. In there, you can use a Linux terminal.

Now, from your app library or start menu, find and open the CLI application that ships with your OS.

When you launch the CLI, it might print a few lines, leaving you with at least one line at the end, which might look something like this on Windows:
```shell
C:\Users\John>
```
or like this on MacOS or Linux:
```shell
Johns-Computer:~ john$
```
This is called the **prompt**. At the end of the prompt is the cursor, where you can start typing commands that get interpreted and executed by the CLI. Try hitting <Enter> on your keyboard without entering anything else; you will see that the CLI just prints another prompt. Try typing `hostname` and hitting enter. This should work on all platforms and print the name of your computer. If you enter a command that the CLI doesn't recognize, you will receive an error message.

Note that when working with the CLI, you will be executing your commands at some specific location in your file system. This is called the "current working directory" or "cwd". When launching the CLI, your cwd will typically be your home folder. To see your cwd, you can use these commands (press enter to execute a command):

 - On MacOS/Linux: `pwd` which stands for 'print working directory'
 - On Windows: `cd` in cmd or `pwd` in PowerShell

As you can see, the current working directory is printed as a sequence of directory names, separated by `\` on Windows, and `/` on MacOS and Linux. In this case, you will see an _absolute_ path, meaning that it shows the entire path from the root directory (something like `C:\` on Windows or simply `/` on MacOS and Linux) to your current directory location.

If you want to view the content in the current working directory, use these commands:

 - On MacOS/Linux: `ls`
 - On Windows: `dir`

This will print the list of files and folders in your cwd.

### Navigating the filesystem

One thing you need to be able to do for this exercise is navigating the filesystem, or in other words, moving between directories on your computer, just like you would in your file manager, explorer or finder.

To change your current working directory to somewhere else, you use the `cd` command on all platforms. It stands for 'change directory'.

For example if you currently are in your home directory:
```shell
/home/john/
```
which contain folders `Desktop`, `Documents`, `Music` and `Downloads`, and you wish to move to the `Documents` folder, you will need to use the following command:
```shell
cd Documents
```
hence, using `pwd` will now reflect the changed cwd:
```shell
/home/john/Documents
```

To move up to the parent directory (the directory which contains the current directory, denoted by two dots, `..`), you can use the `cd ..`. So to go from the `Documents` folder back to the home folder, you'd type `cd ..`:
```shell
/home/john/Documents $ cd ..
/home/john $
```
Moreover, to go back to your home directory, regardless of your current location, use the command

 - On Windows: `cd %userprofile%`
 - On MacOS/Linux/Windows: `cd`

Finally, if you wish to move to a directory of which you know the absolute path of, you can pass it to cd in its entirety: `cd <absolute-path>`. So for example, if you wanted to move to the directory `/home/john/Music/Mozart` on MacOS/Linux, or perhaps `C:\Users\john\Music\Mozart` on Windows, you would enter:

 - On Windows: `cd C:\Users\john\Music\Mozart`
 - On MacOS/Linux:`cd /home/john/Music/Mozart`

Now that you have been introduced to these basic navigation controls, use them to navigate to the folder where you had downloaded this exercise in the previous step. You can do this by using `ls` to view the content of you current path, and `cd` to move into or out of directories until you have reached the exercise's directory.

### Running your script

If you haven't already installed Python, consider going to the second task of this assignment and following the instructions.

Now that you've navigated to your exercise (which should contain the `task` folder), run `python task/script.py` to execute the script. It should print a line of text.

### Running tests

You can also run the test by executing `python -m unittest task/tests.py`

*Remember: you may need to use `python3` instead of `python` to run the correct version*

Please make sure that:

 - your Python 3 environment is working correctly and is up to date
 - you know how to navigate the CLI to change directories and list files
 - you are able to execute Python scripts from the CLI

It is absolutely essential to learn these basics at least once. If you have trouble, there are plenty of guides on the internet that can help with these first steps and you may seek assistance from the tutors.

### Two more tips about the CLI:
 - Instead of typing out entire commands or the names of files and folders, you can just type the first few characters and then press <TAB> on your keyboard. For example, `/home/j<TAB>` will automatically be completed to `/home/john` and `pyt<TAB>` will automatically be completed to `python`. If there are multiple possible completions (e.g. `python2`, `python3`), different CLIs will behave differently, but they will generally try to show you or cycle through all possible completions. You may simply need to press <TAB> multiple times to see suggestions or different completions.
 - Instead of retyping commands, you can press Ctrl-R on your keyboard and start typing a command (this does not work in `cmd`, only in PowerShell or on MacOS and Linux). The CLI will then search your command history and show you the last time you typed those characters. For example, `<Ctrl-R>Moz` would immediately suggest `cd /home/john/Music/Mozart` if that was the last command containing the characters `Moz`. Press Ctrl-R multiple types to step back to older matching commands.

### One final word:
The CLI is a powerful tool. It may seem intimidating at first, and it is not as intuitive as a graphical interface, but becoming a proficient CLI user will allow you to get work done more quickly and effectively in the long run. As a programmer, you will never be able to escape the CLI completely anyway, so you may well choose to explore its power for your own benefit. If you wish to learn more about the CLI, you may wish to consult [this guide for MacOS/Linux](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview). Remember you can install Ubuntu in Windows to learn a POSIX-compliant shell. There also exist plenty of tutorials for cmd and PowerShell.


