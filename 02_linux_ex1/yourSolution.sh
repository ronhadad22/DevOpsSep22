#!/bin/bash

mkdir secretDir
rm -r ./maliciousFiles/
touch ./secretDir/.secret
sudo chmod 600  ./secretDir/.secret
rm important.link

