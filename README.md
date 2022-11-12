# DevOpsSep22
ex 1 

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


