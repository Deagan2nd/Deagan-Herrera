#-------------------------------------------------------------------------------
# Name:        11.22 Prob 10
# Purpose:
#
# Author:      drherrera
#
# Created:     21/10/2025
# Copyright:   (c) drherrera 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def replace(s, old, new):
    parts = s.split(old)
    return new.join(parts)


def test(did_pass):
    if did_pass:
        print("test passed.")
    else:
        print("test failed.")

s = "I am the record of your bitter struggle. I am the evidence of your resistance. I am the reward of your pain. I am death, I am eternal rest and I am terror, I am YOU"
test(replace(s, "I" , "you")) == "you am the record of your bitter struggle. you am the evidence of your resistance. you am the reward of your pain. you am death, you am eternal rest and you am terror, you am YOU"