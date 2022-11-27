wget https://devops-course-sep-22.s3.sa-east-1.amazonaws.com/ex1/secretGenerator.tar.gz
cd /c/Users/ayam9/PycharmProjects/DevOpsSep22/02_linux_ex1/
tar -zxvf secretGenerator.tar.gz #extract compressed file
cd src #cd to src directory
mkdir secretDir #create directory
rm -rf maliciousFiles #remove directory and it's content
touch secretDir/.secret #create file into directory
ls -l secretDir/.secret #check permissions of the file
chmod 600 secretDir/.secret #enable only read and write permissions
rm important.link #remove file
./generatesecret.sh #Generate Secret
