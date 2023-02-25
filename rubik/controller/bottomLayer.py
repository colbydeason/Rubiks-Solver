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
    for topCorners in range(4):
        if _checkRightCornerColor(corneredCube, 'top'):
            corneredCube.rotateCubeR()
        else:
            for bottomCorners in range(4):
                if _checkRightCornerColor(corneredCube, 'bottom'):
                    corneredCube.rotate('URur')
                    print(corneredCube.get() + ',')
                    corneredCube.rotateCubeR()
                    break
                else:
                    corneredCube.rotate('u')
                    print(corneredCube.get() + ',')
                    corneredCube.rotateCubeR()
                    
    corneredCube.resetCubeOrientation()
                
    
def _bringCornerDown(bcdCube):
    return ''
    
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
    
