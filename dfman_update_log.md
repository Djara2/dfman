# May 20 2022

- This update has base system name 22.05.22

## Version 22.05.20.1

- Improved system for handling display arguments.
    - For example, if a user wants to search for files containing certain text, this is now handled by the `get_directory_files` and `get_directory_directories` methods, instead of in the general display method in the main part of the code.

    - Doing this has ensured that users get properly ordered files too when searching, and no duplicate files. Formerly, users would see only 10 or so files, but they would have indices of 60 and higher. They would also see several repeats of the same file. This was unacceptable and the new method works wayyyy better.

- Added ability to view files grouped by extension type (experimental)
    - If you enter "g" as your command, all files will be displayed grouped by their file type.
    - __Issues__
        - Directories will not show up
        - Some files will not show up. For example, I have noticed that music and video files will not appear in the display. I am working on this.

- __Resolved and Unresolved Kanban:__
    - This is the initial version where I am keeping track of work on my project, so thusfar there is nothing really.
    - ❌ Render ALL files in "g" mode

## Version 22.05.20.2

- Added program version to the header, right aligned after the full path text.
- The program version uses math to understand its positioning, and will resize according to your terminal size.

- __Resolved and Unresolved Kanban:__
    - ❌ Render ALL files in "g" mode


## Version 22.05.20.3

- Fixed issue where you could down a level with the b, back, goback, or go back commands. Now you can. Effectively, this will allow you to navigate the entire file system.
- Discovered


# May 23, 2022

- This update has the base name 22.05.23

## Version 22.05.23.1

- Program is now configurable!
    - _dfman_ utilizes 2 files I wrote, _configuration_reader_, and _modify_settings_ to modify a file called _dfman_config.txt_. You can change this file from your file system or directly from dfman.
    - To modify in dfman:
        - For your input, enter "settings" -- this will start the interface for modifying the config file
    - Settings:
        - For now there are only 3 settings, but there will be more to come:
            1. DEBUG (turn DEBUG on or off without having to edit source code)
            2. prompt_icon (the icon on the dfman command line)
            3. show_version_number (turns on/off display of application version number in top right)

# May 24, 2022

- This version has the base name 22.05.24

## Version 22.05.24

- ✅ Fixed old error where the contents of the C: drive could not be displayed
- 🆕 Added new customization options -- "accent_color" in config file. Enter command `settings` to play around with this
- 🆕 dfman is now on Github
- 🆕 Added new `up` command, which takes you to your last visited directory. Say you entered `b` to go down a level in your path (e.g. from Program Files to C: drive) -- if you enter `up` after this, it will take you back to Program Files
