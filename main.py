import os
import json

'''
Standard paths:


Vanilla Ideas
C:\Program Files (x86)\Steam\steamapps\common\Europa Universalis IV\common\ideas

'''


def set_up():
    if not os.path.exists('settings.json'):
        if input("Try standard paths? [y/n]") == "n":
            settings_file = open('settings.json', 'w')
            mdp = input("Mod directory path (Most likely Documents/Paradox Interactive/Europa Universalis IV/mod)")
            fmf = input("Which folder should the finished mod go into?")
            iloc = input(
                "Where are the ideas you'd like to multiply located (Insert Path)? (For example C:\Program Files (x86)\Steam\steamapps\common\Europa Universalis IV\common\ideas)")
            gmloc = input(
                "Where is the game located? (For example C:\Program Files (x86)\Steam\steamapps\common\Europa Universalis IV)")

            dictionary = {"mod_directory_path": mdp, "finished_mod_folder": fmf, "game_location": gmloc,
                          "ideas_location": iloc}

            json.dump(dictionary, settings_file)
            settings_file.close()


def get_json_values():
    json_values = json.load(open('settings.json', 'r'))
    print(json_values)
    return json_values


def get_mdp(json_values):
    try:
        return json_values["mod_directory_path"]
    except:
        print("An error occurred while trying to get the mod directory path")


def get_fmf(json_values):
    try:
        return json_values["finished_mod_folder"]
    except:
        print("An error occurred while trying to get the mod saving path")


def get_iloc(json_values):
    try:
        return json_values["ideas_location"]
    except:
        print("An error occurred while trying to get the idea location")


def get_gmloc(json_values):
    try:
        return json_values["game_location"]
    except:
        print("An error occurred while trying to get the game path")


def make_mod(mdp, fmf, iloc, gmloc, choice):
    multiplier = int(input("Which (absolute) number do you want to multiply the values with?"))
    idea_source = open(os.path.join(iloc, os.listdir(iloc)[choice]), 'r').read()

    cycle_length = 10
    cycler = 0
    cpic = 0  # Current process in cycle

    the_mega_array = idea_source.split('{')

    for c in range(int(len(the_mega_array) / cycle_length)):
        for si in range(len(the_mega_array)):

            s = the_mega_array[si+cycler*cycle_length]

            if cpic == cycle_length: # Check whether current cycle is finished
                break

            s.replace(' ', '')
            s.replace('=', '')
            s.replace('_ideas', '')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    set_up()

    json_values = get_json_values()  # Retrieving file information

    eu4_mod_dir_path = get_mdp(json_values)
    finished_mod_folder = get_fmf(json_values)
    ideas_location = get_iloc(json_values)
    game_location = get_gmloc(json_values)

    print("Which ideas do you want to multiply?")
    i = 0
    for file_path in os.listdir(ideas_location):
        print("To open " + file_path + "\nEnter [" + str(i) + "]")
        i += 1

    choice = int(input("Enter number now: "))

    make_mod(mdp=eu4_mod_dir_path, fmf=finished_mod_folder, iloc=ideas_location, gmloc=game_location, choice=choice)
