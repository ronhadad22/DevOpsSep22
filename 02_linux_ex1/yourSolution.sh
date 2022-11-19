tar -xf secretGenerator.tar.gz
cd src
rm -rf maliciousFiles
rm -rf important.link
mkdir secretDir
cd secretDir
touch .secret
chmod 600 secretDir/.secret
/bin/bash generateSecret.sh
cd secretDir
cp .secret /home/mortis1983/src
cd ..
cp .secret yourSolution.sh