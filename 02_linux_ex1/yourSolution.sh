#!/bin/bash

chmod +x yourSolution.sh

# practice dir creation
if [ ! -d "secretDir" ]; then

 mkdir "secertDir"
fi

# practice dir deletion and file move
if [ -d "maliciousFiles" ]; then

 rm -r maliciousFiles
fi

# practice file creation
if [ ! -f "secretDir/.secret" ]; then

 touch .secert
fi

# practice change permissions
OCTAL_PERMISSIONS=$(stat -c "%a" secretDir/.secret)
if [ "$OCTAL_PERMISSIONS" != "600" ]; then

chmod 600 .secret
fi

# practice file linking understanding
if [ -L 'important.link' ] && [ ! -e 'important.link' ]; then

  rm -r important.link
fi

cat ./CONTENT_TO_HASH | xargs | md5sum > secretDir/.secret&& echo "Done! Your secret was stored in secretDir/.secret"