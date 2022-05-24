# Getting Started with dfman

- ❗ You _cannot_ just install dfman and get it working, you will have to make a few changes, and these changes will require you to modify just a little bit of source code.
    - Later, I will implement a method by which to automatically make it so that you do not have to modify the source code, but until then, you will have to modify the source code to get it working.

# Requirement 1: Add dfman.exe to your system variables

1. Hit START
2. Type "system variables" in the search pane
3. Select the option "Edit the system environment variables"
4. Select "Environment Variables" in the bottom right.
5. Hit the NEW button under the listbox labeled "User variables for [your user name here]"
6. Make the variable name "dfman"
7. Make the variable value the path of your dfman.exe file (e.g. C:\Users\USERNAME\Desktop\dfman\dfman.exe)

# Requirement 2: Modify source code

- _Why do I have to do this?_ the dfman program is actually coded entirely in Python, but there is a dfman.exe file so that it can be called from the start menu easily, or from any directory in the terminal by just entering "dfman" as your command.
    - The dfman.cpp file needs to know where your dfman.py file is located, as dfman.cpp (compiled into dfman.exe) is only a front to call the dfman.py file
    - In turn, once the dfman.py file is called, it will need to know the location of your dfman_config.txt file

1. Edit the dfman.cpp file. There is a line of code commented "MODIFY THIS SO THAT THE PATH IS THE PATH FOR YOUR DFMAN.PY FILE" -- Change the assignment of the string `string_cmd` to the location of your dfman.py file. ❗ Do not forget to put two \ characters for instead of just one in the path. C++ will interpret it as an escape character for whatever letter comes after, instead of as the literal \ character if you forget to do this.

2. Edit the dfman.py file. 
    - There are 2 lines you have to change:
        - `settings_dictionary = cr.read_configuration("C:\\Users\\jjara\\OneDrive\\Desktop\\Programming\\dfman\\dfman_config.txt")` 
            - change the argument (C:\\Users...) to the location of your dfman_config.txt file
        - `modify_settings.modify("C:\\Users\\jjara\\OneDrive\\Desktop\\Programming\\dfman\\dfman_config.txt")` 
            - again, change the argument to the location of your dfman_config.txt file

## Why are you using Python? It's slow

1. Easier to code
2. It's fast enough for me
3. Python's Rich library makes it easy to display the graphics in a clean way
4. I'm more familiar with Python than any other language.

# Requirement 3: Compile dfman

- Enter this command in your directory where you originally downloaded all the dfman files: `g++ dfman.cpp -o dfman`

- ❓ If you do not have the g++ compiler installed on your system, [follow this link to get the g++ command working](https://www.instructables.com/How-to-Install-MinGW-GCCG-Compiler-in-Windows-XP78/) -- ignore step 1 in the article


