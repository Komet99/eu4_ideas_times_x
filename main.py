import os
import json
import pdx

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
                "Where are the ideas you'd like to multiply located (Insert Path)? (For example C:/Program Files ("
                "x86)/Steam/steamapps/common/Europa Universalis IV/common/ideas)")
            gmloc = input(
                "Where is the game located? (For example C:/Program Files (x86)/Steam/steamapps/common/Europa "
                "Universalis IV)")

            dictionary = {"mod_directory_path": mdp, "finished_mod_folder": fmf, "game_location": gmloc,
                          "ideas_location": iloc}

            json.dump(dictionary, settings_file)
            settings_file.close()
        return False
    else:
        return True


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
    multiplier = float(input("Which  number do you want to multiply the values with? "))
    idea_source = os.path.join(iloc, os.listdir(iloc)[choice])

    ideas_name = os.path.basename(idea_source)

    idea_dict = pdx.load(idea_source)

    for idea_key in idea_dict.keys():
        for i, (k, v) in enumerate(idea_dict[idea_key].items()):
            if type(v) == dict:
                vals = {}
                for e in range(len(v)):
                    # print("v: " + str(v))
                    for (v_key, v_val) in enumerate(v.items()):
                        try:
                            float(v_val[1])
                            adj_val = round(float(v_val[1]) * multiplier, 2)
                            if adj_val == 0.99:
                                adj_val = 1
                            if adj_val == 0.66:
                                adj_val = 0.67

                            # Exceptions for values that would not make sense to be above hundred
                            if str(v_val[0]) == "religious_unity" and adj_val > 1:
                                vals["tolerance_own"] = {adj_val - 1}
                                adj_val = 1
                            elif str(v_val[0]) == "cav_to_inf_ratio" and adj_val > 1:
                                vals["cavalry_cost"] = {-1 * (adj_val - 1)}
                                adj_val = 1
                            elif str(v_val[0]) == "land_forcelimit":
                                adj_val = v_val[1]
                            elif str(v_val[0]) == "vassal_forcelimit_bonus":
                                adj_val = v_val[1]
                            elif str(v_val[0]) == "capture_ship_chance" and adj_val > 1:
                                vals["naval_morale"] = {adj_val - 1}
                                adj_val = 1

                            vals[v_val[0]] = adj_val

                        except:
                            vals[v_val[0]] = v_val[1]

                idea_dict[idea_key][k] = vals

    # Create Path
    # Mod name
    mod_name = (str(len(os.listdir(finished_mod_folder))) + "__" + ideas_name[:-3] + "_times_"
                + str(multiplier)).replace(".", "_point_")

    # Path variable
    dir_path = os.path.join(finished_mod_folder,
                            mod_name)
    # Create folders
    os.mkdir(dir_path)
    os.mkdir(os.path.join(dir_path, "common"))
    os.mkdir(os.path.join(dir_path, "common", "ideas"))

    # Create File
    file = open(os.path.join(dir_path, "common\\ideas\\", ideas_name), "x")
    pdx.dump_dict(idea_dict, os.path.join(dir_path, "common\\ideas\\", ideas_name))

    # Created ideas
    descriptor_file = open(os.path.join(dir_path, "descriptor.mod"), 'w')
    desc_string = ('version="1"\n'
                   'tags={\n\t"gameplay"\n}\n'
                   'name="' + mod_name.replace("_", " ") + '"\n'
                                                           'supported_version="latest"\n')

    descriptor_file.write(desc_string)
    descriptor_file.close()

    mod_file = open(os.path.join(eu4_mod_dir_path, mod_name + ".mod", ), "w")

    mod_file.write(desc_string)
    mod_file.write(('path="' + dir_path.replace(str("\\"), "/") + '"'))
    mod_file.close()
    print("Created mod " + mod_name + " at " + dir_path)


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
