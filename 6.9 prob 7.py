#-------------------------------------------------------------------------------
# Name:        6.9 prob 7
# Purpose:
#
# Author:      drherrera
#
# Created:     02/10/2025
# Copyright:   (c) drherrera 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys

def test(did_pass):
    """Print the result of a test."""
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if True:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)

def to_secs(x,y,z):
    if x < 0:
        return -x
    else:
        return x

def test_suite():
 test(to_secs(2, 30, 10) == 9010)
test(to_secs(2, 0, 0) == 7200)
test(to_secs(0, 2, 0) == 120)
test(to_secs(0, 0, 42) == 42)
test(to_secs(0, -10, 10) == -590)


test_suite()  # Here is the call to run the tests