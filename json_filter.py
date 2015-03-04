#!/opt/local/bin/python3
# Jarik Oosting, 27-02-2015

import json
from collections import namedtuple

def main():

    with open("blood-die.json", "r") as in_f:
        file = json.load(in_f)
        JsonTuple = namedtuple("JsonTuple",("language","classification","blood","die"))

        with open("result.json","w") as output:

            for element in file:

                element = [s.encode("utf-8") for s in element]

                elements = JsonTuple(element[0], element[1], element[2].split(), element[3].split())

                [json.dump(element,output) for el in elements[2] if el in elements[3]]

if __name__ == "__main__":
    main()