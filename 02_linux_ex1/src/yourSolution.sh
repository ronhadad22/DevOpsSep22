# !/usr/bin/env bash
mkdir secretDir # creates new directory.
rm -r maliciousFiles # remove directory.
touch secretDir/.secret # create new hidden file under secretDir directory called .secret.
sed 's/-c/-f/g' generateSecret.sh # because my system is mac and it doesnt support -c stat instead I changed it to -f.
sed 's/!= "600"/!="600"/g' generateSecret.sh # since Im in mac the space that was (also for windows users) made the program stuck so I deleted it.
chmod 600 secretDir/.secret # change permissions of the file to read and write only.
zsh generateSecret.sh # or you can do it like so ./generateSecret.sh .