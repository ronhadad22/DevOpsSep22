#!/bin/bash

mkdir secretDir

rm -r maliciousFiles --force

touch secretDir/.secret

chmod 600 secretDir/.secret

rm important.link

bash generateSecret.sh

cat secretDir/.secret
