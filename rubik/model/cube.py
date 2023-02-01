from rubik.model.constants import *

class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self, encodedCube):
        self._cube = encodedCube
        self._cubeList = list(self._cube)
        
    def rotate(self, directions = 'F'):
        for rotation in directions:
            match rotation:
                case 'F':
                    self._rotateF()
                case 'f':
                    self._rotatef()
                case 'B':
                    self._rotateB()
                case 'b':
                    self._rotateb()
                case 'L':
                    self._rotateL()
                case 'l':
                    self._rotatel()
                case 'R':
                    self._rotateR()
                case 'r':
                    self._rotater()
                case 'U':
                    self._rotateU()
                case 'u':
                    self._rotateu()
                case other:
                    self._rotateF()
        
        #returns list into cube
        self._cube = "".join(self._cubeList)
        return self._cube
        pass
    
    def get(self):
        return self._cube

    # Individual rotation private methods
    def _rotateF(self):
        rotatedCubeList = self._cubeList[:]
        # Rotate front panels
        rotatedCubeList[2] = self._cubeList[0]
        rotatedCubeList[5] = self._cubeList[1]
        rotatedCubeList[8] = self._cubeList[2]
        rotatedCubeList[1] = self._cubeList[3]
        rotatedCubeList[4] = self._cubeList[4]
        rotatedCubeList[7] = self._cubeList[5]
        rotatedCubeList[0] = self._cubeList[6]
        rotatedCubeList[3] = self._cubeList[7]
        rotatedCubeList[6] = self._cubeList[8]
        # Rotate top panels CW
        rotatedCubeList[9] = self._cubeList[42]
        rotatedCubeList[12] = self._cubeList[43]
        rotatedCubeList[15] = self._cubeList[44]
        # Rotate right panels CW
        rotatedCubeList[47] = self._cubeList[9]
        rotatedCubeList[46] = self._cubeList[12]
        rotatedCubeList[45] = self._cubeList[15]
        # Rotate bottom panels CW
        rotatedCubeList[29] = self._cubeList[45]
        rotatedCubeList[32] = self._cubeList[46]
        rotatedCubeList[35] = self._cubeList[47]
        # Rotate left panels CW
        rotatedCubeList[44] = self._cubeList[29]
        rotatedCubeList[43] = self._cubeList[32]
        rotatedCubeList[42] = self._cubeList[35]
        # Modifies the cubeList
        self._cubeList = rotatedCubeList  
        
    def _rotatef(self):
        rotatedCubeList = self._cubeList[:]
        # Rotate front panels
        rotatedCubeList[6] = self._cubeList[0]
        rotatedCubeList[3] = self._cubeList[1]
        rotatedCubeList[0] = self._cubeList[2]
        rotatedCubeList[7] = self._cubeList[3]
        rotatedCubeList[4] = self._cubeList[4]
        rotatedCubeList[1] = self._cubeList[5]
        rotatedCubeList[8] = self._cubeList[6]
        rotatedCubeList[5] = self._cubeList[7]
        rotatedCubeList[2] = self._cubeList[8]
        # Rotate top panels CCW
        rotatedCubeList[35] = self._cubeList[42]
        rotatedCubeList[32] = self._cubeList[43]
        rotatedCubeList[29] = self._cubeList[44]
        # Rotate right panels CCW
        rotatedCubeList[42] = self._cubeList[9]
        rotatedCubeList[43] = self._cubeList[12]
        rotatedCubeList[44] = self._cubeList[15]
        # Rotate bottom panels CCW
        rotatedCubeList[15] = self._cubeList[45]
        rotatedCubeList[12] = self._cubeList[46]
        rotatedCubeList[9] = self._cubeList[47]
        # Rotate left panels CCW
        rotatedCubeList[45] = self._cubeList[29]
        rotatedCubeList[46] = self._cubeList[32]
        rotatedCubeList[47] = self._cubeList[35]
        # Modifies the cubeList
        self._cubeList = rotatedCubeList
    
    def _rotateB(self):
        rotatedCubeList = self._cubeList[:]
        # Rotate back panels
        rotatedCubeList[20] = self._cubeList[18]
        rotatedCubeList[23] = self._cubeList[19]
        rotatedCubeList[26] = self._cubeList[20]
        rotatedCubeList[19] = self._cubeList[21]
        rotatedCubeList[22] = self._cubeList[22]
        rotatedCubeList[25] = self._cubeList[23]
        rotatedCubeList[18] = self._cubeList[24]
        rotatedCubeList[21] = self._cubeList[25]
        rotatedCubeList[24] = self._cubeList[26]
        # Rotate top panels CW
        rotatedCubeList[33] = self._cubeList[36]
        rotatedCubeList[30] = self._cubeList[37]
        rotatedCubeList[27] = self._cubeList[38]
        # Rotate right panels CW
        rotatedCubeList[51] = self._cubeList[27]
        rotatedCubeList[52] = self._cubeList[30]
        rotatedCubeList[53] = self._cubeList[33]
        # Rotate bottom panels CW
        rotatedCubeList[17] = self._cubeList[51]
        rotatedCubeList[14] = self._cubeList[52]
        rotatedCubeList[11] = self._cubeList[53]
        # Rotate left panels CW
        rotatedCubeList[36] = self._cubeList[11]
        rotatedCubeList[37] = self._cubeList[14]
        rotatedCubeList[38] = self._cubeList[17]
        # Modifies the cubeList
        self._cubeList = rotatedCubeList
    
    def _rotateb(self):
        rotatedCubeList = self._cubeList[:]
        # Rotate back panels
        rotatedCubeList[24] = self._cubeList[18]
        rotatedCubeList[21] = self._cubeList[19]
        rotatedCubeList[18] = self._cubeList[20]
        rotatedCubeList[25] = self._cubeList[21]
        rotatedCubeList[22] = self._cubeList[22]
        rotatedCubeList[19] = self._cubeList[23]
        rotatedCubeList[26] = self._cubeList[24]
        rotatedCubeList[23] = self._cubeList[25]
        rotatedCubeList[20] = self._cubeList[26]
        # Rotate top panels CCW
        rotatedCubeList[11] = self._cubeList[36]
        rotatedCubeList[14] = self._cubeList[37]
        rotatedCubeList[17] = self._cubeList[38]
        # Rotate right panels CCW
        rotatedCubeList[38] = self._cubeList[27]
        rotatedCubeList[37] = self._cubeList[30]
        rotatedCubeList[36] = self._cubeList[33]
        # Rotate bottom panels CCW
        rotatedCubeList[27] = self._cubeList[51]
        rotatedCubeList[30] = self._cubeList[52]
        rotatedCubeList[33] = self._cubeList[53]
        # Rotate left panels CCW
        rotatedCubeList[53] = self._cubeList[11]
        rotatedCubeList[52] = self._cubeList[14]
        rotatedCubeList[51] = self._cubeList[17]
        # Modifies the cubeList
        self._cubeList = rotatedCubeList

    def _rotateL(self):
        rotatedCubeList = self._cubeList[:]
        # Rotate left panels
        rotatedCubeList[29] = self._cubeList[27]
        rotatedCubeList[32] = self._cubeList[28]
        rotatedCubeList[35] = self._cubeList[29]
        rotatedCubeList[28] = self._cubeList[30]
        rotatedCubeList[31] = self._cubeList[31]
        rotatedCubeList[34] = self._cubeList[32]
        rotatedCubeList[27] = self._cubeList[33]
        rotatedCubeList[30] = self._cubeList[34]
        rotatedCubeList[33] = self._cubeList[35]
        # Rotate top panels CW
        rotatedCubeList[0] = self._cubeList[36]
        rotatedCubeList[3] = self._cubeList[39]
        rotatedCubeList[6] = self._cubeList[42]
        # Rotate front panels CW
        rotatedCubeList[45] = self._cubeList[0]
        rotatedCubeList[48] = self._cubeList[3]
        rotatedCubeList[51] = self._cubeList[6]
        # Rotate bottom panels CW
        rotatedCubeList[26] = self._cubeList[45]
        rotatedCubeList[23] = self._cubeList[48]
        rotatedCubeList[20] = self._cubeList[51]
        # Rotate back panels CW
        rotatedCubeList[42] = self._cubeList[20]
        rotatedCubeList[39] = self._cubeList[23]
        rotatedCubeList[36] = self._cubeList[26]
        # Modifies the cubeList
        self._cubeList = rotatedCubeList

    def _rotatel(self):
        rotatedCubeList = self._cubeList[:]
        # Rotate left panels
        rotatedCubeList[33] = self._cubeList[27]
        rotatedCubeList[30] = self._cubeList[28]
        rotatedCubeList[27] = self._cubeList[29]
        rotatedCubeList[34] = self._cubeList[30]
        rotatedCubeList[31] = self._cubeList[31]
        rotatedCubeList[28] = self._cubeList[32]
        rotatedCubeList[35] = self._cubeList[33]
        rotatedCubeList[32] = self._cubeList[34]
        rotatedCubeList[29] = self._cubeList[35]
        # Rotate top panels CCW
        rotatedCubeList[26] = self._cubeList[36]
        rotatedCubeList[23] = self._cubeList[39]
        rotatedCubeList[20] = self._cubeList[42]
        # Rotate front panels CCW
        rotatedCubeList[36] = self._cubeList[0]
        rotatedCubeList[39] = self._cubeList[3]
        rotatedCubeList[42] = self._cubeList[6]
        # Rotate bottom panels CCW
        rotatedCubeList[0] = self._cubeList[45]
        rotatedCubeList[3] = self._cubeList[48]
        rotatedCubeList[6] = self._cubeList[51]
        # Rotate back panels CCW
        rotatedCubeList[51] = self._cubeList[20]
        rotatedCubeList[48] = self._cubeList[23]
        rotatedCubeList[45] = self._cubeList[26]
        # Modifies the cubeList
        self._cubeList = rotatedCubeList

    def _rotateR(self):
        rotatedCubeList = self._cubeList[:]
        # Rotate right panels
        rotatedCubeList[11] = self._cubeList[9]
        rotatedCubeList[14] = self._cubeList[10]
        rotatedCubeList[17] = self._cubeList[11]
        rotatedCubeList[10] = self._cubeList[12]
        rotatedCubeList[13] = self._cubeList[13]
        rotatedCubeList[16] = self._cubeList[14]
        rotatedCubeList[9] = self._cubeList[15]
        rotatedCubeList[12] = self._cubeList[16]
        rotatedCubeList[15] = self._cubeList[17]
        # Rotate top panels CW
        rotatedCubeList[18] = self._cubeList[44]
        rotatedCubeList[21] = self._cubeList[41]
        rotatedCubeList[24] = self._cubeList[38]
        # Rotate right panels CW
        rotatedCubeList[53] = self._cubeList[18]
        rotatedCubeList[50] = self._cubeList[21]
        rotatedCubeList[47] = self._cubeList[24]
        # Rotate bottom panels CW
        rotatedCubeList[2] = self._cubeList[47]
        rotatedCubeList[5] = self._cubeList[50]
        rotatedCubeList[8] = self._cubeList[53]
        # Rotate front panels CW
        rotatedCubeList[38] = self._cubeList[2]
        rotatedCubeList[41] = self._cubeList[5]
        rotatedCubeList[44] = self._cubeList[8]
        # Modifies the cubeList
        self._cubeList = rotatedCubeList

    def _rotater(self):
        rotatedCubeList = self._cubeList[:]
        # Rotate right panels
        rotatedCubeList[15] = self._cubeList[9]
        rotatedCubeList[12] = self._cubeList[10]
        rotatedCubeList[9] = self._cubeList[11]
        rotatedCubeList[16] = self._cubeList[12]
        rotatedCubeList[13] = self._cubeList[13]
        rotatedCubeList[10] = self._cubeList[14]
        rotatedCubeList[17] = self._cubeList[15]
        rotatedCubeList[14] = self._cubeList[16]
        rotatedCubeList[11] = self._cubeList[17]
        # Rotate top panels CCW
        rotatedCubeList[8] = self._cubeList[44]
        rotatedCubeList[5] = self._cubeList[41]
        rotatedCubeList[2] = self._cubeList[38]
        # Rotate right panels CCW
        rotatedCubeList[44] = self._cubeList[18]
        rotatedCubeList[41] = self._cubeList[21]
        rotatedCubeList[38] = self._cubeList[24]
        # Rotate bottom panels CCW
        rotatedCubeList[24] = self._cubeList[47]
        rotatedCubeList[21] = self._cubeList[50]
        rotatedCubeList[18] = self._cubeList[53]
        # Rotate front panels CCW
        rotatedCubeList[47] = self._cubeList[2]
        rotatedCubeList[50] = self._cubeList[5]
        rotatedCubeList[53] = self._cubeList[8]
        # Modifies the cubeList
        self._cubeList = rotatedCubeList

    def _rotateU(self):
        rotatedCubeList = self._cubeList[:]
        # Rotate top panels
        rotatedCubeList[38] = self._cubeList[36]
        rotatedCubeList[41] = self._cubeList[37]
        rotatedCubeList[44] = self._cubeList[38]
        rotatedCubeList[37] = self._cubeList[39]
        rotatedCubeList[40] = self._cubeList[40]
        rotatedCubeList[43] = self._cubeList[41]
        rotatedCubeList[36] = self._cubeList[42]
        rotatedCubeList[39] = self._cubeList[43]
        rotatedCubeList[42] = self._cubeList[44]
        # Rotate front panels CW
        rotatedCubeList[27] = self._cubeList[0]
        rotatedCubeList[28] = self._cubeList[1]
        rotatedCubeList[29] = self._cubeList[2]
        # Rotate right panels CW
        rotatedCubeList[0] = self._cubeList[9]
        rotatedCubeList[1] = self._cubeList[10]
        rotatedCubeList[2] = self._cubeList[11]
        # Rotate back panels CW
        rotatedCubeList[9] = self._cubeList[18]
        rotatedCubeList[10] = self._cubeList[19]
        rotatedCubeList[11] = self._cubeList[20]
        # Rotate left panels CW
        rotatedCubeList[18] = self._cubeList[27]
        rotatedCubeList[19] = self._cubeList[28]
        rotatedCubeList[20] = self._cubeList[29]
        # Modifies the cubeList
        self._cubeList = rotatedCubeList

    def _rotateu(self):
        rotatedCubeList = self._cubeList[:]
        # Rotate top panels
        rotatedCubeList[42] = self._cubeList[36]
        rotatedCubeList[39] = self._cubeList[37]
        rotatedCubeList[36] = self._cubeList[38]
        rotatedCubeList[43] = self._cubeList[39]
        rotatedCubeList[40] = self._cubeList[40]
        rotatedCubeList[37] = self._cubeList[41]
        rotatedCubeList[44] = self._cubeList[42]
        rotatedCubeList[41] = self._cubeList[43]
        rotatedCubeList[38] = self._cubeList[44]
        # Rotate front panels CCW
        rotatedCubeList[9] = self._cubeList[0]
        rotatedCubeList[10] = self._cubeList[1]
        rotatedCubeList[11] = self._cubeList[2]
        # Rotate right panels CCW
        rotatedCubeList[18] = self._cubeList[9]
        rotatedCubeList[19] = self._cubeList[10]
        rotatedCubeList[20] = self._cubeList[11]
        # Rotate back panels CCW
        rotatedCubeList[27] = self._cubeList[18]
        rotatedCubeList[28] = self._cubeList[19]
        rotatedCubeList[29] = self._cubeList[20]
        # Rotate left panels CCW
        rotatedCubeList[0] = self._cubeList[27]
        rotatedCubeList[1] = self._cubeList[28]
        rotatedCubeList[2] = self._cubeList[29]
        # Modifies the cubeList
        self._cubeList = rotatedCubeList