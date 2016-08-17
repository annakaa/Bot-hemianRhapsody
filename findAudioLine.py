import os
import sys
import random
from BRDict import BRDict
from RihannaDict import RihannaDict


def findAudioLineBR(inwords):
  availableLines = BRDict.keys()
  random.shuffle(availableLines)
  for al in availableLines:
    if BRDict[al].find(inwords)>-1:
      return [BRDict[al],al]
  return [None,None]
  
  
def findAudioLineRihanna(inwords):
  availableLines = RihannaDict.keys()
  random.shuffle(availableLines)
  for al in availableLines:
    if RihannaDict[al].find(inwords)>-1:
      return [RihannaDict[al],al]
  return [None,None]
  
def findAudioLine(inwords, RIHANNA):
  print inwords, RIHANNA
  if RIHANNA:
    return findAudioLineRihanna(inwords)
  else:
    return findAudioLineBR(inwords)