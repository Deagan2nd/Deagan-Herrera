#-------------------------------------------------------------------------------
# Name:        7.26 prob 9
# Purpose:
#
# Author:      drherrera
#
# Created:     09/10/2025
# Copyright:   (c) drherrera 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def print_triangular_numbers(n):
    start = 1
    end = 0
    while start <= n:
        end += start
        print(str(start) + "\t" + str(end))
        start += 1

print_triangular_numbers(5)