#-------------------------------------------------------------------------------
# Name:        13.11 Prob 1
# Purpose:
#
# Author:      drherrera
#
# Created:     04/11/2025
# Copyright:   (c) drherrera 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

myfile = open("oldfile.txt", "w")
myfile.write("Frost Monarch. Do not assume the position of KING with only that much power\n")
myfile.close()


lines = open("oldfile.txt").readlines()

out = open("newfile.txt", "w")

c = len(lines) - 1

while c >= 0:
    out.write(lines[c])
    c -= 1

out.close()
