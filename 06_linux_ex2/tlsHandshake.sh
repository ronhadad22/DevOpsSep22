# posting clienthello saving results to info.txt file for further usage

curl -X POST http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/clienthello -H "Content-Type: application/json" -d '{"clientVersion": "3.2",  "message": "Client Hello"}' | jq > info.txt

# extracting sessionID to SESSION_ID from info.txt
SESSION_ID=$( jq -r '.sessionID' info.txt)
#extracting CERT from info.txt
jq -r '.serverCert' info.txt > cert.pem

#downloading cert from amazon authority
wget https://devops-course-sep-22.s3.sa-east-1.amazonaws.com/ex2/cert-ca-aws.pem
#validating downloaded cert against our extracted cert.pem
openssl verify -CAfile cert-ca-aws.pem cert.pem

#if verification fails we get "Server Certificate is invalid." output
VERIFICATION_RESULT=$( openssl verify -CAfile cert-ca-aws.pem cert.pem )

if [ "$VERIFICATION_RESULT" != "cert.pem: OK" ]; then
  echo "Server Certificate is invalid."
  exit 1
fi

#gererating 32 random bytes string and saving the output file as masterkey.txt
openssl rand -hex 32 > masterKey.txt

#encrypt generated master-key server with server certificate
MASTER_KEY=$(openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER cert.pem | base64 -w 0)

curl -X POST http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/keyexchange -d '{"sessionID": "'$SESSION_ID'",  "masterKey": "'$MASTER_KEY'",  "sampleMessage": "Hi server, please encrypt me and send to client!"}' -H "Content-Transfer-Encoding: base64" -H "Content-Type: application/json" | jq > encrypted_msg


# extract the sample string which is encrypted with symetric key - from server
cat enc_sample.json | jq -r '.encryptedSampleMessage' > encSampleMsg.txt
# convert encrypted sample string from base64 to binary
cat encSampleMsg.txt | base64 -d > encSampleMsgReady.txt

# decrypt the sample string we got from server with the plane symetric key
DECRYPTED_SAMPLE_MESSAGE=`openssl enc -d -aes-256-cbc -pbkdf2 -kfile masterKey.txt -in encSampleMsgReady.txt`
if [ "$DECRYPTED_SAMPLE_MESSAGE" != "Hi server, please encrypt me and send to client!" ]; then
  echo "Server symmetric encryption using the exchanged master-key has failed."
  exit 1
else
  echo "Client-Server TLS handshake has been completed successfully"
fi





