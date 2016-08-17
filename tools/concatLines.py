import os
import sys

def concatLines(infile, outfile):
  outtext = ""
  currentLine = ""
  currentStart = None
  lastLine = ""
  
  for line in open(infile):
    parts = line.split()
    start=parts[0]
    end=parts[1]
    word=parts[2]
    if word=="PAU":
      if len(currentLine)>0:
        newLine = currentStart+'\t'+start+'\t'+currentLine+'\n'
        outtext+=newLine
      outtext+=line
      currentStart = None
      currentLine = ""
    else:
      if not currentStart:
        currentStart = start
      currentLine+=' '+word
      
  fh = open(outfile,'w')
  fh.write(outtext)
  fh.close()
  
  
if __name__=="__main__":
  concatLines(sys.argv[1],sys.argv[2])