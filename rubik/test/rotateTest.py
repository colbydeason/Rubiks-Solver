from unittest import TestCase
from rubik.view.rotate import rotate
 
class RotateTest(TestCase):
        
    # Analysis of rotate:
    #     
    #     Parameters:
    #         parms: dictionary with 'cube', and 'dir'
    #             'dir' -> string of characters, mandatory, arrives un-validated but is validated in cube.py
    #             'cube' -> string, 54 characters, 6 unique characters [a-zA-Z0-9],
    #                       5, 14, 23, 32, 41, and 50 characters must be unique:
    #                       mandatory, arrives un-validated but is validated by cube.py
    #
    #         outputs:
    #             nominal: 
    #                 result -> dictionary with the following entries
    #                     'cube' -> successfully rotated cube with same parameters as input
    #                     'status' -> 'ok' indicating successful instantiation and rotation
    #             abnormal:
    #                 result -> dictionary with the following entry
    #                     'status' -> starts with 'error: ' indicating what went wrong during instantiation
    #                                 or rotation: first error that occurs is displayed
    #             side-effects:
    #                 none
    #
    #    NOTE: because cube validates and boundary tests 'cube' and 'dir', boundary testing will not be done
    #          here, and the primary focus of this test is the format of the output
    #
    #             happy path:
    #                 test 001: successfully rotated cube
    #             sad path:
    #                 test 901: invalid cube only
    #                 test 902: invalid rotation only
    #                 test 903: invalid cube and rotation
    #                
    #             evil path:
    #                 none
    
    def test_rotateTest_rotate_001_SuccessfullyRotatedCube(self):
        testCube = 'ceedaafffdeefbbcbbaeefccfccbdefdefdaccbaebdaadddcfabba'
        testDir = 'FRBLU'
        parms = {}
        parms['cube'] = testCube
        parms['dir'] = testDir
        result = rotate(parms)
        expectedResult = {}
        expectedResult['cube'] = 'aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeeeeeefffffffff'
        expectedResult['status'] = 'ok'
        
        self.assertEqual(result, expectedResult)
    
    def test_rotateTest_rotate_901_InvalidCubeOnly(self):
        testCube = 'ceedaafffdeefbbcbbaeefccfccbdefdefdaccbaebdaadd'
        testDir = 'FRBLU'
        parms = {}
        parms['cube'] = testCube
        parms['dir'] = testDir
        result = rotate(parms)
        expectedResult = {}
        expectedResult['status'] = 'error: invalid length for cube [54]'
        
        self.assertEqual(result, expectedResult)
    
    def test_rotateTest_rotate_902_InvalidRotationOnly(self):
        pass
    
    def test_rotateTest_rotate_903_InvalidCubeAndRotation(self):
        pass