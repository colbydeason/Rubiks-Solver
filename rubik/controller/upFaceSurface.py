from rubik.model.constants import *
from rubik.model.cube import Cube

def solveUpSurface(theCube: Cube) -> str:
    
    if theCube.upFaceSurfaceDone():
        return ''
    
    
    # while _alignCorner(theCube):
    #     theCube.rotate("RUrURUUr")
    for shape in range(4):
        if _alignCorner(theCube):
            theCube.rotate("RUrURUUr")
        else:
            break
    
    
    return theCube.popCurrentRotationStringResetOrientation()

def _alignCorner(cornerCube):
    cornerArray = [UTL, UTR, UBL, UBR]
    cornerColorArray = []
    topColor = cornerCube.getRelativeSquare(UMM)
    for corner in cornerArray:
        cornerColorArray.append(cornerCube.getRelativeSquare(corner))
    numberMatching = cornerColorArray.count(topColor)
    
    if numberMatching == 0 or numberMatching == 2:
        
        
        # while topColor != cornerCube.getRelativeSquare(LTR):
        #     cornerCube.rotateCubeR()
        for square in range(4):
            if topColor != cornerCube.getRelativeSquare(LTR):
                cornerCube.rotateCubeR()
            else:
                break
        
        
        return True
    elif numberMatching == 1:
        
        
        # while topColor != cornerCube.getRelativeSquare(UBL):
        #     cornerCube.rotateCubeR()
        for square in range(4):
            if topColor != cornerCube.getRelativeSquare(UBL):
                cornerCube.rotateCubeR()
            else:
                break
        
        
        return True
    else:
        return False