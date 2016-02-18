from djinn import *
from voxinn.heightmap.HeightmapMatrix import *
from voxinn.heightmap.Dimensions import *
class TerrainGenerator:
    def __init__(self, hml):
        self.heightmapList = hml
        
    def generate(self):
        blockList = []
        height = 0
        x,z = getDimensions(self.heightmapList)
        for zaxis in range(z):
            for xaxis in range(x):
                for height in range(self.heightmapList[zaxis][xaxis]+1):
                    blockList.append(Box2(1,1,1,xaxis,height,zaxis,0,'brick.bmp'))      
        return blockList
    
    def render(self,blocklist):
        for block in blocklist:
            block.build() 
