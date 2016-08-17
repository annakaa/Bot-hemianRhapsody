import os
import sys

FS=44100
OCT_CMD = 'octave --silent --eval  "splitAudioFile(\'INFILE\',\'OUTDIR\',FS,FROMS, TOS, INDEX); exit;"'

def chop(inwav, intxt, outdir):
  ctr = 0
  for line in open(intxt):
    parts = line.split()
    fromS = (parts[0])
    toS = (parts[1])
    cmd = OCT_CMD.replace('INFILE',inwav).replace('OUTDIR',outdir).replace('FS',str(FS)).replace('FROMS',fromS).replace('TOS',toS).replace('INDEX',str(ctr))
    os.system(cmd)
    
    
if __name__=="__main__":
  chop(sys.argv[1],sys.argv[2],sys.argv[3])