#!/usr/bin/env python3
import ipdb

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    np1 = NationalPark("Yosemite")
    np2 = NationalPark("Garden of the Gods")
    np3 = NationalPark("Rocky Mountain")

    v1 = ("Killian")
    v2 = ("Katie")
    v3 = ("Emily")

    t1 = (np2, v3, "January 1st", "February 3rd")
    t2 = (np1, v2, "January 1st", "February 3rd")
    t3 = (np3, v1, "January 1st", "February 3rd")
    t4 = (np2, v1, "February 3rd", "March 2nd")

    ipdb.set_trace()
