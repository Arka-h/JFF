#!/usr/bin/python3.7
import sys
class style:				#class of escape sequences  for adding color
    violet    = '\033[95m'
    blue      = '\033[94m'
    green     = '\033[92m'
    yellow    = '\033[93m'
    red       = '\033[91m'
    end       = '\033[0m'	#just one is requied to cease effect of n number of colors before it...
    bold      = '\033[1m'
    underline = '\033[4m'
    anchor    = '\x1b]8;;'  #html anchor
    _a_       = '\a'
if (len(sys.argv)>1):
    sys.stdout.write(f"{style.bold}{style.green}\n {style.underline}{style.anchor}https://arka-h.github.io/JFF/ascii_face.html{style._a_}WELCOME ")
    for i in range(1,len(sys.argv)): sys.stdout.write( f'{style.blue} {sys.argv[i].upper()}{style.end}{style.anchor}{style._a_}\n' )
elif (len(sys.argv)==1):
    sys.stderr.write("\nUsage: {0} <arg1> <arg2> ...\n".format(sys.argv[0]))
print("")
