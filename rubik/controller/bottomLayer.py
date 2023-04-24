from rubik.model.constants import *
from rubik.model.cube import Cube

def solveBottomLayer(theCube: Cube) -> str:
    
    # Solving Breakdown
    #
    # Step 1: Move Corners to top
    #     a) check if any of the corners in the bottom of the cube have white in them, move them up
    # Step 2: Put corners into correct place
    #     b) move corners one by one into the correct place in the bottom of the cube
    
    if theCube.bottomLayerDone():
        return ''
    _moveCornerOut(theCube)
    _bringCornerDown(theCube)
    
    if not theCube.bottomLayerDone():
        return 'error: unsolvable cube'
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
    for corner in range(4):
        colorList = _alignCorner(bcdCube)
        if colorList[0] == bcdCube.getBottomColor():
            bcdCube.rotate('URur')
        elif colorList[1] == bcdCube.getBottomColor():
            bcdCube.rotate('fuuFUfuF')
        elif colorList[2] == bcdCube.getBottomColor():
            bcdCube.rotate('RUr')
        if corner != 3:
            while not _checkRightCornerColor(bcdCube, 'top'):
                bcdCube.rotateCubeR()
    
def _checkRightCornerColor(cCube, topOrBottom):
    cornerTop = [FTR, UBR, RTL]
    cornerBottom = [FBR, RBL, DTR]
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
            return False

def _alignCorner(alCube):
    cornerArray = [FTR, UBR, RTL]
    middle1 = FMM
    middle2 = RMM
    colorList = []
    for square in cornerArray:
        colorList.append(alCube.getRelativeSquare(square))
    for tryMatch in range(4):
        middle1Color = alCube.getRelativeSquare(middle1)
        middle2Color = alCube.getRelativeSquare(middle2)
        if (middle1Color in colorList) and (middle2Color in colorList):
            return colorList
        else:
            alCube.rotate('u')
            alCube.rotateCubeR()
