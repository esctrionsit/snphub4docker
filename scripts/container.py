#!/usr/bin/python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys, os

import random

#os.system(sys.argv[0])

#print sys.argv[0]
#print sys.argv[1]
#print sys.argv[-1]
DIR=os.path.dirname(sys.argv[0])
#print DIR

import subprocess

argv_len = len(sys.argv)

if ("-h" in sys.argv) or ("-H" in sys.argv) or ("--help" in sys.argv):
    print("Usage:          snphub create container [options]")
    print("Description:    create a SnpHub docker container form SnpHub docker image")
    print("Options:")
    print("")
    print("     -p <host_port>     Port that published to host. Default using randomport")
    print("     -v <data_path>     Bind mount a volume of user re-seq data into container")
    print("                        (AFTER pre-processed with \"snphub init <path>\")")
    print("                        (absolute path is recommended)")
    print("")
else:
    fixed_port = False
    port = str(random.randint(40000,60000))
    mount = False
    mount_path = ""
    count = 1
    #
    if "-p" in sys.argv:
        p_index = (sys.argv).index("-p")
        if len(sys.argv) == p_index + 1 or str(sys.argv[p_index + 1]) in ['-p', '-v']:
            print("Wrong parameter. Enter \"snphub create container -h\" for help.")
            print("")
            exit(1)
        fixed_port = True
        port = str(sys.argv[p_index + 1])
        count += 2
    #
    if "-v" in sys.argv:
        v_index = (sys.argv).index("-v")
        if len(sys.argv) == v_index + 1 or str(sys.argv[v_index + 1]) in ['-p', '-v']:
            print("Wrong parameter. Enter \"snphub create container -h\" for help.")
            print("")
            exit(1)
        mount = True
        mount_path = str(sys.argv[v_index + 1])
        count += 2
    #
    if argv_len > count:
        print("Wrong parameter. Enter \"snphub create container -h\" for help.")
        print("")
        exit(1)
    #
    try:
        if mount:
            out_bytes = subprocess.call(" ".join(['docker', 'run', '-d', '-p', port+':5000', '-v', mount_path + ':/snphub_data', 'snphub_image', '''python /run_snphub''']), shell=True)
        else:
            out_bytes = subprocess.call(" ".join(['docker', 'run', '-d', '-p', port+':5000', 'snphub_image', '''python /run_snphub sample ''']), shell=True)
    except:
        print("")
        print("Seems an error occured.")
        print("Check weather Docker is correctly installed, and using root account or using \"sudo\" before the command?")
        print("Or check weather the SnpHub image is already created?")
        print("Or check the mount path along with host port?")
        print("")
        exit(1)
        #
    #
    print("Finished")
    print("")
#
