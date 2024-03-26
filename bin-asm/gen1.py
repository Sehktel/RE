#-------------------------------------------------------------------------------
# Name:        generator 00-FF
# Purpose:
#
# Author:      Sehktel
#
# Created:     26.03.2024
# Copyright:   (c) Sehktel 2024
# Licence:     MIT
#-------------------------------------------------------------------------------

def main():

    for i in range(256):
        print(f"{i:02X}",end="")
        print(f"{i:02X}",end="")
        print(f"{i:02X}",end="")

        print(f"{i:02X}",end="")
        print(f"{i:02X}",end="")
        print(f"{i:02X}",end="")
        #print()
    pass

if __name__ == '__main__':
    main()
