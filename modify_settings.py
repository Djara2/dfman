import os
from rich.console import Console
from rich.markdown import Markdown
import config_reader as cr

def display_settings(setting_dictionary):
    con = Console()
    color = "default"
    x = 0
    entire_print = ""
    for setting in setting_dictionary.keys():
        if setting_dictionary[setting] == "True\n":
            color == "green"

        if setting_dictionary[setting] == "False\n":
            color = "red"

        if color != "default":
            con.print(f"{x}. {setting}: [{color}]{setting_dictionary[setting]}[/]")
            #entire_print += f"{x}. {setting}: [{color}]{setting_dictionary[setting]}[/]\n"
        else:
            con.print(f"{x}. {setting}: [white]{setting_dictionary[setting]}[/]")
            #entire_print += f"{x}. {setting}: {setting_dictionary[setting]}\n"
        x += 1

def modify(filename):
    con = Console()


    command = ""

    while command != "exit":

        os.system("cls")
        con.print(Markdown("# Settings"))
        print()
        settings_dictionary = cr.read_configuration(filename)
        display_settings(settings_dictionary)

        command = input("\nModify which # setting?: ")
        command_is_int = False
        try:
            command = int(command)
            command_is_int = True
        except:
            con.print(f"\n[red]Error:[/] input \"{command}\" is not an integer.")

        if command_is_int:

            x = 0
            file = open(filename, "r", encoding = "utf-8")
            lines = ""
            for line in file:
                if x == command:
                    split_line = line.split(":")
                    setting = split_line[0]
                    state = input(f"\nWhat do you want to set {setting} to?: ")
                    if " " in state:
                        state = f"\"{state}\""
                    line = f"{setting}: {state}\n"
                x += 1
                lines += line
            file.close()
            file = open(filename, "w")
            file.writelines(lines)
            file.close()
