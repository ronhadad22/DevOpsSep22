#!/bin/bash
SESSION_ID=$(curl -X POST -H "Content-Type: application/json" -d '{
  "clientVersion": "3.2",
  "message": "Client Hello"
}' http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/clienthello | jq -r '.sessionID')

curl -X POST -H "Content-Type: application/json" -d '{
  "clientVersion": "3.2",
  "message": "Client Hello"
}' http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/clienthello | jq -r '.serverCert' > cert.pem

wget https://devops-course-sep-22.s3.sa-east-1.amazonaws.com/ex2/cert-ca-aws.pem

VERIFICATION_RESULT=$( openssl verify -CAfile cert-ca-aws.pem cert.pem )

if [ "$VERIFICATION_RESULT" != "cert.pem: OK" ]; then
  echo "Server Certificate is invalid."
  exit 1
fi

(dd if=/dev/urandom bs=32 count=1) >masterKey.txt

MASTER_KEY=$(openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER cert.pem | base64 -b 0)

curl  -d '{"sessionID": "'$SESSION_ID'" , "masterKey": "'$MASTER_KEY'",
    "sampleMessage": "Hi server, please encrypt me and send to client!"}'
  -H "Content-Transfer-Encoding: base64"  -H "Content-Type: application/json"
   -X POST http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/keyexchange

