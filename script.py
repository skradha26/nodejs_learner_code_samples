#!/usr/bin/env python3.7

import subprocess
import os
import sys
import pathlib


'''
Script follows the steps in Part 1 of https://github.com/crcresearch/evm-fabric-setup
'''

def dockertestfunc():
    dockerimageslist = subprocess.call('''(docker images | grep hyperledger | awk '/^.*\s/ {print $3}')''', shell=True)
    print(dockerimageslist)
    if dockerimageslist == 0:
        print("No dangling hyperledger docker images found")


    output = subprocess.call('''docker rmi -f $(docker images | grep hyperledger | awk '/^.*\s/ {print $3}') ''',stderr=subprocess.DEVNULL,shell=True)
    print("output \n" , output)
    if output == 1:
        print("Docker images couldn't be removed because of the following error")
        subprocess.call('''docker rmi -f $(docker images | grep hyperledger | awk '/^.*\s/ {print $3}') ''', shell=True)  

    else:
        corefunc()           


def corefunc():
    print("Checking Go path..")
    output = str(os.system("echo $PATH | grep -q \"/Users/sradha/.go\" && echo \"go path exists\""))
    if output != "found it":
        home = os.getenv("HOME")
        gopath = home + "/.go"
        print("Path to GO folder", gopath)
        os.mkdir(gopath)
        addPath = os.getenv("PATH") + ":" + "/" + gopath
        print("GOPATH will be added to your PATH \n\n")
        print(addPath)
        os.environ['PATH']=addPath
        path1 = os.getenv("PATH")
    else:
        proceed_yes = input("Go path exists")  
    
    user_input = input("Proceeding to get Hyperledger Fabric Samples and Download Fabric Images.. Press ENTER to continue..")
    print("Hyperledger directory will be created in the path: $GOPATH/src/github.com/hyperledger \n\n")
    os.makedirs(gopath + "/src/github.com/hyperledger")
    print("Changing working directory to", gopath + "/src/github.com/hyperledger \n\n")
    os.chdir(gopath + "/src/github.com/hyperledger")
    fabricsamplespath = os.getcwd()
    clone = "git clone https://github.com/hyperledger/fabric-samples.git"
    os.system(clone)
    os.chdir(gopath + "/src/github.com/hyperledger" + "/fabric-samples")
    checkoutRelease = "git checkout release-1.4"
    os.system(checkoutRelease)
    #make binaries available on your path
    fabricbinariespath = os.getcwd()+ "/bin" + os.getenv("PATH")
    os.environ['PATH']= fabricbinariespath
    dockerimagesdownload = "curl -sSL https://bit.ly/2ysbOFE | bash -s -- 1.4.0 1.4.0 0.4.18"
    os.system(dockerimagesdownload)
    print("Download complete!")
    sys.exit()


dockertestfunc();
