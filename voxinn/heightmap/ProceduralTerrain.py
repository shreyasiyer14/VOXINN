import random
from djinn import *
import os
import sys

class ProceduralTerrain:
    
    def __init__(self, heightmapList):
        self.heightmapList = heightmapList

    def generateHill(self):
        randindex = random.randint(0,len(self.heightmapList[0])-1)
        makemap = random.randint(-5,1)

        ind, i, flag = 0, 0, 0
        count = 0
        num = 1
        while ind < len(self.heightmapList):
            if makemap>=0:
              i = ind
              flag = 1
              for j in range(9):  
                for index in range((9-count)/2):
                    self.heightmapList[i].append(0)
                for index in range(9 - 2 * ((9 - count)/2)):
                    self.heightmapList[i].append(num)
                    num += 1
                num -= 2
                while num > 0:
                    self.heightmapList[i].append(num)
                    num -= 1
                for index in range((9-count)/2):
                    self.heightmapList[i].append(0)
                count += 2
                num = 1
                i += 1
                index = 0
              for j in range(len(self.heightmapList)-9):
                  for x in range(9):
                      self.heightmapList[i].append(0)
                  
            if flag == 1:
               ind = i
                
            if flag == 0:
              for ind in range(len(self.heightmapList)):
                for k in range(9):
                    self.heightmapList[ind].append(0)
                    
            count = 0
            num = 1
            ind += 1
       
        heightmap = self.heightmapList
        return heightmap

    def generateStar(self):
        randindex = random.randint(0,len(self.heightmapList[0])-1)
        makemap = random.randint(0,1)
        objects = 0
        ind, i, flag = 0, 0, 0
        count = 0
        num = 1
        while ind < len(self.heightmapList):
            if makemap:
              i = ind
              flag = 1
              for j in range(9):  
                for index in range((9-count)/2):
                    self.heightmapList[i].append(0)
                    objects += 1
                for index in range(9 - 2 * ((9 - count)/2)):
                    self.heightmapList[i].append(num)
                    num += 1
                    objects += num
                num -= 2
                while num > 0:
                    self.heightmapList[i].append(num)
                    num -= 1
                    objects += num
                for index in range((9-count)/2):
                    self.heightmapList[i].append(0) 
                    objects += 1
                count += 2
                num = 1
                i += 1
                index = 0
              for j in range(len(self.heightmapList)-9):
                  for x in range(9):
                      self.heightmapList[i].append(0)
                      objects += 1
                  
            if flag == 1:
               ind = i
                
            if flag == 0:
              for ind in range(len(self.heightmapList)):
                for k in range(9):
                    objects += 1
                    self.heightmapList[ind].append(0)
                    
            count = 0
            num = 1
            ind += 1
        print "Procedural Objects: ", objects
        heightmap = self.heightmapList
        return heightmap
