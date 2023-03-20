import rubik.model.constants
from rubik.model.cube import Cube

def solveMiddleLayer(theCube: Cube) -> str:
    
    # Solving Breakdown
    #
    # Step 1: Move edges out of middle layer
    #     find top edge that is yellow, move into place where edge is not yellow on middle layer
    # Step 2: Move edges into middle layer and solve
    #     go through each edge and come down
    
    _edgeOut(theCube)
    _bringDown(theCube)
    
    return theCube.popCurrentRotationStringResetOrientation()
    
    def _edgeOut(edgeCube):
        return ''
    
    def _bringDown(solveCube):
        return ''
    
    def _checkEdge(checkCube):
        return ''
    
    def _alignEdge(alignCube):
        topColor = alignCube.get()[40]