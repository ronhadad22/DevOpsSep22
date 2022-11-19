#!/bin/bash
# Code by Dean Sorie

wget https://devops-course-sep-22.s3.sa-east-1.amazonaws.com/ex2/cert-ca-aws.pem

RESPONSE1=$(curl -d '{ "clientVersion": "3.2", "message": "Client Hello" }' -H "Content-Type: application/json" -X POST http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/clienthello)


SESSION_ID=$(echo $RESPONSE1 | jq -r '.sessionID')
SERVER_CERT=$(echo $RESPONSE1 | jq -r '.serverCert' | tee cert.pem)
VERIFICATION_RESULT=$( openssl verify -CAfile cert-ca-aws.pem cert.pem )
RANDOM_KEY=$(openssl rand -hex 32)
echo $RANDOM_KEY | dd of=masterKey.txt

if [ "$VERIFICATION_RESULT" != "cert.pem: OK" ]; then
  echo "Server Certificate is invalid."
  exit 1
fi

MASTER_KEY=$(openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER cert.pem | base64 -w 0)

RESPONSE2=$(curl -d '{ "sessionID": "'$SESSION_ID'", "masterKey": "'$MASTER_KEY'", "sampleMessage": "Hi server, please encrypt me and send to client!"  }' -H "Content-Transfer-Encoding: base64" -H "Content-Type: application/json" -X POST http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/keyexchange)

ENCRYPTED_MESSAGE=$(echo $RESPONSE2 | jq -r '.encryptedSampleMessage')

echo $ENCRYPTED_MESSAGE | dd of=encSampleMsg.txt

cat encSampleMsg.txt | base64 -d > encSampleMsgReady.txt

DECRYPTED_SAMPLE_MESSAGE=$(cat encSampleMsgReady.txt | openssl enc -d -aes-256-cbc -pbkdf2 -k $RANDOM_KEY) 

if [ "$DECRYPTED_SAMPLE_MESSAGE" != "Hi server, please encrypt me and send to client!" ]; then
  echo "Server symmetric encryption using the exchanged master-key has failed."
  exit 1
else
  echo "Client-Server TLS handshake has been completed successfully"
fi
