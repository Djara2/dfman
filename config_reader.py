def read_configuration(filename, DEBUG = False):
    return_dictionary = {}
    file = open(filename, "r")
    for line in file:
        if line != "\n":
            if DEBUG:
                print(f"Original line:\n\n{line}")
            line = line.split(": ")
            if DEBUG:
                print(f"\n\nLine after split:\n\n{line}")
            setting = line[0]
            argument = line[1]
            argument = argument[0:len(argument)-1]
            if DEBUG:
                print(f"Setting \"{setting}\" is set to \"{argument}\"")
            return_dictionary[setting] = argument
    file.close()
    return return_dictionary

def restore_objects(filename, DEBUG = False):
    file = open(filename, "r")
    object_dictionary = {}
    attributes = []
    last_key = None
    for line in file:
        if line != "\n":
            if DEBUG:
                print(f"Got line:\n\n{line}")

            if "\t" in line:
                obj_name = line
                obj_name = obj_name[0:len(obj_name)-1]
                object_dictionary[obj_name] = None
                last_key = obj_name

            else:
                line = line[0:len(line)-1]
                attributes.append(line)
            object_dictionary[last_key] = line
