
bucketname='{bucketName=s3dev}'


print(f"aws codeartifact get-package-version-asset --domain 's3={bucketname}' --format maven --package")