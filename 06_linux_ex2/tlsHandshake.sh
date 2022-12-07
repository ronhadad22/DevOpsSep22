# #!/bin/bash

##instal jq
#sudo apt -get install jq


## if run the second time and more
#rm cert-ca-aws.pem


## get  reposetory
        curl  -X POST \
        http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/clienthello \
        -H 'Content-Type: application/json' \
        -d '{"clientVersion": "3.2", "message": "Client Hello"}' | jq '.' > response.json

## extract sessionId and certificate from server
        cat response.json | jq -r '.serverCert' > cert.pem

## get ca from repo
        wget -q https://devops-course-sep-22.s3.sa-east-1.amazonaws.com/ex2/cert-ca-aws.pem

## verifing certificat
        VERIFICATION_RESULT=$(openssl verify -CAfile cert-ca-aws.pem cert.pem)

        if [ "$VERIFICATION_RESULT" != "cert.pem: OK" ]; then
          echo "Server Certificate is invalid."
          exit 1
        fi
## create 32 bytes  masterkey
        openssl rand -hex 16 > masterKey.txt
        RANDOM_KEY=$(cat masterKey.txt)
## encript masterkey
        MASTER_KEY=$(openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER cert.pem | base64 -w 0)

## request for keyexchange
        curl -sb -X POST http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/keyexchange \
        -H "Content-Transfer-Encoding: base64" -H "Content-Type: application/json" \
        -d '{"sessionID": "'$SESSION_ID'", "masterKey": "'$MASTER_KEY'", "sampleMessage": "Hi server, please encrypt me and send to client!"}' | jq '.'>ENC_RESP.json


        cat ENC_RESP.json | jq -r '.encryptedSampleMessage' > encSampleMsg.txt
        cat encSampleMsg.txt | base64 -d > encSampleMsgReady.txt


## decrypt the respose message
        DECRYPTED_SAMPLE_MESSAGE=$(openssl enc -d -aes-256-cbc -pbkdf2 -k $RANDOM_KEY -in encSampleMsgReady.txt)


## echo if the job is OK or NOT
        if [ "$DECRYPTED_SAMPLE_MESSAGE" != "Hi server, please encrypt me and send to client!" ]; then
        echo "Server symmetric encryption using the exchanged master-key has failed."
        exit 1
        else
        echo "Client-Server TLS handshake has been completed successfully"
        fi
