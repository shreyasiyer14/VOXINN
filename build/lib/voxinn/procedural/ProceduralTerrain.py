import random
from djinn import *
import os
import sys

class ProceduralTerrain:
    
    def __init__(self, heightmapList):
        self.heightmapList = heightmapList

    def generateHill(self):
       count = 0
       num = 1
       randindex = random.randint(0,len(self.heightmapList)-1)
       while ind < len(self.heightmapList):
            if ind == randindex:
              i = ind
              for j in range(len(9)):  
                for index in range((9-count)/2):
                    self.heightmapList[i].append(0)
            
                for index in range(9 - 2 * ((9 - count)/2)):
                    self.heightmapList[i].append(num)
                    num += 1 
                num -= 1
                while num != 0:
                    self.heightmapList[i].append(num)
                    num -= 1
 
                for index in range((9-count)/2):
                    self.heightmapList[i].append(0)
                count -= 2
                num = 1
                i += 1
                flag = 1
            ind = i
            if flag == 0:
                for k in range(len(9)):
                    self.heightmapList[ind].append(0)
                    ind += 1
