curl -k -X POST http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/clienthello -d '{"clientVersion":"3.2","message": "Client Hello"}' \ -H "Content-Type: application/json" | jq > linux_ex2.json

# to connect to the server and recive the SessionID , serverVersion and the Certificate to a json format

cat linux_ex2.json| jq -r '.serverCert' > cert.pem

# to extract the server cert

SERVER_CERT=$(cat cert.pem)

# to set the cert value

cat lunux_ex2.json | jq -r '.sessionID' > sessionID.json

# to extract the session id 

SESSION_ID=$(cat sessionID.json)

# to set the session id value

cat linux_ex2.json| jq -r '.serverVersion' > serverVersion.json

# to extract the server version

SERVER_VERSION=$(cat serverVersion.json)

# to set the server version value

openssl verify -CAfile cert-ca-aws.pem cert.pem

# to verify the certificate

RANDOM_KEY=$(openssl rand -hex 32)
echo $RANDOM_KEY > Master_Key.txt

# to generate a 32 random bytes string and saving it to masterKey.txt text file.

openssl smime -encrypt -aes-256-cbc -in Master_Key.txt -outform DER cert.pem | base64 -w 0

# to encrypt the the generated master-key secret with the server certificate

curl -k -X POST http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/keyexchange --data '{"SessionID": "'$SESSION_ID'", "masterKey": "'$MASTER_KEY'", "sampleMessage": "Hi server, please encrypt me and send to client!"}'  -H "Content-Transfer-Encoding: base64" -H "Content-Type: application/json" | tee > encryption.json

# exchanging the key with the server + encrypting + sending back to client + exporting to encyptio.jason file

cat encryption.json  | jq -r '.encryptedSampleMessage' > encrypted_message.txt

# to extract the encrypted message

cat encrypted_message.txt | base64 -d > decrypted_message.txt

# to decrypt message

DECRYPTED_SAMPLE_MESSAGE=$(openssl enc -d -aes-256-cbc -pbkdf2 -kfile masterKey.txt -in decrypted_message.txt)

# to set decrypted sample message value



if [ "$DECRYPTED_SAMPLE_MESSAGE" != "Hi server, please encrypt me and send to client!" ]; then
  echo "Server symmetric encryption using the exchanged master-key has failed."
  exit 1
else
  echo "Client-Server TLS handshake has been completed successfully"
fi

# to complete the handshake

Client-Server TLS handshake has been completed
successfully
