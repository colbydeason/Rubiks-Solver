'''
Created on Jan 31, 2023

@author: Colby Deason
'''
import unittest
import rubik.model.cube as Cube


class Test(unittest.TestCase):

    # Analysis of Cube:
    #     
    #    Cube: class, instance of a state machine, maintain internal state (don't allow changes of state from the outside)
    #    Methods: __init__ => instantiates a cube from a string denoting the colors on the cube
    #             get      => returns string of internal representation of the cube
    #             rotate   => rotates the cube based on the 'dir' key
    #    
    #    Analysis of Cube.rotate
    #        inputs:
    #            directions: string, len >= 0, in[FfRrBbLlUu]; optional, defaults to F if missing; unvalidated
    #        outputs:
    #            nominal:
    #                return serialized rotated cube
    #            abnormal:
    #                raise DirException
    #            side-effects: internal state change of cube
    #
    #        happy path:
    #            test 001: F rotation
    #            test 002: f rotation
    #            test 003: B rotation
    #            test 004: b rotation
    #            test 005: L rotation
    #            test 006: l rotation 
    #            test 007: R rotation
    #            test 008: r rotation
    #            test 009: U rotation
    #            test 010: u rotation
    #            test 011: missing direction
    #            test 012: empty direction - ""
    #            test 013: multiple character rotation
    #            
    #        sad path:
    #            test 901: invalid direction
    #
    #        evil path:
    #            none
    
    rngCube = ""
    
    def test_cubeTest_rotate_001_FRotation(self):
        
    
    
    def testName(self):
        pass
