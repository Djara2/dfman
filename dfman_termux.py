import os
from rich.console import Console
from rich.markdown import Markdown
from math import floor
import pyclip
import config_reader as cr
import modify_settings


VERSION = "ver. 22.06.04.1"

def sort_files_by_extension(files):
    map = {}
    for file in files:
        if "." in file:
            file_as_list = file.split(".")
            extension = file_as_list[len(file_as_list)-1]
            if extension not in map.keys():
                map[extension] = []
            else:
                map[extension].append(file)

    return map

def get_directory_files(path, argument=None):
    directory_contents = os.listdir(path)
    files_list = []
    for file in directory_contents:
        if os.path.isfile(os.path.join(path, file)):
            if argument == None:
                if not "~" in file:
                    files_list.append(file)
            else:
                if argument[0] in ["search", "s"]:
                    search_string = argument[1]
                    if (search_string in file) and (not "~" in file):
                        files_list.append(file)

                if argument[0] == "grouped_extensions":
                    # get ALL files, then filter
                    if not "~" in file:
                        files_list.append(file)

    if argument != None:
        if argument[0] == "grouped_extensions":
            files_map = sort_files_by_extension(files_list)
            files_list = []
            for extension in files_map:
                for file in files_map[extension]:
                    files_list.append(file)

    return files_list

def get_directory_directories(path, argument = None):
    directory_contents = os.listdir(path)
    directories_list = []
    for file in directory_contents:
        if not (os.path.isfile(os.path.join(path, file))):
            if argument == None:
                directories_list.append(file)
            else:
                if argument[0] in ["search", "s"]:
                    search_string = argument[1]
                    if search_string in file:
                        directories_list.append(file)
    return directories_list

console = Console()
current_dir_path = os.getcwd()
current_dir_name = os.path.basename(current_dir_path)
current_dir_md = Markdown(f"# {current_dir_name}")

folders = []
files = []

music_file_types = ["m4a", "mp3", "wav", "ogg", "wma", "webm", "3gp", "aa", "aac", "aax"]
picture_file_types = ["png", "jpg", "jpeg", "gif", "webp", "bmp", "tiff", "tif"]
video_file_types = ["mp4", "mkv", "mov", "webm", "avi", "flv", "mkv", "wmv"]
document_file_types = ["pdf", "md", "docx", "doc", "odt"]
code_file_types = ["py", "cpp", "java", "cpp", "sh", "exe"]

filetype_icon_map = {}
for extension in music_file_types:
    filetype_icon_map[extension] = "🎵"

for extension in picture_file_types:
    filetype_icon_map[extension] = "📷"

for extension in video_file_types:
    filetype_icon_map[extension] = "🎬"

for extension in document_file_types:
    filetype_icon_map[extension] = "📙"

for extension in code_file_types:
    if extension == "py":
        filetype_icon_map[extension] = "🐍"
    if extension == "java":
        filetype_icon_map[extension] = "☕"

    if extension == "cpp":
        filetype_icon_map[extension] = "➕"

    if extension == "exe":
        filetype_icon_map[extension] = "📦"

    if extension == "sh":
        filetype_icon_map[extension] = "📟"


stack = []
up_stack = []
arguments = []

