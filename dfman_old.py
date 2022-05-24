import os
from rich.console import Console
from rich.markdown import Markdown
from math import floor
import pyclip
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

DEBUG = False

console = Console()
current_dir_path = os.getcwd()
current_dir_name = os.path.basename(current_dir_path)
current_dir_md = Markdown(f"# {current_dir_name}")
folders = []
files = []

music_file_types = ["m4a", "mp3", "wav", "ogg", "wma"]
picture_file_types = ["png", "jpg", "jpeg", "gif"]
video_file_types = ["mp4", "mkv", "mov", "webm"]
code_file_types = ["py", "cpp", "java", "cpp", "sh", "exe"]

filetype_icon_map = {}
for extension in music_file_types:
    filetype_icon_map[extension] = "🎵"

for extension in picture_file_types:
    filetype_icon_map[extension] = "🎴"

for extension in video_file_types:
    filetype_icon_map[extension] = "🎬"

for extension in code_file_types:
    if extension == "py":
        filetype_icon_map[extension] = "🐍"
    if extension == "java":
        filetype_icon_map[extension] = "☕"

    if extension == "cpp":
        filetype_icon_map[extension] = "🇨"

    if extension == "exe":
        filetype_icon_map[extension] = "📦"


stack = []
arguments = []

while True:
    os.system("cls")
    TERMINAL_SIZE = os.get_terminal_size()
    TERMINAL_COLUMNS = TERMINAL_SIZE.columns
    TERMINAL_ROWS = TERMINAL_SIZE.lines
    console.print(current_dir_md)
    console.print(f"[underline]Full path:[/] {current_dir_path}\n")
    
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
            if len(arguments) == 0:
                line = f"{str_x}. 📁 {current_item_alias}"
            else:
                if arguments[0] in ["search", "s"]:
                    if arguments[1] in current_item:
                        line = f"{str_x}. 📁 {current_item_alias}"
                if arguments[0] == "dirs":
                    line = f"{str_x}. 📁 {current_item_alias}"

        else:
            icon = "📄"
            if "." in current_item:
                current_item_list = current_item.split(".")
                current_item_file_extension = current_item_list[len(current_item_list)-1]
                if current_item_file_extension in filetype_icon_map.keys():
                    icon = filetype_icon_map[current_item_file_extension]
            if len(arguments) == 0:
                line = f"{str_x}. {icon} {current_item_alias}"
            else:
                if arguments[0] in ["search", "s"]:
                    if arguments[1] in current_item:
                        line = f"{str_x}. {icon} {current_item_alias}"

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
                if len(arguments) == 0:
                    line += f"{str_x}. 📁 {current_item_alias}"
                else:
                    if arguments[0] in ["search", "s"]:
                        if arguments[1] in current_item:
                            line += f"{str_x}. 📁 {current_item_alias}"
                    if arguments[0] == "dirs":
                        line += f"{str_x}. 📁 {current_item_alias}"

            else:
                icon = "📄"
                if "." in current_item:
                    current_item_list = current_item.split(".")
                    current_item_file_extension = current_item_list[len(current_item_list)-1]
                    if current_item_file_extension in filetype_icon_map.keys():
                        icon = filetype_icon_map[current_item_file_extension]
                if len(arguments) == 0:
                    line += f"{str_x}. {icon} {current_item_alias}"

                else:
                    if arguments[0] in ["search", "s"]:
                        if arguments[1] in current_item:
                            line += f"{str_x}. {icon} {current_item_alias}"

        while len(line) <= 2*floor(TERMINAL_COLUMNS/3):
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
                if len(arguments) == 0:
                    line += f"{str_x}. 📁 {current_item_alias}"

                else:
                    if arguments[0] in ["search", "s"]:
                        if arguments[1] in current_item:
                            line += f"{str_x}. 📁 {current_item_alias}"
                    if arguments[0] == "dirs":
                        line += f"{str_x}. 📁 {current_item_alias}"

            else:
                icon = "📄"
                if "." in current_item:
                    current_item_list = current_item.split(".")
                    current_item_file_extension = current_item_list[len(current_item_list)-1]
                    if current_item_file_extension in filetype_icon_map.keys():
                        icon = filetype_icon_map[current_item_file_extension]

                if len(arguments) == 0:
                    line += f"{str_x}. {icon} {current_item_alias}"
                else:
                    if arguments[0] in ["search", "s"]:
                        if arguments[1] in current_item:
                            line += f"{str_x}. {icon} {current_item_alias}"

        console.print(line)

        x += 1

    if DEBUG:
        print(whole_dir)

    arguments = []
    user_action = input("\n> ")
    if user_action == "exit":
        os.system("cls")
        exit()

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
                    current_dir_path += f"\\{whole_dir[object]}"
                    current_dir_name = os.path.basename(current_dir_path)
                    current_dir_md = Markdown(f"# {current_dir_name}")
                else:
                    cmd = f"{whole_dir[object]}"
                    cmd = "\"" + current_dir_path + "\\" + cmd
                    os.system(f"start \"\" {cmd}")
            else:
                halt = input("Input index is out of bounds. ")
        else:
            if user_action == "dirs":
                arguments.append("dirs")
            if user_action in ["cwd", "cdirp"]:
                pyclip.copy(f"cd \"{current_dir_path}\"")
            if user_action in ["back", "b"]:
                if len(stack) != 0:
                    current_dir_path = stack.pop()
                    current_dir_name = os.path.basename(current_dir_path)
                    current_dir_md = Markdown(f"# {current_dir_name}")
                else:
                    current_dir_path = current_dir_path[:len(current_dir_path) - len(current_dir_name)]
                    current_dir_name = os.path.basename(current_dir_path)
                    current_dir_md = Markdown(f"# {current_dir_name}")

            if user_action == "gui":
                os.system(f"explorer \"{current_dir_path}\"")

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
                new_dir_name = "\""
                for x in range(1, len(user_action_list)):
                    new_dir_name += (user_action_list[x] + " ")

                new_dir_name += "\""

            os.system(f"mkdir \"{current_dir_path}\\{new_dir_name}\"")

        if user_action_list[0] in ["options", "o"]:
            object = int(user_action_list[1])
            if object < len(whole_dir):
                object = whole_dir[object]
                print(f"\nOptions for {object}:\n\n1. 📝 Edit with vim\n2. 👀 Open with readmd\n3. 🔖 Rename\n4. 🚮 Delete\n5. ❌ Cancel\n\n")
                safe_selection_made = False
                while not safe_selection_made:
                    selection = input("Selection? ")
                    try:
                        selection = int(selection)
                        safe_selection_made = True
                    except:
                        console.print("[red]Input is not an integer corresponding to the options list.[/]\n")
                
                if selection == 1:
                    extension = object.split(".")
                    extension = extension[len(extension)-1]
                    cmd = f"vim \"{current_dir_path}\\{object}\""
                    os.system(cmd)
                
                if selection == 2:
                    cmd = f"readmd \"{current_dir_path}\\{object}\""
                    os.system(cmd)
                    halt = input("Press ENTER to continue ")

                if selection == 3:
                    rename = input("Rename file to? ")
                    extension = object.split(".")
                    extension = extension[len(extension)-1]
                    #newname = current_dir_path + "\\" + rename + "." + extension
                    #newname = "\"" + newname + "\""
                    newname = rename + "." + extension
                    os.system(f"rename {object} {newname}")

                if selection == 4:
                    is_dir = (object in directories)
                    object = "\"" + current_dir_path + "\\" + object + "\""
                    if not is_dir:
                        os.system(f"del {object}")
                    else:
                        os.system(f"rmdir {object}")


            else:
                halt = input("Input index is out of bounds ")



    if DEBUG:
        halt = input("Press enter to continue ")
