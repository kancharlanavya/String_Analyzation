#!/usr/bin/python


import logging as log
import sys

try:
    import json
except ImportError:
    import simplejson as json


class analyze_string(object):
    input_string= ""

    def __init__(self,  *argv):
        if argv:                                # To Check if an argument is passed or not
            self.input_string = argv[0]         # As of now we are verifying only for first variable
        else:
            self.input_string = None            # Incase a class is initialized with out input we are assigning None string

    def longest_word(self):
        try:
            input_list = self.input_string.split(' ')   # Split the sentence into string
            return sorted(input_list, key=len)[-1]
        except Exception, e:
            log.error (e)
            return []

    def length(self):
        longest_string = self.longest_word()
        if longest_string:
            print ("Longest string = %s" %(longest_string))
            print ("Length of longest string = %s" % (len (longest_string)))
        else:
            log.warning("Null String provided as input")
        pass




def init_analyze_string(input_string):
    student = analyze_string(input_string)
    student.length()


if len(sys.argv) < 2:
    log.error("Sufficient inputs are missing to process, Exiting...")
else:
    init_analyze_string(sys.argv[1])

