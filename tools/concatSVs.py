import os
import sys

def modTimestamps(origText, lastTimestamp):
  modText = ""
  end = -1
  for line in origText.split('\n'):
    parts = line.split()
    if len(parts)<3:
      continue
    start = float(parts[0])+lastTimestamp
    end = float(parts[1])+lastTimestamp
    word = parts[2]
    newline = str(start)+'\t'+str(end)+'\t'+word+'\n'
    modText+=newline

  return [modText, end]

def concatSVs(prefix, max, outfile):
  print "11"
  lastTimestamp = 0.
  
  nums = [str(n).zfill(2) for n in range(1, max+1)]
  files = [prefix+n+'.txt' for n in nums]
  print files
  
  finalText = ""
  
  for infile in files:
    fh = open(infile)
    text=fh.read()
    fh.close()
    [modText, lastTimestamp] = modTimestamps(text, lastTimestamp)
    print lastTimestamp
    finalText+=modText
    
  fh = open(outfile,'w')
  fh.write(finalText)
  fh.close()
  
  
def main():
  concatSVs(sys.argv[1], int(sys.argv[2]), sys.argv[3])
  
if __name__=="__main__":
  main()