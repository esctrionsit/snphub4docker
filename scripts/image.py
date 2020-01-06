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
    print("Usage:          snphub create image [options]")
    print("Description:    build a SnpHub docker image (only need run once generally)")
    print("Options:")
    print("     -l <path>     print Docker build log into a file")
    print("                   (absolute path is recommended)")
    print("")
else:
    log_output = False
    log_output_path = ""
    count = 1
    #
    if "-l" in sys.argv:
        l_index = (sys.argv).index("-l")
        if len(sys.argv) == l_index + 1:
            print("Wrong parameter. Enter \"snphub create image -h\" for help.")
            print("")
            exit(1)
        log_output = True
        log_output_path = sys.argv[l_index + 1]
        count += 2
    #
    if argv_len > count:
        print("Wrong parameter. Enter \"snphub create image -h\" for help.")
        print("")
        exit(1)
    #
    try:
        out_bytes = subprocess.check_output(['docker', 'build', DIR+'/../Docker_build/', '-t', 'snphub_image'])
    except:
        print("")
        print("Seems an error occured.")
        print("Check weather Docker is correctly installed, and using root account or using \"sudo\" before the command?")
        print("Or check the docker build log? (using \"-l <path>\")")
        print("")
        exit(1)
        #
    #
    out_text = out_bytes.decode('utf-8')
    # Write log file
    if log_output:
        try:
            f = open(log_output_path, "w")
            f.write(out_text)
            f.close()
        except:
            print("WARRING: failed to write Docker log file")
        #
    #
    out_last_line = out_text.split('\n')[-2]
    if  out_last_line.split()[0]== u"Successfully":
        print("Success")
        print("")
        exit(0)
    else:
        print("Docker image building progess seems failed.")
        print("Run command with \"-l <path>\" could output log file into a specific path.")
        print("")
        exit(1)