while True:
    os.system("clear")

    settings_dictionary = cr.read_configuration("/data/data/com.termux/files/home/dfman/dfman_config.txt")
    #settings_dictionary = cr.read_configuration("dfman_config.txt")

    if settings_dictionary["DEBUG"] == "True":
        DEBUG = True
    else:
        DEBUG = False

    PROMPT_ICON = settings_dictionary["prompt_icon"]

    if settings_dictionary["double_space_lines"] == "True":
        DOUBE_SPACE_LINES = True
    else:
        DOUBE_SPACE_LINES = False

    ACCENT_COLOR = settings_dictionary["accent_color"]

    TERMINAL_SIZE = os.get_terminal_size()
    TERMINAL_COLUMNS = TERMINAL_SIZE.columns
    TERMINAL_ROWS = TERMINAL_SIZE.lines
    console.print(current_dir_md)
    runner_line = f"[underline]Full path[/] {current_dir_path}"

    # the + 14 is to account for the len function considering the style tags [underline] and [/] as part of the length.
    if settings_dictionary["show_version_number"] == "True":
        amt_spaces = TERMINAL_COLUMNS - len(runner_line) - len(VERSION) + 14
        runner_line += " " * amt_spaces
        runner_line += VERSION
    #console.print(f"[underline]Full path:[/] {current_dir_path}\n{" "}")
    console.print(f"{runner_line}\n")

    if len(arguments) == 0:
        directories = get_directory_directories(current_dir_path)
        files = get_directory_files(current_dir_path)
    else:
        directories = get_directory_directories(current_dir_path, arguments)
        files = get_directory_files(current_dir_path, arguments)

    arguments = []
    whole_dir = directories + files

    x = 0
    while x < (len(whole_dir)):
        str_x = str(x)

        if len(str_x) == 1:
            str_x = f"0{x}"

        icon = None

        current_item = whole_dir[x]

        if len(current_item) > 32:
            current_item_alias = current_item[:30] + "..."

        else:
            current_item_alias = current_item

        if current_item in directories:
            if ACCENT_COLOR == "default":
                line = f"{str_x}. 📁 {current_item_alias}"
            else:
                line = f"[{ACCENT_COLOR}]{str_x}.[/] 📁 [white]{current_item_alias}[/]"

        else:
            icon = "📄"
            if "." in current_item:
                current_item_list = current_item.split(".")
                current_item_file_extension = current_item_list[len(current_item_list)-1]
                if current_item_file_extension in filetype_icon_map.keys():
                    icon = filetype_icon_map[current_item_file_extension]
            if ACCENT_COLOR == "default":
                line = f"{str_x}. {icon} {current_item_alias}"
            else:
                line = f"[{ACCENT_COLOR}]{str_x}[/]. {icon}[white] {current_item_alias}[/]"

        while len(line) <= floor(TERMINAL_COLUMNS/3):
            line += " "

        x += 1
        str_x = str(x)
        if len(str_x) == 1:
            str_x = f"0{x}"

        if x < len(whole_dir):
            current_item = whole_dir[x]
            if len(current_item) > 32:
                current_item_alias = current_item[:30] + "..."
            else:
                current_item_alias = current_item

            if current_item in directories:
                if ACCENT_COLOR == "default":
                    line += f"{str_x}. 📁 {current_item_alias}"
                else:
                    line += f"[{ACCENT_COLOR}]{str_x}.[/] 📁 {current_item_alias}"

            else:
                icon = "📄"
                if "." in current_item:
                    current_item_list = current_item.split(".")
                    current_item_file_extension = current_item_list[len(current_item_list)-1]
                    if current_item_file_extension in filetype_icon_map.keys():
                        icon = filetype_icon_map[current_item_file_extension]
                if ACCENT_COLOR == "default":
                    line += f"{str_x}. {icon} {current_item_alias}"
                else:
                    line += f"[{ACCENT_COLOR}]{str_x}.[/] {icon} {current_item_alias}"


        while len(line) <= 2*floor(TERMINAL_COLUMNS/3):
            line += " "

        x += 1
        str_x = str(x)
        if len(str_x) == 1:
            str_x = f"0{x}"

        if x < len(whole_dir):
            current_item = whole_dir[x]
            if len(current_item) > TERMINAL_COLUMNS - len(line):
                current_item_alias = current_item[:TERMINAL_COLUMNS - len(line) - 16] + "..."
            else:
                current_item_alias = current_item

            if current_item in directories:
                if ACCENT_COLOR == "default":
                    line += f"{str_x}. 📁 {current_item_alias}"
                else:
                    line += f"[{ACCENT_COLOR}]{str_x}.[/] 📁 {current_item_alias}"


            else:
                icon = "📄"
                if "." in current_item:
                    current_item_list = current_item.split(".")
                    current_item_file_extension = current_item_list[len(current_item_list)-1]
                    if current_item_file_extension in filetype_icon_map.keys():
                        icon = filetype_icon_map[current_item_file_extension]
                if ACCENT_COLOR == "default":
                    line += f"{str_x}. {icon} {current_item_alias}"
                else:
                    line += f"[{ACCENT_COLOR}]{str_x}.[/] {icon} {current_item_alias}"

        if DOUBE_SPACE_LINES:
            line += "\n"

        console.print(line)

        x += 1

    if DEBUG:
        print(whole_dir)

    arguments = []
    if DEBUG:
        print(f"Stack: {stack}")

    user_action = input(f"\n{PROMPT_ICON} ")

    if user_action == "exit":
        notice = input("\n\n🔔 Command to navigate to most recent directory will be copied.\n\n✅ To accept this, enter ENTER or Y.\n❌ To REJECT this, enter N.\n\n> ")
        if notice in ["", "y", "Y"]:
            pyclip.copy(f"cd \"{current_dir_path}\"")
        os.system("clear")
        exit()

    if user_action == "settings":
        modify_settings.modify("/data/data/com.termux/files/home/dfman/dfman_config.txt")

    user_action_list = user_action.split()

    if len(user_action_list) == 1:
        input_is_int = True
        try:
            object = int(user_action_list[0])
        except:
            input_is_int = False

        if input_is_int:
            if object < len(whole_dir):
                if whole_dir[object] in directories:
                    stack.append(current_dir_path)
                    current_dir_path += f"/{whole_dir[object]}"
                    current_dir_name = os.path.basename(current_dir_path)
                    current_dir_md = Markdown(f"# {current_dir_name}")
                else:
                    cmd = f"{whole_dir[object]}"
                    cmd = "\"" + current_dir_path + "/" + cmd
                    os.system(f"start \"\" {cmd}")
            else:
                halt = input("Input index is out of bounds. ")
        else:
            if user_action == "dirs":
                arguments.append("dirs")

            if user_action == "g":
                arguments.append("grouped_extensions")

            if user_action in ["cwd", "cdirp"]:
                pyclip.copy(f"cd \"{current_dir_path}\"")

            if user_action in ["back", "b"]:
                if len(stack) >= 1:
                    up_stack.append(current_dir_path)
                    current_dir_path = stack.pop()
                    current_dir_name = os.path.basename(current_dir_path)
                    current_dir_md = Markdown(f"# {current_dir_name}")
                else:
                    if DEBUG:
                        print(f"Current dir path: {current_dir_path}")
                        print(f"Current dir name: {current_dir_name}")

                    # extra minus 1 so as to remove the final \ character (this was preventing going down one level in earlier versions)
                    up_stack.append(current_dir_path)
                    current_dir_path = current_dir_path[:len(current_dir_path) - len(current_dir_name) - 1]

                    """
                    this is to fix an error where the C: drive could not be displayed because a \ character was missing from the path. It is a hard-coded fix, but still a fix.
                    """
                    if current_dir_path == "C:":
                        current_dir_path = "C:\\"

                    current_dir_name = os.path.basename(current_dir_path)

                    if DEBUG:
                        print(f"rendered dir path: {current_dir_path}")
                        print(f"Current dir name: {current_dir_name}")

                    # Finally, create a markdown object for the basename of the directory path, so that it can be rendered pretty in the terminal using the Python rich library
                    current_dir_md = Markdown(f"# {current_dir_name}")

            if user_action == "gui":
                os.system(f"explorer \"{current_dir_path}\"")

            if user_action == "up":
                if len(up_stack) != 0:
                    current_dir_path = up_stack.pop()
                    current_dir_name = os.path.basename(current_dir_path)
                    current_dir_md = Markdown(f"# {current_dir_name}")

    elif len(user_action_list) > 1:
        if user_action[0] == "!":
            os.system(user_action[1:])
        if user_action == "go back":
            if len(stack) > 0:
                current_dir_path = stack.pop()
                current_dir_name = os.path.basename(current_dir_path)
                current_dir_md = Markdown(f"# {current_dir_name}")
            else:
                current_dir_path = current_dir_path[:len(current_dir_path) - len(current_dir_name)]
                current_dir_name = os.path.basename(current_dir_path)
                current_dir_md = Markdown(f"# {current_dir_name}")

        if user_action_list[0] in ["search", "s"]:
            for x in range(len(user_action_list)):
                arguments.append(user_action_list[x])

        if user_action_list[0] == "mkdir":
            if len(user_action_list) == 2:
                new_dir_name = user_action_list[1]
            else:
                new_dir_name = ""
                for x in range(1, len(user_action_list)):
                    new_dir_name += (user_action_list[x] + " ")

                #new_dir_name += "\""

            os.system(f"mkdir \"{current_dir_path}/{new_dir_name}\"")

        if user_action_list[0] in ["options", "o"]:
            object = int(user_action_list[1])
            if object < len(whole_dir):
                object = whole_dir[object]

                print(f"\nOptions for {object}:\n\n1. ❌ Cancel\n2. 📝 Edit with vim\n3. 👀 Open with readmd\n4. 🐈 Read with cat cmd\n5. 🔖 Rename\n6. 🚮 Delete\n\n")

                safe_selection_made = False

                while not safe_selection_made:
                    selection = input("Selection? ")
                    try:
                        selection = int(selection)
                        safe_selection_made = True
                    except:
                        console.print("[red]Input is not an integer corresponding to the options list.[/]\n")

                if selection == 2:
                    extension = object.split(".")
                    extension = extension[len(extension)-1]
                    cmd = f"vim \"{current_dir_path}/{object}\""
                    os.system(cmd)

                if selection == 3:
                    if DEBUG:
                        print(f"Got directory as: {current_dir_path}\n\nGot file as: {object}\n\nGot full file path as: \"{current_dir_path}/{object}\"")
                    cmd = "readmd \"" + current_dir_path + "/" + object + "\""
                    if DEBUG:
                        halt = input("Continue? ")
                    os.system(cmd)
                    halt = input("Press ENTER to continue ")

                if selection == 4:
                    os.system(f"cat \"{current_dir_path}/{object}\"")
                    halt = input("\n\nPress ENTER to continue ")

                if selection == 5:
                    console.print(f"\n💡 enter blank string (just hit ENTER) to cancel operation\n")
                    rename = input("Rename file to? ")
                    if rename != "":
                        if os.path.isfile(os.path.join(current_dir_path, object)):
                            extension = object.split(".")
                            extension = extension[len(extension)-1]
                            newname = rename + "." + extension
                            if DEBUG:
                                print(f"Got extension as: {extension}")
                                print(f"Got newname as: {newname}")
                                print(f"Command is: rename {object} {newname}")
                            os.system(f"mv \"{current_dir_path}/{object}\" \"{current_dir_path}/{newname}\"")
                        else:
                            if DEBUG:
                                print(f"file is: {object}")
                            rename = f"\"{rename}\""
                            os.system(f"mv \"{current_dir_path}/{object}\" \"{current_dir_path}/{rename}\"")
                    #newname = current_dir_path + "\\" + rename + "." + extension
                    #newname = "\"" + newname + "\""


                if selection == 6:
                    warning = console.print(f"\n❗ Are you [underline]SURE[/] you want to delete [italic]{object}[/]?\n")
                    confirm = input("> ")
                    if confirm in ["y", "yes", "Y", "Yes"]:
                        is_dir = (object in directories)
                        object = "\"" + current_dir_path + "/" + object + "\""
                        if not is_dir:
                            os.system(f"rm \"{object}\"")
                        else:
                            os.system(f"rmdir {object}")


            else:
                halt = input("Input index is out of bounds ")



    if DEBUG:
        halt = input("Press enter to continue ")
