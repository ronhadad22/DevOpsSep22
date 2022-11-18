#!/bin/bash

wget https://devops-course-sep-22.s3.sa-east-1.amazonaws.com/ex2/cert-ca-aws.pem

RESPONSE1=$(curl -d '{ "clientVersion": "3.2", "message": "Client Hello" }' -H "Content-Type: application/json" -X POST http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/clienthello)


SESSION_ID=$(echo $RESPONSE1 | jq -r '.sessionID')
SERVER_CERT=$(echo $RESPONSE1 | jq -r '.serverCert' | tee cert.pem)
VERIFICATION_RESULT=$( openssl verify -CAfile cert-ca-aws.pem cert.pem )
RANDOM_KEY=$(openssl rand -hex 32)
echo $RANDOM_KEY | dd of=masterKey.txt


echo $SESSION_ID

if [ "$VERIFICATION_RESULT" != "cert.pem: OK" ]; then
  echo "Server Certificate is invalid."
  exit 1
fi

MASTER_KEY=$(openssl smime -encrypt -aes-256-cbc -in masterKey.txt cert.pem | base64 -w 0)
#MASTER_KEY=$(openssl rsa -aes256 -in masterKey.txt -outform DER cert.pem | base64 -w 0)

#echo $MASTER_KEY

RESPONSE2=$(curl -d '{ "sessionID": "'$SESSION_ID'", "masterKey": "'$MASTER_KEY'", "sampleMessage": "Hi server, please encrypt me and send to client!"  }' -H "Content-Type: application/json" -X POST http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/keyexchange)


ENCRYPTED_MESSAGE=$(echo $RESPONSE2 | jq -r '.encryptedSampleMessage')

#echo \n$RESPONSE2\n

#echo $ENCRYPTED_MESSAGE

echo $ENCRYPTED_MESSAGE | dd of=encSampleMsg.txt

cat encSampleMsg.txt | base64 -d > encSampleMsgReady.txt


# Unable to decrypt as of yet, will figure this out tomorrow
#openssl smime -decrypt -in encSampleMsgReady.txt -recip cert.pem
