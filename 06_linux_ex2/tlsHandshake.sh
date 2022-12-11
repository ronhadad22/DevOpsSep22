(curl -X POST http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/clienthello -H "Content-Type: application/json" -d '{"clientVersion": "3.2", "message": "Client Hello"}')

SESSION_ID=$(echo $R1 | jq -r '.sessionID')
SERVER_CERT=$(echo $R1 | jq -r '.serverCert' | tee cert.pem)
VERIFICATION_RESULT=$( openssl verify -CAfile cert-ca-aws.pem cert.pem )
random=$(openssl rand -hex 32)
echo $random | dd of=master.txt

if [ "$VERIFICATION_RESULT" != "cert.pem: OK" ]; then
  echo "Server Certificate is invalid."
  exit 1
fi

MASTER_KEY=$(openssl smime -encrypt -aes-256-cbc -in master.txt -outform DER cert.pem | base64 -w 0)

R2=$(curl -d '{ "sessionID": "'$SESSION_ID'", "master": "'$MASTER'", "sampleMessage": "Hi server, please encrypt me and send to client!"  }' -H "Content-Transfer-Encoding: base64" -H "Content-Type: application/json" -X POST http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/keyexchange)

ENCRYPTEDMESSAGE=$(echo $R2 | jq -r '.encryptedSampleMessage')

echo $ENCRYPTEDMESSAGE | dd of=encSampleMsg.txt

cat encSampleMsg.txt | base64 -d > encSampleMsgReady.txt

DECRYPTED_SAMPLE_MESSAGE=$(cat encSampleMsgReady.txt | openssl enc -d -aes-256-cbc -pbkdf2 -k $RANDOM_KEY)

if [ "$DECRYPTED_SAMPLE_MESSAGE" != "Hi server, please encrypt me and send to client!" ]; then
  echo "Server symmetric encryption using the master-key has failed."
  exit 1
else
  echo "Client-Server has been completed successfully"
fi
