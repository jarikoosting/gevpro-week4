#!/opt/local/bin/python3.4
# Jarik Oosting, 27-02-2015

import sys
import xml.etree.ElementTree as ET

def main(argv):

    if len(argv) == 3:
        tree = ET.parse(argv[1])
        root = tree.getroot()

        for child in root.findall('POINT'):
            bottom = int(child.find('BOTTOM_HZ').text)
            top = int(child.find('TOP_HZ').text)
            start = float(child.find('F0_START').text)
            end = float(child.find('F0_END').text)

            if not (bottom <= start <= top) or not (bottom <= end <= top):
                root.remove(child)

        tree.write(argv[2])

    else:
        print("Wrong commands used.")

if __name__ == "__main__":
    main(sys.argv)
