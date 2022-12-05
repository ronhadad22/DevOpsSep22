#send Hello HTTP request to the server
curl -X POST http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/clienthello -H 'Content-Type: application/json' -d '{"clientVersion": "3.2", "message": "Client Hello"}' | jq '.' > HelloCl.json
#print the content of the json file
cat HelloCl.json
#save SESSION_ID key from the JSON response
SESSION_ID=`cat HelloCl.json | jq -r '.sessionID'`
#save the server cert in a file called cert.pem
cat HelloCl.json | jq -r '.serverCert' > cert.pem
#verify the certificate.
wget https://devops-course-sep-22.s3.sa-east-1.amazonaws.com/ex2/cert-ca-aws.pem
#snippet to exit the program if the certificate validation failed.
VERIFICATION_RESULT=$( openssl verify -CAfile cert-ca-aws.pem cert.pem )

if [ "$VERIFICATION_RESULT" != "cert.pem: OK" ]; then
  echo "Server Certificate is invalid."
  exit 1
fi
#generate and save a 32 random bytes string
RANDOM_KEY=$(openssl rand -hex 32)
echo $RANDOM_KEY > masterKey.txt
#encrypt the generated master-key secret with the server certificate.
MASTER_KEY=$(openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER cert.pem | base64 -w 0)
#an HTTP POST request to the server endpoint /keyexchange.
curl -X POST http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/keyexchange -d '{"sessionID": "'$SESSION_ID'", "masterKey": "'$MASTER_KEY'", "sampleMessage": "Hi server, please encrypt me and send to client!"}' -H "Content-Transfer-Encoding: base64" -H 'Content-Type: application/json' | jq '.' > EncSamp.json
#print the content of the json file
cat EncSamp.json
#extract the encrypted message from server
cat EncSamp.json | jq -r '.encryptedSampleMessage' > encSampleMsg.txt
#convert from Base64 to Binary
cat encSampleMsg.txt | base64 -d > encSampleMsgReady.txt
#exit the program upon an invalid decryption
if [ "$DECRYPTED_SAMPLE_MESSAGE" != "Hi server, please encrypt me and send to client!" ]; then
  echo "Server symmetric encryption using the exchanged master-key has failed."
  exit 1
else
  echo "Client-Server TLS handshake has been completed successfully"
fi