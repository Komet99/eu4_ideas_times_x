import os
import json


def load(path):
    pdx_obj = []
    file = open(path)
    while True:
        lines = file.readlines()
        i = 0
        for i in range(len(lines)):
            line = lines[i]
            if [*line][-1] != "#":
                parts = line.split("=")
                header = parts[0].strip()
                values = []

                i += 1
                while lines[i][0:4] == "    ":
                    line_v = lines[i][4:]
                    if [*line_v][-1] != "#":
                        parts_v = line_v.split("=")
                        header_v = parts_v[0].strip()

                pdx_obj[i] = [{"header": header,
                                   "values": [

                ]}]
            if not line:
                break


load("C:/Program Files (x86)/Steam/steamapps/common/Europa Universalis IV/common/ideas/00_country_ideas.txt")
