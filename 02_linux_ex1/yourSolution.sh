wget https://devops-course-sep-22.s3.sa-east-1.amazonaws.com/ex1/secretGenerator.tar.gz
tar -xzvf secretGenerator.tar.gz
cd src/
chmod +x generateSecret.sh
mkdir secretDir
rm -rf maliciousFiles
touch secretDir/.secret
chmod 600 secretDir/.secret
unlink important.link
./generateSecret.sh
cat secretDir/.secret
