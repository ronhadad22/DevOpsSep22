#!bin/bash

# Create directory
  mkdir secretDir

  # Create file
    touch /home/happytoast17/test/src/secretDir/.secret

    # Give permissions
      chmod 600 /home/happytoast17/test/src/secretDir/.secret

      # Remove malicious directory
        rm -r maliciousFiles

        # Remove bad link
        unlink important.link

        # Make the script executable
          chmod u+x generateSecret.sh