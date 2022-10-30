#!/bin/bash

mkdir secretDir

rm -r maliciousFiles --force

touch secretDir/.secret

chmod 600 secretDir/.secret

rm important.link

cat ./CONTENT_TO_HASH | xargs | md5sum > secretDir/.secret
