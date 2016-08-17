import sys
import os

INSUFFIX='.wav'
OUTSUFFIX='.mp3'

#FFMPEG_CMD = 'ffmpeg -y --disable-encoders -i "INPATH" -ar 16000 -ac 1 "OUTPATH"'
FFMPEG_CMD = 'ffmpeg -y -i "INPATH" -ar 44100 -ac 1 -ab 192k "OUTPATH"'


def recodeDir(inpath, outpath):
  for f in os.listdir(inpath):  
    infile = inpath+'/'+f
    outfile = outpath+'/'+f.replace(INSUFFIX, OUTSUFFIX)
    recodeFile(infile, outfile)

def recodeFile(infile, outfile):
  if not os.path.exists(outfile) and os.path.isfile(infile):
    cmd = FFMPEG_CMD.replace("INPATH",infile).replace("OUTPATH",outfile)
    print cmd
    os.system(cmd)
      
      
      

def main(argv):
  if len(argv)<1:
    return 1
  inputArg = argv[0]
  outputArg = argv[1]
  print inputArg, outputArg
  if os.path.isdir(inputArg):
    recodeDir(inputArg, outputArg)
  else:
    recodeFile(inputArg, outputArg)

if __name__ == "__main__":
  main(sys.argv[1:])


