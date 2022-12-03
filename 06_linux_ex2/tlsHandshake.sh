1)curl -d '{ "clientVersion": "3.2", "message": "Client Hello" }' -H "Content-Type: application/json" -X POST http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/clienthello | tee AWS.txt

2)SESSION_ID=$(jq -r '.sessionID' AWS.txt)

3)jq -r '.serverCert' AWS.txt | tee cert.pem

4)wget https://devops-course-sep-22.s3.sa-east-1.amazonaws.com/ex2/cert-ca-aws.pem

5)VERIFICATION_RESULT=$( openssl verify -CAfile cert-ca-aws.pem cert.pem )

6) if [ "$VERIFICATION_RESULT" != "cert.pem: OK" ]; then
  echo "Server Certificate is invalid."
  exit 1
fi

7) echo $RANDOM | md5sum | head -c 32 | tee masterKey.txt

8) MASTER_KEY=$(openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER cert.pem | base64 -w 0)

9) curl -d '{"sessionID": "'$SESSION_ID'", "masterKey": "'$MASTER_KEY'", "sampleMessage": "Hi server, please encrypt me and send to client!"}' -H "Content-Type: application/json" -H "Content-Transfer-Encoding: base64" -X POST http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/keyexchange | tee encSampleMsg.txt

10) jq -r '.encryptedSampleMessage' encSampleMsg.txt | base64 -d | tee encSampleMsgReady.txt

11) MASTER=$(cat masterKey.txt)

12) openssl enc -d -aes-256-cbc -pbkdf2 -k $MASTER -in encSampleMsgReady.txt -out decrypted.txt