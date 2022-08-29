import os
import json


def load(path):
    file = open(path)
    while True:
        line = file.readline()
        for character in [*line]:
            print(character)
        if not line:
            break


load("C:/Program Files (x86)/Steam/steamapps/common/Europa Universalis IV/common/ideas/00_country_ideas.txt")
