#!/bin/bash
curl -X POST -H "Content-Type: application/json" -d '{"clientVersion": "3.2","message": "Client Hello"}' http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/clienthello | jq -r '.serverCert' > cert.pem
curl -X POST -H "Content-Type: application/json" -d '{"clientVersion": "3.2","message": "Client Hello"}' http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/clienthello | jq -r '.sessionID' > session_id
SESSION_ID=$(cat session_id)
wget https://devops-course-sep-22.s3.sa-east-1.amazonaws.com/ex2/cert-ca-aws.pem
openssl verify -CAfile cert-ca-aws.pem cert.pem

VERIFICATION_RESULT=$( openssl verify -CAfile cert-ca-aws.pem cert.pem )

if [ "$VERIFICATION_RESULT" != "cert.pem: OK" ]; then
  echo "Server Certificate is invalid."
  exit 1
fi

openssl rand -hex 32 > masterKey.txt
openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER cert.pem | base64 -w 0 > masterkey_secret
MASTER_KEY=$(cat masterkey_secret)
curl -X POST -H "Content-Type: application/json" -d '{"sessionID": "'$SESSION_ID'","masterKey": "'$MASTER_KEY'","sampleMessage": "Hi server, please encrypt me and send to client!"}' http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/keyexchange | jq -r '.encryptedSampleMessage' > encSampleMsg.txt
cat encSampleMsg.txt | base64 -d > encSampleMsgReady.txt
openssl enc -d -aes-256-cbc -pbkdf2 -k masterKey -in encSampleMsgReady.txt -out decSampleMsg.txt

if [ "$DECRYPTED_SAMPLE_MESSAGE" != "Hi server, please encrypt me and send to client!" ]; then
  echo "Server symmetric encryption using the exchanged master-key has failed."
  exit 1
else
  echo "Client-Server TLS handshake has been completed successfully"
fi