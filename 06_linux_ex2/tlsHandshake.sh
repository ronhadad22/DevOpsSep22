curl  -X POST  http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/clienthello -H 'Content-Type: application/json'  -d '{"clientVersion": "3.2", "message": "Client Hello"}' |  jq -r '.serverCert' > cert.pem

SESSION_ID=$(curl  -X POST  http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/clienthello -H 'Content-Type: application/json'  -d '{"clientVersion": "3.2", "message": "Client Hello"}' |  jq '.sessionID' )


echo SESSION_ID=$SESSION_ID


#openssl verify -CAfile cert-ca-aws.pem cert.pem

if [ ! -f "cert-ca-aws.pem" ]; then
        wget https://devops-course-sep-22.s3.sa-east-1.amazonaws.com/ex2/cert-ca-aws.pem

fi

VERIFICATION_RESULT=$(openssl verify -CAfile cert-ca-aws.pem cert.pem)

echo VERIFICATION_RESULT=$VERIFICATION_RESULT

if [ "$VERIFICATION_RESULT" != "cert.pem: OK" ]; then
          echo "Server Certificate is invalid."
            exit 1
fi

openssl rand -hex 32> masterKey.txt

MASTER_KEY=$(openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER cert.pem | base64 -w 0)


curl  -X POST  http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/keyexchange -H 'Content-Type: application/json'  -d '{"sessionID": '$SESSION_ID',"masterKey": "'$MASTER_KEY'","sampleMessage": "Hi server, please encrypt me and send to client!"}'  |  jq -r '.encryptedSampleMessage' > encSampleMsg.txt

cat encSampleMsg.txt | base64 -d > encSampleMsgReady.txt

MKEY=$(cat masterKey.txt)
DECRYPTED_SAMPLE_MESSAGE=$(openssl enc -d -aes-256-cbc -pbkdf2 -k "$MKEY" -in encSampleMsgReady.txt)
echo DECRYPTED_SAMPLE_MESSAGE=$DECRYPTED_SAMPLE_MESSAGE

if [ "$DECRYPTED_SAMPLE_MESSAGE" != "Hi server, please encrypt me and send to client!" ]; then
          echo "Server symmetric encryption using the exchanged master-key has failed."
            exit 1
    else
              echo "Client-Server TLS handshake has been completed successfully"
fi