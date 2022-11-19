#ex2
######################################################################################################

#!/bin/bash

# clean environment
reset
cd /tmp/
rm -rf masterKey.txt  encSampleMsg.txt  encSampleMsgReady.txt  cert.pem  DECRYPTED_SAMPLE_MESSAGE  cert-ca-aws.pem* hello.json mykey enc_sample.json
sleep 2
# get session_id and server public key
curl -sb -X POST http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/clienthello --data '{"clientVersion": "3.2", "message": "Client Hello"}' -H "Content-Type: application/json"   | jq '.'  > hello.json
cat hello.json
# extract sessionID
SESSION_ID=`cat hello.json | jq -r '.sessionID'`
# extract server public key
cat hello.json | jq -r '.serverCert' > cert.pem
# get CA certificate to verify server certificate and get server public key
wget https://devops-course-sep-22.s3.sa-east-1.amazonaws.com/ex2/cert-ca-aws.pem
# verify server public key
VERIFICATION_RESULT=$( openssl verify -CAfile cert-ca-aws.pem cert.pem )

if [ "$VERIFICATION_RESULT" != "cert.pem: OK" ]; then
  echo "Server Certificate is invalid."
  exit 1
fi
# create 32 byte random HEX symetric key (aes requires onl hex key!!!!!)
RANDOM_KEY=$(openssl rand -hex 32)
echo $RANDOM_KEY > masterKey.txt
# encrypt symetric key with server public key
MASTER_KEY=$(openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER cert.pem | base64 -w 0)
# send sample string with encrypted symetric key to server
curl -sb  -X POST http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/keyexchange --data '{"sessionID": "'$SESSION_ID'", "masterKey": "'$MASTER_KEY'", "sampleMessage": "Hi server, please encrypt me and send to client!"}'  -H "Content-Transfer-Encoding: base64" -H "Content-Type: application/json" |   jq '.'  >  enc_sample.json
cat enc_sample.json
# extract the sample string which is encrypted with symetric key - from server
cat enc_sample.json | jq -r '.encryptedSampleMessage' > encSampleMsg.txt
# convert encrypted sample string from base64 to binary
cat encSampleMsg.txt | base64 -d > encSampleMsgReady.txt
# decrypt the sample string we got from server with the plane symetric key
DECRYPTED_SAMPLE_MESSAGE=`openssl enc -d -aes-256-cbc -pbkdf2 -k $RANDOM_KEY -in encSampleMsgReady.txt`
if [ "$DECRYPTED_SAMPLE_MESSAGE" != "Hi server, please encrypt me and send to client!" ]; then
  echo "Server symmetric encryption using the exchanged master-key has failed."
  exit 1
else
  echo "Client-Server TLS handshake has been completed successfully"
fi





