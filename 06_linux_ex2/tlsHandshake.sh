#!/bin/bash

Return_1=$(curl -X POST -H "Content-Type: application/json" \
-d '{"clientVersion": "3.2", "message": "Client Hello"}' \
    http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/clienthello)

SESSION_ID=$(echo $Return_1 | jq -r '.sessionID')

echo $Return_1 | jq -r '.serverCert' > cert.pem
SERVER_CERT=$(cat cert.pem)

wget https://devops-course-sep-22.s3.sa-east-1.amazonaws.com/ex2/cert-ca-aws.pem

VERIFICATION_RESULT=$(openssl verify -CAfile cert-ca-aws.pem cert.pem) ; echo $VERIFICATION_RESULT

if [ "$VERIFICATION_RESULT" != "cert.pem: OK" ]; then
  echo "Server Certificate is invalid."
  exit 1
fi

openssl rand -hex 32 > masterKey.txt
RANDOM_KEY=$(cat masterKey.txt)
MASTER_KEY=$(openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER cert.pem | base64 -w 0)

Return_2=$(curl -X POST -H "Content-Type: application/json" \
-d '{
    "sessionID": "'$SESSION_ID'",
    "masterKey": "'$MASTER_KEY'",
    "sampleMessage": "Hi server, please encrypt me and send to client!"
}' \
    http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/keyexchange)

echo $Return_2 | jq -r '.encryptedSampleMessage' > encSampleMsg.txt
ENCRYPTED_MESSAGE=$(cat encSampleMsg.txt)

cat encSampleMsg.txt | base64 -d > encSampleMsgReady.txt
DECRYPTED_SAMPLE_MESSAGE=$(cat encSampleMsgReady.txt | openssl enc -d -aes-256-cbc -pbkdf2 -k $RANDOM_KEY) 

if [ "$DECRYPTED_SAMPLE_MESSAGE" != "Hi server, please encrypt me and send to client!" ]; then
  echo "Server symmetric encryption using the exchanged master-key has failed."
  exit 1
else
  echo "Client-Server TLS handshake has been completed successfully"
fi
