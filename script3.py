#!/usr/bin/env python3.7

import subprocess
import os
import sys
import shutil as sh


def evmcodeInstantiation():	
	print("Environment variables will be set to change which peer is targeted ")
	os.system("docker exec cli bash -c \" export CORE_PEER_MSPCONFIGPATH=/opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp; export CORE_PEER_ADDRESS=peer0.org1.example.com:7051\" ")
	os.system("docker exec cli bash -c \" export CORE_PEER_LOCALMSPID=\"Org1MSP\"; export CORE_PEER_TLS_ROOTCERT_FILE=/opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt \" ")
	os.system("docker exec cli bash -c \" peer chaincode install -n evmcc -l golang -v 0 -p github.com/hyperledger/fabric-chaincode-evm/evmcc \" ")
	command = "peer chaincode instantiate -n evmcc -v 0 -C mychannel -c \'{\"Args\":[]}\' -o orderer.example.com:7050 --tls --cafile /opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem"
	os.system("docker exec cli bash -c \" command \" ")
	print("current working directory in container:")
	os.system("docker exec cli pwd") 
	

	

evmcodeInstantiation()