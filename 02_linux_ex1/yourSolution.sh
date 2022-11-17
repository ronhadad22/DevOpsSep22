#!bin/bash

# Create directory
  mkdir secretDir

  # Create file
    touch /home/gil/Devops/src/secretDir/.secret

    # permissions remove for group and other
      chmod g=- , o=- /home/gil/Devops/src/secretDir/.secret

       # Remove link
        unlink important.link

        # Remove malicious directory
        rm -r maliciousFiles

        # Make the script executable
          chmod u+x generateSecret.sh