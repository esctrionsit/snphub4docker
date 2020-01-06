#!/usr/bin/python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys, os

#os.system(sys.argv[0])

#print sys.argv[0]
#print sys.argv[1]
#print sys.argv[-1]
DIR=os.path.dirname(sys.argv[0])
#print DIR

import subprocess

argv_len = len(sys.argv)

if ("-h" in sys.argv) or ("-H" in sys.argv) or ("--help" in sys.argv):
    print("Usage:          snphub list")
    print("Description:    to list all the containers created")
    print("")
else:
    if argv_len>1:
        print("Wrong parameter. Enter \"snphub list -h\" for help.")
    else:
        try:
            out_bytes = subprocess.check_output(['docker', 'ps', '-a'])
        except:
            print("")
            print("Seems an error occured.")
            print("Check weather Docker is correctly installed, and using root account or using \"sudo\" before the command?")
            print("")
            exit(1)
        #
        out_text = out_bytes.decode('utf-8')
        out_lines = out_text.split('\n')
        snphub_indexs = []
        for i in range(1, len(out_lines)):
            if len(out_lines[i].split())>1 and out_lines[i].split()[1] == "snphub_image":
                snphub_indexs.append(i)
            #
        #
        print(out_lines[0])
        for i in snphub_indexs:
            print(out_lines[i])
        print("")
    #
#
