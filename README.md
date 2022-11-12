# DevOpsSep22
ex 1 

rosindima10092@gmail.com
814c5723c21e7e90a3eae36c8df3c513  -



Kernel System Calls
-------------------
`
stat("./welcomeToDevOpsMay22", {st_mode=S_IFDIR|0700, st_size=4096, ...}) = 0
`

Created new folder named "welcomToDevOpsMay22" with 0700 permissions

`openat(AT_FDCWD, "welcomeToDevOpsMay22/goodLuck", O_WRONLY|O_CREAT|O_TRUNC, 0666) = 3`

Created File called "goodLuck" in welcomeToDevOpsMay22" folder and changer permissions to 0666

`newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=0, ...}, AT_EMPTY_PATH) = 0`

file permissions changed to 0644.

`write(3, "There you go... tell me what I d"..., 36) = 36`

In "goodLuck" file wrote "There you go... tell me what I do..."

`close(3)`

closed the file.

Binary Numbers
--------------
Q1 :Convert the following binary numbers to a decimals: 111, 100, 10110

A1:
    111 = 7
    100 = 4
    10110 = 22

Q2: What is the available decimal range represented by a 8 bits binary number?

A2: With 8 bits, the maximum number of values is 256 or 0 through 255.

Q3: Given a 9 bits binary number, suggest a method to represent a negative numbers between 0-255

A3: 9 binary number is looks like:

    +/-   128     64     32     16      8      4      2      1
     0      0      0      0      0      0      0      0      0

The first 0/1 at the left tells us if its a positive or a negative number.

    1 = Negatine
    0 = Possitive

Example for negative 9 bits binary number: 

    100101010 = -42





    
