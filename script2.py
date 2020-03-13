#!/usr/bin/env python3.7

import subprocess
import os
import sys
import shutil as sh

'''
Script follows the steps in Part 1 of https://github.com/crcresearch/evm-fabric-setup from 
"Mount the EVM Chaincode and start the network" till the end of step 1

Before starting this script ensure that you have executed "script.py" so that necessary
folder and docker images are available for successful execution of this script.
'''

def evmchaincodesetup():
	req_complete = input("Before starting this script ensure that you have executed \"script.py\" so that necessary folder and docker images are available for successful execution of this script.. Press Y to continue..")
	if str(req_complete) == 'Y':
		print("proceeding..")
		startEvmChaincodeSetup()
	elif str(req_complete) == 'y':
		print("proceeding..")
		startEvmChaincodeSetup()
	else:
		sys.exit()


def startEvmChaincodeSetup():
	gopath = os.getenv("HOME") + "/.go" + "/src/github.com/hyperledger/"
	os.chdir(gopath)
	print("Cloning fabric-chaincode-evm repo in your GOPATH directory.")
	clone = "git clone https://github.com/hyperledger/fabric-chaincode-evm"
	os.system(clone)
	os.chdir(gopath +"/fabric-chaincode-evm")
	checkoutRelease = "git checkout release-0.1"
	os.system(checkoutRelease)
	os.chdir(gopath + "fabric-samples/first-network")
	print("backing up docker-compose-cli.yaml file")
	sh.copy((gopath + "fabric-samples/first-network" + "/docker-compose-cli.yaml"),(gopath + "fabric-samples/first-network" + "/docker-compose-cli.yaml.backup"))
	os.remove(gopath + "fabric-samples/first-network" + "/docker-compose-cli.yaml")
	sh.copy((gopath + "docker-compose-cli.yaml.orig"),(gopath + "fabric-samples/first-network" + "/docker-compose-cli.yaml.orig"))
	sh.move("docker-compose-cli.yaml.orig","docker-compose-cli.yaml")
	currentdirectory = os.getcwd()
	print(currentdirectory)
	os.system("./byfn.sh generate")
	os.system("./byfn.sh up")   
   

 #def evmchaincodeinstantiatefunc():










		







evmchaincodesetup()