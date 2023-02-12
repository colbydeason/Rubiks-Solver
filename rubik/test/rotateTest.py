from unittest import TestCase
from rubik.view.rotate import rotate
 
class RotateTest(TestCase):
        
    # Analysis of rotate:
    #     
    #     Parameters:
    #         parms: dictionary with 'cube', 'dir', and 'status'
    #             'dir' -> string of characters, validated and used by cube
    #             'cube' -> string, 54 characters, 6 unique characters [a-zA-Z0-9],
    #                       5, 14, 23, 32, 41, and 50 characters must be unique:
    #                       mandatory, arrives un-validated 