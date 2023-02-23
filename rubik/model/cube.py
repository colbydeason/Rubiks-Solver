from rubik.model.constants import *

class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self, encodedCube):
        self._cube = encodedCube
        self._isValidCube()
        self._cubeList = list(self._cube)
        # First index is current front facing face
        self._faceState = []
        self._faceState.append('F')
        self._faceState.append('R')
        self._faceState.append('B')
        self._faceState.append('L')
        self._currentRotationsString = ''
        
    def rotateCubeR(self):
        tempFace = self._faceState.pop(0)
        self._faceState.append(tempFace)
    
    def rotateCubeL(self):
        tempFace = self._faceState.pop(3)
        self._faceState.insert(0, tempFace)
        
    def resetCubeOrientation(self):
        self._faceState = []
        self._faceState.append('F')
        self._faceState.append('R')
        self._faceState.append('B')
        self._faceState.append('L')
        
    def rotate(self, directions = 'F'):
        if directions == None or len(directions) == 0:
            directions = 'F'
        for rotation in directions:
            match rotation:
                case 'F':
                    match self.getCurrentOrientation():
                        case 'F':
                            self._rotateF()
                        case 'R':
                            self._rotateR()
                        case 'B':
                            self._rotateB()
                        case 'L':
                            self._rotateL()
                case 'f':
                    match self.getCurrentOrientation():
                        case 'F':
                            self._rotatef()
                        case 'R':
                            self._rotater()
                        case 'B':
                            self._rotateb()
                        case 'L':
                            self._rotatel()
                case 'B':
                    match self.getCurrentOrientation():
                        case 'F':
                            self._rotateB()
                        case 'R':
                            self._rotateL()
                        case 'B':
                            self._rotateF()
                        case 'L':
                            self._rotateR()
                case 'b':
                    match self.getCurrentOrientation():
                        case 'F':
                            self._rotateb()
                        case 'R':
                            self._rotatel()
                        case 'B':
                            self._rotatef()
                        case 'L':
                            self._rotater()
                case 'L':
                    match self.getCurrentOrientation():
                        case 'F':
                            self._rotateL()
                        case 'R':
                            self._rotateF()
                        case 'B':
                            self._rotateR()
                        case 'L':
                            self._rotateB()
                case 'l':
                    match self.getCurrentOrientation():
                        case 'F':
                            self._rotatel()
                        case 'R':
                            self._rotatef()
                        case 'B':
                            self._rotater()
                        case 'L':
                            self._rotateb()
                case 'R':
                    match self.getCurrentOrientation():
                        case 'F':
                            self._rotateR()
                        case 'R':
                            self._rotateB()
                        case 'B':
                            self._rotateL()
                        case 'L':
                            self._rotateF()
                case 'r':
                    match self.getCurrentOrientation():
                        case 'F':
                            self._rotater()
                        case 'R':
                            self._rotateb()
                        case 'B':
                            self._rotatel()
                        case 'L':
                            self._rotatef()
                case 'U':
                    self._rotateU()
                case 'u':
                    self._rotateu()
                case _:
                    self._cube = 'error: invalid direction'
                    return self._cube
        
        self._cube = "".join(self._cubeList)
        return self._cube
    
    def get(self):
        return self._cube

    def getCurrentOrientation(self):
        return self._faceState[0]
    
    def getCurrentRotationString(self):
        returnString = self._currentRotationsString
        return returnString
    
    def popCurrentRotationStringResetOrientation(self):
        returnString = self._currentRotationsString
        self._currentRotationsString = ''
        self.resetCubeOrientation()
        return returnString
    
    def getRelativeSquare(self, square):
        if square < 0 or square > 53:
            raise Exception('square request is out of bounds')
        match self.getCurrentOrientation():
            case 'F':
                adjSquare = self._cube[square]
            case 'R':
                if FTL <= square <= BBR:
                    adjSquare = self._cube[square + 9]
                elif LTL <= square <= LBR:
                    adjSquare = self._cube[square - 27]
                else:
                    match square:
                        case 36:
                            adjSquare = self._cube[UBL]
                        case 37:
                            adjSquare = self._cube[UML]
                        case 38:
                            adjSquare = self._cube[UTL]
                        case 39:
                            adjSquare = self._cube[UBM]
                        case 40:
                            adjSquare = self._cube[UMM]
                        case 41:
                            adjSquare = self._cube[UTM]
                        case 42:
                            adjSquare = self._cube[UBR]
                        case 43:
                            adjSquare = self._cube[UMR]
                        case 44:
                            adjSquare = self._cube[UTR]
                        case 45:
                            adjSquare = self._cube[DTR]
                        case 46:
                            adjSquare = self._cube[DMR]
                        case 47:
                            adjSquare = self._cube[DBR]
                        case 48:
                            adjSquare = self._cube[DTM]
                        case 49:
                            adjSquare = self._cube[DMM]
                        case 50:
                            adjSquare = self._cube[DBM]
                        case 51:
                            adjSquare = self._cube[DTL]
                        case 52:
                            adjSquare = self._cube[DML]
                        case 53:
                            adjSquare = self._cube[DBL]
            case 'B':
                if FTL <= square <= RBR:
                    adjSquare = self._cube[square + 18]
                elif BTL <= square <= LBR:
                    adjSquare = self._cube[square - 18]
                else:
                    match square:
                        case 36:
                            adjSquare = self._cube[UBR]
                        case 37:
                            adjSquare = self._cube[UBM]
                        case 38:
                            adjSquare = self._cube[UBL]
                        case 39:
                            adjSquare = self._cube[UMR]
                        case 40:
                            adjSquare = self._cube[UMM]
                        case 41:
                            adjSquare = self._cube[UML]
                        case 42:
                            adjSquare = self._cube[UTR]
                        case 43:
                            adjSquare = self._cube[UTM]
                        case 44:
                            adjSquare = self._cube[UTL]
                        case 45:
                            adjSquare = self._cube[DBR]
                        case 46:
                            adjSquare = self._cube[DBM]
                        case 47:
                            adjSquare = self._cube[DBL]
                        case 48:
                            adjSquare = self._cube[DMR]
                        case 49:
                            adjSquare = self._cube[DMM]
                        case 50:
                            adjSquare = self._cube[DML]
                        case 51:
                            adjSquare = self._cube[DTR]
                        case 52:
                            adjSquare = self._cube[DTM]
                        case 53:
                            adjSquare = self._cube[DTL]
            case 'L':
                if FTL <= square <= FBR:
                    adjSquare = self._cube[square + 27]
                elif RTL <= square <= LBR:
                    adjSquare = self._cube[square - 9]
                else:
                    match square:
                        case 36:
                            adjSquare = self._cube[UTR]
                        case 37:
                            adjSquare = self._cube[UMR]
                        case 38:
                            adjSquare = self._cube[UBR]
                        case 39:
                            adjSquare = self._cube[UTM]
                        case 40:
                            adjSquare = self._cube[UMM]
                        case 41:
                            adjSquare = self._cube[UBM]
                        case 42:
                            adjSquare = self._cube[UTL]
                        case 43:
                            adjSquare = self._cube[UML]
                        case 44:
                            adjSquare = self._cube[UBL]
                        case 45:
                            adjSquare = self._cube[DBL]
                        case 46:
                            adjSquare = self._cube[DML]
                        case 47:
                            adjSquare = self._cube[DTL]
                        case 48:
                            adjSquare = self._cube[DBM]
                        case 49:
                            adjSquare = self._cube[DMM]
                        case 50:
                            adjSquare = self._cube[DTM]
                        case 51:
                            adjSquare = self._cube[DBR]
                        case 52:
                            adjSquare = self._cube[DMR]
                        case 53:
                            adjSquare = self._cube[DTR]
        return adjSquare

    def _isValidCube(self):
        if not self._cubeIsString():
            return
        if not self._isValidLength():
            return
        if not self._isValidFaces():
            return
        if not self._isUniquelyCentered():
            return
        
    def _cubeIsString(self):
        if isinstance(self._cube, str):
            return True
        else:
            self._cube = 'error: missing cube [string]'
            return False
        
    def _isValidLength(self):
        if len(self._cube) == 54:
            return True
        else:
            self._cube = 'error: invalid length for cube [54]'
            return False   
        
    def _isValidFaces(self):
        uniqueArray = []
        for i in range(len(self._cube)):
            newChar = self._cube[i]
            if not self._isValidCharacter(newChar):
                self._cube = 'error: invalid character for cube [a-zA-Z0-9]'
                return False
            if len(uniqueArray) == 0:
                uniqueArray.append([self._cube[i], "1"])
            else:
                for j in range(len(uniqueArray)):
                    if self._cube[i] == uniqueArray[j][0]:
                        uniqueArray[j][1] = uniqueArray[j][1] +"1"
                        break
                    elif j == len(uniqueArray) - 1:
                        uniqueArray.append([self._cube[i], "1"])    
        if not (len(uniqueArray) == 6):
            self._cube = 'error: incorrect number of unique colors [6, 9 of each]'
        for i in uniqueArray:
            if i[1] != '111111111':
                self._cube = 'error: incorrect number of unique colors [6, 9 of each]'
                return False
        return True
    
    def _isValidCharacter(self, char):
        if char.isalpha():
            return True
        elif char.isnumeric():
            return True
        else:
            return False    
        
    def _isUniquelyCentered(self):
        uniqList = [self._cube[4], self._cube[13], self._cube[22], self._cube[31], self._cube[40], self._cube[49]]
        if (len(set(uniqList)) == len(uniqList)):
            return True
        else:
            self._cube = 'error: centers are not unique'
            return False
        
    # Individual rotation private methods
    def _rotateF(self):
        rotatedCubeList = self._cubeList[:]
        # Rotate front panels
        rotatedCubeList[FTR] = self._cubeList[FTL]
        rotatedCubeList[FMR] = self._cubeList[FTM]
        rotatedCubeList[FBR] = self._cubeList[FTR]
        rotatedCubeList[FTM] = self._cubeList[FML]
        rotatedCubeList[FMM] = self._cubeList[FMM]
        rotatedCubeList[FBM] = self._cubeList[FMR]
        rotatedCubeList[FTL] = self._cubeList[FBL]
        rotatedCubeList[FML] = self._cubeList[FBM]
        rotatedCubeList[FBL] = self._cubeList[FBR]
        # Rotate top panels CW
        rotatedCubeList[RTL] = self._cubeList[UBL]
        rotatedCubeList[RML] = self._cubeList[UBM]
        rotatedCubeList[RBL] = self._cubeList[UBR]
        # Rotate right panels CW
        rotatedCubeList[DTR] = self._cubeList[RTL]
        rotatedCubeList[DTM] = self._cubeList[RML]
        rotatedCubeList[DTL] = self._cubeList[RBL]
        # Rotate bottom panels CW
        rotatedCubeList[LTR] = self._cubeList[DTL]
        rotatedCubeList[LMR] = self._cubeList[DTM]
        rotatedCubeList[LBR] = self._cubeList[DTR]
        # Rotate left panels CW
        rotatedCubeList[UBR] = self._cubeList[LTR]
        rotatedCubeList[UBM] = self._cubeList[LMR]
        rotatedCubeList[UBL] = self._cubeList[LBR]
        # Modifies the cubeList and turn list
        self._currentRotationsString += 'F'
        self._cubeList = rotatedCubeList  
        
    def _rotatef(self):
        rotatedCubeList = self._cubeList[:]
        # Rotate front panels
        rotatedCubeList[FBL] = self._cubeList[FTL]
        rotatedCubeList[FML] = self._cubeList[FTM]
        rotatedCubeList[FTL] = self._cubeList[FTR]
        rotatedCubeList[FBM] = self._cubeList[FML]
        rotatedCubeList[FMM] = self._cubeList[FMM]
        rotatedCubeList[FTM] = self._cubeList[FMR]
        rotatedCubeList[FBR] = self._cubeList[FBL]
        rotatedCubeList[FMR] = self._cubeList[FBM]
        rotatedCubeList[FTR] = self._cubeList[FBR]
        # Rotate top panels CCW
        rotatedCubeList[LBR] = self._cubeList[UBL]
        rotatedCubeList[LMR] = self._cubeList[UBM]
        rotatedCubeList[LTR] = self._cubeList[UBR]
        # Rotate right panels CCW
        rotatedCubeList[UBL] = self._cubeList[RTL]
        rotatedCubeList[UBM] = self._cubeList[RML]
        rotatedCubeList[UBR] = self._cubeList[RBL]
        # Rotate bottom panels CCW
        rotatedCubeList[RBL] = self._cubeList[DTL]
        rotatedCubeList[RML] = self._cubeList[DTM]
        rotatedCubeList[RTL] = self._cubeList[DTR]
        # Rotate left panels CCW
        rotatedCubeList[DTL] = self._cubeList[LTR]
        rotatedCubeList[DTM] = self._cubeList[LMR]
        rotatedCubeList[DTR] = self._cubeList[LBR]
        # Modifies the cubeList
        self._currentRotationsString += 'f'
        self._cubeList = rotatedCubeList
    
    def _rotateB(self):
        rotatedCubeList = self._cubeList[:]
        # Rotate back panels
        rotatedCubeList[BTR] = self._cubeList[BTL]
        rotatedCubeList[BMR] = self._cubeList[BTM]
        rotatedCubeList[BBR] = self._cubeList[BTR]
        rotatedCubeList[BTM] = self._cubeList[BML]
        rotatedCubeList[BMM] = self._cubeList[BMM]
        rotatedCubeList[BBM] = self._cubeList[BMR]
        rotatedCubeList[BTL] = self._cubeList[BBL]
        rotatedCubeList[BML] = self._cubeList[BBM]
        rotatedCubeList[BBL] = self._cubeList[BBR]
        # Rotate top panels CW
        rotatedCubeList[LBL] = self._cubeList[UTL]
        rotatedCubeList[LML] = self._cubeList[UTM]
        rotatedCubeList[LTL] = self._cubeList[UTR]
        # Rotate right panels CW
        rotatedCubeList[DBL] = self._cubeList[LTL]
        rotatedCubeList[DBM] = self._cubeList[LML]
        rotatedCubeList[DBR] = self._cubeList[LBL]
        # Rotate bottom panels CW
        rotatedCubeList[RBR] = self._cubeList[DBL]
        rotatedCubeList[RMR] = self._cubeList[DBM]
        rotatedCubeList[RTR] = self._cubeList[DBR]
        # Rotate left panels CW
        rotatedCubeList[UTL] = self._cubeList[RTR]
        rotatedCubeList[UTM] = self._cubeList[RMR]
        rotatedCubeList[UTR] = self._cubeList[RBR]
        # Modifies the cubeList
        self._currentRotationsString += 'B'
        self._cubeList = rotatedCubeList
    
    def _rotateb(self):
        rotatedCubeList = self._cubeList[:]
        # Rotate back panels
        rotatedCubeList[BBL] = self._cubeList[BTL]
        rotatedCubeList[BML] = self._cubeList[BTM]
        rotatedCubeList[BTL] = self._cubeList[BTR]
        rotatedCubeList[BBM] = self._cubeList[BML]
        rotatedCubeList[BMM] = self._cubeList[BMM]
        rotatedCubeList[BTM] = self._cubeList[BMR]
        rotatedCubeList[BBR] = self._cubeList[BBL]
        rotatedCubeList[BMR] = self._cubeList[BBM]
        rotatedCubeList[BTR] = self._cubeList[BBR]
        # Rotate top panels CCW
        rotatedCubeList[RTR] = self._cubeList[UTL]
        rotatedCubeList[RMR] = self._cubeList[UTM]
        rotatedCubeList[RBR] = self._cubeList[UTR]
        # Rotate right panels CCW
        rotatedCubeList[UTR] = self._cubeList[LTL]
        rotatedCubeList[UTM] = self._cubeList[LML]
        rotatedCubeList[UTL] = self._cubeList[LBL]
        # Rotate bottom panels CCW
        rotatedCubeList[LTL] = self._cubeList[DBL]
        rotatedCubeList[LML] = self._cubeList[DBM]
        rotatedCubeList[LBL] = self._cubeList[DBR]
        # Rotate left panels CCW
        rotatedCubeList[DBR] = self._cubeList[RTR]
        rotatedCubeList[DBM] = self._cubeList[RMR]
        rotatedCubeList[DBL] = self._cubeList[RBR]
        # Modifies the cubeList
        self._currentRotationsString += 'b'
        self._cubeList = rotatedCubeList

    def _rotateL(self):
        rotatedCubeList = self._cubeList[:]
        # Rotate left panels
        rotatedCubeList[LTR] = self._cubeList[LTL]
        rotatedCubeList[LMR] = self._cubeList[LTM]
        rotatedCubeList[LBR] = self._cubeList[LTR]
        rotatedCubeList[LTM] = self._cubeList[LML]
        rotatedCubeList[LMM] = self._cubeList[LMM]
        rotatedCubeList[LBM] = self._cubeList[LMR]
        rotatedCubeList[LTL] = self._cubeList[LBL]
        rotatedCubeList[LML] = self._cubeList[LBM]
        rotatedCubeList[LBL] = self._cubeList[LBR]
        # Rotate top panels CW
        rotatedCubeList[FTL] = self._cubeList[UTL]
        rotatedCubeList[FML] = self._cubeList[UML]
        rotatedCubeList[FBL] = self._cubeList[UBL]
        # Rotate front panels CW
        rotatedCubeList[DTL] = self._cubeList[FTL]
        rotatedCubeList[DML] = self._cubeList[FML]
        rotatedCubeList[DBL] = self._cubeList[FBL]
        # Rotate bottom panels CW
        rotatedCubeList[BBR] = self._cubeList[DTL]
        rotatedCubeList[BMR] = self._cubeList[DML]
        rotatedCubeList[BTR] = self._cubeList[DBL]
        # Rotate back panels CW
        rotatedCubeList[UBL] = self._cubeList[BTR]
        rotatedCubeList[UML] = self._cubeList[BMR]
        rotatedCubeList[UTL] = self._cubeList[BBR]
        # Modifies the cubeList
        self._currentRotationsString += 'L'
        self._cubeList = rotatedCubeList

    def _rotatel(self):
        rotatedCubeList = self._cubeList[:]
        # Rotate left panels
        rotatedCubeList[LBL] = self._cubeList[LTL]
        rotatedCubeList[LML] = self._cubeList[LTM]
        rotatedCubeList[LTL] = self._cubeList[LTR]
        rotatedCubeList[LBM] = self._cubeList[LML]
        rotatedCubeList[LMM] = self._cubeList[LMM]
        rotatedCubeList[LTM] = self._cubeList[LMR]
        rotatedCubeList[LBR] = self._cubeList[LBL]
        rotatedCubeList[LMR] = self._cubeList[LBM]
        rotatedCubeList[LTR] = self._cubeList[LBR]
        # Rotate top panels CCW
        rotatedCubeList[BBR] = self._cubeList[UTL]
        rotatedCubeList[BMR] = self._cubeList[UML]
        rotatedCubeList[BTR] = self._cubeList[UBL]
        # Rotate front panels CCW
        rotatedCubeList[UTL] = self._cubeList[FTL]
        rotatedCubeList[UML] = self._cubeList[FML]
        rotatedCubeList[UBL] = self._cubeList[FBL]
        # Rotate bottom panels CCW
        rotatedCubeList[FTL] = self._cubeList[DTL]
        rotatedCubeList[FML] = self._cubeList[DML]
        rotatedCubeList[FBL] = self._cubeList[DBL]
        # Rotate back panels CCW
        rotatedCubeList[DBL] = self._cubeList[BTR]
        rotatedCubeList[DML] = self._cubeList[BMR]
        rotatedCubeList[DTL] = self._cubeList[BBR]
        # Modifies the cubeList
        self._currentRotationsString += 'l'
        self._cubeList = rotatedCubeList

    def _rotateR(self):
        rotatedCubeList = self._cubeList[:]
        # Rotate right panels
        rotatedCubeList[RTR] = self._cubeList[RTL]
        rotatedCubeList[RMR] = self._cubeList[RTM]
        rotatedCubeList[RBR] = self._cubeList[RTR]
        rotatedCubeList[RTM] = self._cubeList[RML]
        rotatedCubeList[RMM] = self._cubeList[RMM]
        rotatedCubeList[RBM] = self._cubeList[RMR]
        rotatedCubeList[RTL] = self._cubeList[RBL]
        rotatedCubeList[RML] = self._cubeList[RBM]
        rotatedCubeList[RBL] = self._cubeList[RBR]
        # Rotate top panels CW
        rotatedCubeList[BTL] = self._cubeList[UBR]
        rotatedCubeList[BML] = self._cubeList[UMR]
        rotatedCubeList[BBL] = self._cubeList[UTR]
        # Rotate right panels CW
        rotatedCubeList[DBR] = self._cubeList[BTL]
        rotatedCubeList[DMR] = self._cubeList[BML]
        rotatedCubeList[DTR] = self._cubeList[BBL]
        # Rotate bottom panels CW
        rotatedCubeList[FTR] = self._cubeList[DTR]
        rotatedCubeList[FMR] = self._cubeList[DMR]
        rotatedCubeList[FBR] = self._cubeList[DBR]
        # Rotate front panels CW
        rotatedCubeList[UTR] = self._cubeList[FTR]
        rotatedCubeList[UMR] = self._cubeList[FMR]
        rotatedCubeList[UBR] = self._cubeList[FBR]
        # Modifies the cubeList
        self._currentRotationsString += 'R'
        self._cubeList = rotatedCubeList

    def _rotater(self):
        rotatedCubeList = self._cubeList[:]
        # Rotate right panels
        rotatedCubeList[RBL] = self._cubeList[RTL]
        rotatedCubeList[RML] = self._cubeList[RTM]
        rotatedCubeList[RTL] = self._cubeList[RTR]
        rotatedCubeList[RBM] = self._cubeList[RML]
        rotatedCubeList[RMM] = self._cubeList[RMM]
        rotatedCubeList[RTM] = self._cubeList[RMR]
        rotatedCubeList[RBR] = self._cubeList[RBL]
        rotatedCubeList[RMR] = self._cubeList[RBM]
        rotatedCubeList[RTR] = self._cubeList[RBR]
        # Rotate top panels CCW
        rotatedCubeList[FBR] = self._cubeList[UBR]
        rotatedCubeList[FMR] = self._cubeList[UMR]
        rotatedCubeList[FTR] = self._cubeList[UTR]
        # Rotate right panels CCW
        rotatedCubeList[UBR] = self._cubeList[BTL]
        rotatedCubeList[UMR] = self._cubeList[BML]
        rotatedCubeList[UTR] = self._cubeList[BBL]
        # Rotate bottom panels CCW
        rotatedCubeList[BBL] = self._cubeList[DTR]
        rotatedCubeList[BML] = self._cubeList[DMR]
        rotatedCubeList[BTL] = self._cubeList[DBR]
        # Rotate front panels CCW
        rotatedCubeList[DTR] = self._cubeList[FTR]
        rotatedCubeList[DMR] = self._cubeList[FMR]
        rotatedCubeList[DBR] = self._cubeList[FBR]
        # Modifies the cubeList
        self._currentRotationsString += 'r'
        self._cubeList = rotatedCubeList

    def _rotateU(self):
        rotatedCubeList = self._cubeList[:]
        # Rotate top panels
        rotatedCubeList[UTR] = self._cubeList[UTL]
        rotatedCubeList[UMR] = self._cubeList[UTM]
        rotatedCubeList[UBR] = self._cubeList[UTR]
        rotatedCubeList[UTM] = self._cubeList[UML]
        rotatedCubeList[UMM] = self._cubeList[UMM]
        rotatedCubeList[UBM] = self._cubeList[UMR]
        rotatedCubeList[UTL] = self._cubeList[UBL]
        rotatedCubeList[UML] = self._cubeList[UBM]
        rotatedCubeList[UBL] = self._cubeList[UBR]
        # Rotate front panels CW
        rotatedCubeList[LTL] = self._cubeList[FTL]
        rotatedCubeList[LTM] = self._cubeList[FTM]
        rotatedCubeList[LTR] = self._cubeList[FTR]
        # Rotate right panels CW
        rotatedCubeList[FTL] = self._cubeList[RTL]
        rotatedCubeList[FTM] = self._cubeList[RTM]
        rotatedCubeList[FTR] = self._cubeList[RTR]
        # Rotate back panels CW
        rotatedCubeList[RTL] = self._cubeList[BTL]
        rotatedCubeList[RTM] = self._cubeList[BTM]
        rotatedCubeList[RTR] = self._cubeList[BTR]
        # Rotate left panels CW
        rotatedCubeList[BTL] = self._cubeList[LTL]
        rotatedCubeList[BTM] = self._cubeList[LTM]
        rotatedCubeList[BTR] = self._cubeList[LTR]
        # Modifies the cubeList
        self._currentRotationsString += 'U'
        self._cubeList = rotatedCubeList

    def _rotateu(self):
        rotatedCubeList = self._cubeList[:]
        # Rotate top panels
        rotatedCubeList[UBL] = self._cubeList[UTL]
        rotatedCubeList[UML] = self._cubeList[UTM]
        rotatedCubeList[UTL] = self._cubeList[UTR]
        rotatedCubeList[UBM] = self._cubeList[UML]
        rotatedCubeList[UMM] = self._cubeList[UMM]
        rotatedCubeList[UTM] = self._cubeList[UMR]
        rotatedCubeList[UBR] = self._cubeList[UBL]
        rotatedCubeList[UMR] = self._cubeList[UBM]
        rotatedCubeList[UTR] = self._cubeList[UBR]
        # Rotate front panels CCW
        rotatedCubeList[RTL] = self._cubeList[FTL]
        rotatedCubeList[RTM] = self._cubeList[FTM]
        rotatedCubeList[RTR] = self._cubeList[FTR]
        # Rotate right panels CCW
        rotatedCubeList[BTL] = self._cubeList[RTL]
        rotatedCubeList[BTM] = self._cubeList[RTM]
        rotatedCubeList[BTR] = self._cubeList[RTR]
        # Rotate back panels CCW
        rotatedCubeList[LTL] = self._cubeList[BTL]
        rotatedCubeList[LTM] = self._cubeList[BTM]
        rotatedCubeList[LTR] = self._cubeList[BTR]
        # Rotate left panels CCW
        rotatedCubeList[FTL] = self._cubeList[LTL]
        rotatedCubeList[FTM] = self._cubeList[LTM]
        rotatedCubeList[FTR] = self._cubeList[LTR]
        # Modifies the cubeList
        self._currentRotationsString += 'u'
        self._cubeList = rotatedCubeList