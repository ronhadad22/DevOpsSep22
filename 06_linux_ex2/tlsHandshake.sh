#!/bin/bash


curl -X POST -H "Content-Type:  application/json" -d '{"clientVersion": "3.2", "message": "Client Hello"}' http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/clienthello | jq -r ."serverVersion" > serverVersion
curl -X POST -H "Content-Type:  application/json" -d '{"clientVersion": "3.2", "message": "Client Hello"}' http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/clienthello | jq -r ."sessionID" > sessionID
curl -X POST -H "Content-Type:  application/json" -d '{"clientVersion": "3.2", "message": "Client Hello"}' http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/clienthello | jq -r ."serverCert" > serverCert

wget https://devops-course-sep-22.s3.sa-east-1.amazonaws.com/ex2/cert-ca-aws.pem
mv serverCert cert.pem
VERIFICATION_RESULT=$( openssl verify -CAfile cert-ca-aws.pem cert.pem )

if [ "$VERIFICATION_RESULT" != "cert.pem: OK" ]; then
  echo "Server Certificate is invalid."
  exit 1
fi

openssl genrsa -out yourdomain.com.key 4096

openssl req -sha512 -new \
    -subj "/C=CN/ST=Beijing/L=Beijing/O=example/OU=Personal/CN=yourdomain.com" \
    -key yourdomain.com.key \
    -out masterKey.txt


openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER cert.pem | base64 -w 0

MASTER_KEY='cat masterKey.txt'
SESSION_ID='cat sessionID'


curl -X POST -H "Content-Type:application/json" -d '{"sessionID":"'$SESSION_ID'","masterKey":"'$MASTER_KEY'","sampleMessage": "Hi server, please encrypt me and send to client!"}' http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/keyexchange


cat encSampleMsg.txt | base64 -d > encSampleMsgReady.txt

if [ "$DECRYPTED_SAMPLE_MESSAGE" != "Hi server, please encrypt me and send to client!" ]; then
  echo "Server symmetric encryption using the exchanged master-key has failed."
  exit 1
else
  echo "Client-Server TLS handshake has been completed successfully"
fi