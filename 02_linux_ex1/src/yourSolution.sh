# !/usr/bin/env bash
mkdir secretDir
rm -r maliciousFiles
touch secretDir/.secret
sed 's/-c/-f/g' generateSecret.sh
sed 's/!= "600"/!="600"/g' generateSecret.sh
chmod 600 secretDir/.secret
zsh generateSecret.sh # or you can do it like so ./generateSecret.sh

