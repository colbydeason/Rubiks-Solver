import rubik.model.constants
from rubik.model.cube import Cube

def solveMiddleLayer(theCube: Cube) -> str:
    
    # Solving Breakdown
    #
    # Step 1: Move edges out of middle layer
    #     find top edge that is yellow, move into place where edge is not yellow on middle layer
    # Step 2: Move edges into middle layer and solve
    #     go through each edge and come down
    
    if theCube.middleLayerDone():
        return ''
    _edgeOut(theCube)
    _bringDown(theCube)
    
    return theCube.popCurrentRotationStringResetOrientation()
    
def _edgeOut(edgeCube):
    topColor = 40
    for i in range(4):
        if edgeCube.checkForColor([5, 12], topColor):
            edgeCube.rotateCubeR()
            continue
        else:
            for j in range(4):
                if edgeCube.checkForColor([28, 39], topColor):
                    edgeCube.rotate('RUrufuF')
                    edgeCube.rotateCubeR()
                    break
                else:
                    edgeCube.rotate('U')
    edgeCube.resetCubeOrientation()
            
def _bringDown(solveCube):
    topColor = 40
    for i in range(4):
        while solveCube.checkForColor([1, 43], topColor):
                solveCube.rotate('u')
        matchSide = _alignTopEdge(solveCube)
        match matchSide:
            case 'L':
                solveCube.rotate('ulULUFuf')
            case 'R':
                solveCube.rotate('URurufUF')
            
        
    
def _alignTopEdge(alignCube):
    while alignCube.getRelativeSquare(1) != alignCube.getRelativeSquare(4):
        alignCube.rotate('u')
        alignCube.rotateCubeR()
    if alignCube.getRelativeSquare(43) == alignCube.getRelativeSquare(31):
        matchSide = 'L'
    else:
        matchSide = 'R'
    return matchSide
            