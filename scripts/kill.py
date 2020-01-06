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

if (argv_len == 1) or ("-h" in sys.argv) or ("-H" in sys.argv) or ("--help" in sys.argv):
    print("Usage:          snphub kill <CONTAINER ID>")
    print("Description:    kill (force stop) a specific container")
    print("")
else:
    if argv_len>2:
        print("Wrong parameter. Enter \"snphub kill -h\" for help.")
    else:
        container_id = str(sys.argv[1])
        try:
            out_bytes = subprocess.call(['docker', 'kill', container_id])
        except:
            print("")
            print("Seems an error occured.")
            print("Check weather Docker is correctly installed, and using root account or using \"sudo\" before the command?")
            print("Check weather the container id is correct? (use \"snphub list\" to see all containers)")
            print("")
            exit(1)
        #
        print("Finished")
        print("")
    #
#
