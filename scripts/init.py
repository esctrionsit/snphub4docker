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

if argv_len == 1 or ("-h" in sys.argv) or ("-H" in sys.argv) or ("--help" in sys.argv):
    print("Usage:          snphub init -y")
    print("Description:    pre-processing the user provided re-seq data")
    print("Options:")
    print("     -y     sure to pre-processing user re-seq data")
    print("")
    print("Steps: ")
    print("  Step.1   Fulfill file \"setup_config.R\".")
    print("  Step.2   Make sure the current user has the reading/writing permission on \"path_datafolder\" in file \"setup_config.R\".")
    print("  Step.3   Run \"snphub init -y\".")
    print("")
else:
    if (argv_len > 2) or (sys.argv[1] != "-y"):
        print("Wrong parameter. Enter \"snphub init -h\" for help.")
    else:
        try:
            out_bytes = subprocess.call(['Rscript', DIR + '/setup.R'])
        except:
            print("")
            print("Seems an error occured.")
            print("Check weather R is correctly installed?")
            print("Check weather the current user has writing permission?")
            print("")
            exit(1)
        #
        print("")
        print("Finished")
        print("")
    #
#
