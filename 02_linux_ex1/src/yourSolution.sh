#!/bin/bash

mkdir secretDir
rmdir maliciousFiles
> secretDir/.secret
sudo chmod 600 secretDir/.secret
OCTAL_PERMISSIONS=$(stat -c "%a" secretDir/.secret)
unlink important.link
at ./CONTENT_TO_HASH | xargs | md5sum > secretDir/.secret && echo "Done! Your secret was stored in secretDir/.secret"

