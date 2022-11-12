mkdir secretDir
echo "Created secretDir directory"
rm -r maliciousFiles
echo "Deleted maliciousFiles folder"
touch secretDir/.secret
echo "Created .secret file in secretDir folder"
chmod 600 secretDir/.secret
echo "read and write permission only changed"
rm -r important.link
echo "important.link broken link deleted"
/bin/bash generateSecret.sh

