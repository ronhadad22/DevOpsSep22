# installing the package as required(mac)
#'''brew install jq'''

# saving request output to the exercise.json file
curl -k -X POST http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/clienthello                                                    -d '{"clientVersion": "3.2", "message": "Client Hello"}' \
-H "Content-Type: application/json" | tee > exercise.json
#extract sessionID ServerVersion and public key
grep -o '"sessionID": "[^"]*' exercise.json | grep -o '[^"]*$'| tee > sessionID
SESSION_ID=`cat sessionID`
grep -o '"serverVersion": "[^"]*' exercise.json | grep -o '[^"]*$'| tee > serverVersion
SERVER_VERSION=`cat serverVersion`
grep -o '"serverCert": "[^"]*' exercise.json | grep -o '[^"]*$'| sed 's/\\n/\
/g' | tee > cert.pem
SERVER_CERT=`cat cert.pem`


#cat exercise.json| jq -r '.sessionID’ > sessionID.json
#cat exercise.json| jq -r '.serverVersion' > serverVersion.json
#cat exercise.json| jq -r '.serverCert > serverCert.json

# download CA for authentication
wget https://devops-course-sep-22.s3.sa-east-1.amazonaws.com/ex2/cert-ca-aws.pem

#verify public key with CA
VERIFICATION_RESULT=`openssl verify -CAfile cert-ca-aws.pem cert.pem`

if [ "$VERIFICATION_RESULT" != "cert.pem: OK" ]; then
  echo "Server Certificate is invalid."
  exit 1
fi
# create 32 byte random key
openssl rand -hex 32 | tee > masterKey.txt
# encrypt symetric key with public key
# base 64 mac doesnt contain -w 0 flag
MASTER_KEY=`openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER cert.pem | base64`
# uncomment this for linux
#MASTER_KEY=`openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER cert.pem | base64 -w 0`

# send encrypted symetric key to server
curl -k -X POST http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/keyexchange --data '{"sessionID": "'$SESSION_ID'", "masterKey": "'$MASTER_KEY'", "sampleMessage": "Hi server, please encrypt me and send to client!"}'  -H "Content-Transfer-Encoding: base64" -H "Content-Type: application/json" | tee > encrypted_file.json

#extract the recieved encrypted messeage from server
grep -o '"encryptedSampleMessage": "[^"]*' encrypted_file.json | grep -o '[^"]*$' | tee > encrypted_message.txt 

# convert from base64 to Binary
cat encrypted_message.txt | base64 -d > decryptedmessage.txt

# decrypt the sample message
DECRYPTED_SAMPLE_MESSAGE=`openssl enc -d -aes-256-cbc -pbkdf2 -kfile masterKey.txt -in decryptedmessage.txt`


if [ "$DECRYPTED_SAMPLE_MESSAGE" != "Hi server, please encrypt me and send to client!" ]; then echo "Server symmetric encryption using the exchanged master-key has failed."
  exit 1
else
  echo "Client-Server TLS handshake has been completed successfully"
fi

