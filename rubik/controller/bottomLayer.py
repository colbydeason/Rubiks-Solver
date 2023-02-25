import rubik.model.constants
from rubik.model.cube import Cube

def solveBottomLayer(theCube: Cube) -> str:
    
    # Solving Breakdown
    #
    # Step 1: Move Corners to top
    #     a) check if any of the corners in the bottom of the cube have white in them, move them up
    # Step 2: Put corners into correct place
    #     b) move corners one by one into the correct place in the bottom of the cube
    
    _moveCornerOut(theCube)
    _bringCornerDown(theCube)
    
    return theCube.popCurrentRotationStringResetOrientation()     

def _moveCornerOut(corneredCube):
    for topCorners in range(8):
        if _checkRightCornerColor(corneredCube, 'top'):
            corneredCube.rotateCubeR()
        else:
            for bottomCorners in range(4):
                if _checkRightCornerColor(corneredCube, 'bottom'):
                    corneredCube.rotate('URur')
                    corneredCube.rotateCubeR()
                    break
                else:
                    corneredCube.rotate('u')
                    corneredCube.rotateCubeR()
                    
    corneredCube.resetCubeOrientation()
                
    
def _bringCornerDown(bcdCube):
    currCorner = [2, 44, 9]
    for corner in range(4):
        colorArray = _alignCorner(bcdCube)
        if colorArray[0] == bcdCube.getBottomColor():
            bcdCube.rotate('URur')
        elif colorArray[1] == bcdCube.getBottomColor():
            bcdCube.rotate('fuuFUfuF')
        elif colorArray[2] == bcdCube.getBottomColor():
            bcdCube.rotate('RUr')
        else:
            raise Exception('Corner is not a bottom face corner in _bringCornerDown')
        if corner != 4:
            while not _checkRightCornerColor(bcdCube, 'top'):
                bcdCube.rotateCubeR()
    
def _checkRightCornerColor(cCube, topOrBottom):
    cornerTop = [2, 44, 9]
    cornerBottom = [8, 15, 47]
    match topOrBottom:
        case 'top':
            colorArray = []
            for square in cornerTop:
                colorArray.append(cCube.getRelativeSquare(square))
            if colorArray.count(cCube.getBottomColor()) == 1:
                return True
            else:
                return False
        case 'bottom':  
            colorArray = []
            for square in cornerBottom:
                colorArray.append(cCube.getRelativeSquare(square))
            if colorArray.count(cCube.getBottomColor()) == 1:
                return True
            else:
                return False    
        case other:
            raise Exception("must be top or bottom for _checkRightCornerColor")

def _alignCorner(alCube):
    cornerArray = [2, 44, 9]
    middle1 = 4
    middle2 = 13
    middle1Color = alCube.getRelativeSquare(middle1)
    middle2Color = alCube.getRelativeSquare(middle2)
    colorArray = []
    for square in cornerArray:
        colorArray.append(alCube.getRelativeSquare(square))
    for tryMatch in range(4):
        if (colorArray.includes(middle1Color)) and (colorArray.includes(middle2Color)):
            return colorArray
        else:
            alCube.rotate('u')
            alCube.rotateCubeR()
    raise Exception('Corner not able to match centers in _alignCorner')
