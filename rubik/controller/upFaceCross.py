from rubik.model.constants import *
from rubik.model.cube import Cube

def solveUpCross(theCube: Cube) -> str:
    
    if theCube.upFaceCrossDone():
        return ''
    for shape in range(4):
        if _alignShape(theCube):
            theCube.rotate("FRUruf")
        else:
            break
    if not theCube.upFaceCrossDone():
        return 'error: unsolvable cube'
    return theCube.popCurrentRotationStringResetOrientation()

def _alignShape(shapeCube):
    topColor = shapeCube.getRelativeSquare(UMM)
    edgeArray = [UTM, UML, UMR, UBM]
    if shapeCube.checkForColor(edgeArray, UMM, notIn = True):
        return True
    if shapeCube.isSameColor(edgeArray):
        return False
    for edge in range(4):
        if shapeCube.getRelativeSquare(UBM) == topColor:
            shapeCube.rotateCubeR()
            continue
        else:
            if shapeCube.getRelativeSquare(UML) != topColor:
                shapeCube.rotateCubeL()
                return True
            else:
                return True