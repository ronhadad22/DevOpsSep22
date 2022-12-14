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

curl -k -X POST http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/keyexchange -d '{"sessionID": "'$SESSION_ID'", "masterKey": "'$MASTER_KEY'", "sampleMessage": "Hi server, please encrypt me and send to client!"}'  -H "Content-Transfer-Encoding: base64" -H "Content-Type: application/json" | jq -r '.encryptedSampleMessage' > encrypted_file.json

cat encrypted_file.json  | jq -r '.encryptedSampleMessage' > encSampleMsg.txt

cat encSampleMsg.txt | base64 -d > decryptedmessage.txt

DECRYPTED_SAMPLE_MESSAGE=$(openssl enc -d -aes-256-cbc -pbkdf2 -kfile masterKey.txt -in decryptedmessage.txt)

if [ "$DECRYPTED_SAMPLE_MESSAGE" != "Hi server, please encrypt me and send to client!" ]; then   echo "Server symmetric encryption using the exchanged master-key has failed.";   exit 1; else   echo "Client-Server TLS handshake has been completed
successfully"; fi