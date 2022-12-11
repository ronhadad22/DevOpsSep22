 mkdir net1
 cd net1
  curl -d '{ "clientVersion": "3.2", "message": "Client Hello" }' -H "Content-Type: application/json" -X POST http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/clienthello | tee AWS.txt
cat AWS.txt
{"serverVersion": "3.2", "sessionID": "e0dddd40-0046-4b36-8eb3-d8eb59f8ac53", "serverCert": "-----BEGIN CERTIFICATE-----\nMIIFsTCCA5mgAwIBAgIJAJfxoAiN4eBMMA0GCSqGSIb3DQEBDQUAMG8xCzAJBgNV\nBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5nMRAwDgYDVQQHDAdCZWlqaW5nMRAwDgYD\nVQQKDAdleGFtcGxlMREwDwYDVQQLDAhQZXJzb25hbDEXMBUGA1UEAwwOeW91cmRv\nbWFpbi5jb20wHhcNMjIxMTE2MTMzMjIxWhcNMzIxMTEzMTMzMjIxWjBvMQswCQYD\nVQQGEwJDTjEQMA4GA1UECAwHQmVpamluZzEQMA4GA1UEBwwHQmVpamluZzEQMA4G\nA1UECgwHZXhhbXBsZTERMA8GA1UECwwIUGVyc29uYWwxFzAVBgNVBAMMDnlvdXJk\nb21haW4uY29tMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA0Zb0In+T\nPtxgEQ2C58ZLTqru2oYuKGOOC2BfaSYaopOAajOkAB8/YdxtW/LzcbZbBEIYZgdq\nNUcOCj9KWj3OTi9KJ/90Xi3TTCnegpabnuxuJ+dSvc9WfxDILkr3VFkpx+jNCbmS\nmIpVcJNob/hMWZORSyD6d966knALRJZW3v/qqZ5Bd1iNffjCcgpf/RgABARkS/iP\ncljPCRaeBqJmZdLmEIQm7xL6G3hWVbY4RjIKggwVWYnjoZkDcSC1SjRho6m2bu0V\nQ5N0yxG+og5yz1HxSgv4QmoHEyw7nlQGH6NR7RPrj+vstMeN0YoQTL/lPW5Xdu9h\n39udhHEsx90ZWKmSuhRaHEF+8fNFpwvKlpDPpoyQ95tvW3nvwE4BOuWR9SIHEGm8\nOzIbXVu+vIStu44QezHvJeWNT2SU1VygAYgk9+/UeDC5PM6bhpzyvozSc10Anwhw\npq9yVN+boxIwGG/c0S+/O3cx+OjN5y0luymV47bzlwy1RYAuTsvPpa5K/OuYJc0F\nb8/vGrly/CbzCp6MyKsgtW034g2d0OfjLxA+9Y4Q0GUrBlIueOfuV1li/jzipTZC\nwsA8pfP1mIzj2DdVbjQH9Ebq4WEBmOYl2pQ6cieRlqUw7EvpYRcDeJfEkltIep4G\n5E924QPlAX6V344OdkArbOIME3KAtIiEAJsCAwEAAaNQME4wHQYDVR0OBBYEFJ0Q\nXOltcBF2D5FQkmJIokke1MRSMB8GA1UdIwQYMBaAFJ0QXOltcBF2D5FQkmJIokke\n1MRSMAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQENBQADggIBAEt0fR28HhooBUKB\nt6xRPJGrGGO7WIW0k+onVpquE3G4Wnxm89QrBbihaFTGfoGQGmP/ipMWAjbUd9Bz\nov70qLK+msC7cW1cviddaSvMZ3Am9vVQr0e7bvDpjX+P3rCK0w46DoPZV6WacXtV\nN6Cc8/N+GCEvvEYfQbR0yrX7UUuNxTxBdTSDMMHnCr89oO5+1Kn5vhFi7++wqdhr\nGz8WmK6l4fL9OZU5mkpMctGWpBD28j9yd2MWWhkQlyn/jRRy72zCHDyqO4Lnwkro\nLzbIE+CH7shpYyYN39vlLi05Dyxx3hy01GIOhvaecZXIVfWM9lfEiYj/wNXiExr0\neTyRGrhwf4Gq+Ol5byjwSgs4eOFtHxdDko+Ip7NcItcX1It9JCbaVf+W9VmP26cT\nAd6yi6qaQrPorhTuNs/sI1wVgblRkTpdEzud9DdAGAJyOch6s9M6Nn4ga7yXzs5a\nLTjVYYgxsd2uP+499WCRZyP/84usjZRu1AiLmEzlpykFk8ZQ2FrE4B14gERwkkDT\nxzJ0eSbyqxhi0Ex1SyPq4cERx2yqYNXJrhM1IQkyHpnVanKbk9OvuGRBX+SDfLup\nsh/agHpG6icariKTbyjyWHLbz/dYT2n6oQ5b+nofv7eCqC3G1YMXZ0I1r5/EKhtx\n35O8gYNE8K1j/xgnkS3IRELqofW+\n-----END CERTIFICATE-----\n"}
wget https://devops-course-sep-22.s3.sa-east-1.amazonaws.com/ex2/cert-ca-aws.pem

SESSION_ID=$(cat AWS.txt | jq -r '.sessionID')
SERVER_CERT=$(cat AWS.txt | jq -r '.serverCert' | tee cert.pem)

VERIFICATION_RESULT= openssl verify -CAfile cert-ca-aws.pem cert.pem\
cert.pem: OK

MASTER_KEY=$(openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER cert.pem | base64 -w 0)

RANDOM_KEY=$(openssl rand -hex 32)


echo $RANDOM_KEY |tee masterKey.txt

RESPONE=$(curl -d '{ "sessionID": "'$SESSION_ID'", "masterKey": "'$MASTER_KEY'", "sampleMessage": "Hi server, please encrypt me and send to client!"  }' -H "Content-Transfer-Encoding: base64" -H "Content-Type: application/json" -X POST http://ec2-54-207-102-47.sa-east-1.compute.amazonaws.com:8081/keyexchange)

ENCRYPTED_MESSAGE=$(echo $RESPONSE | jq -r '.encryptedSampleMessage')

echo $ENCRYPTED_MESSAGE |tee encSampleMsg.txt


cat encSampleMsg.txt | base64 -d > encSampleMsgReady.txt

DECRYPTED_SAMPLE_MESSAGE=$(cat encSampleMsgReady.txt | openssl enc -d -aes-256-cbc -pbkdf2 -k $RANDOM_KEY)

