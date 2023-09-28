//pwd - print the current workind directory to the user

//ls - list the contents of the current working directory

//cd ~ or cd - changes the working directory to the user's home directory

//ls -l - displays the current directory in a long format

//ls -al - displays current directory contents, includding hidden files starting with "." in a long format
ls al - also diplays the current directory contents

//mkdir /tmp/my_first_directory - creates a directory named "my first directory" in the /tmp directory

//mv /tmp/betty /tmp/my_first_directory - moves the file "betty from /tmp to /tmp/my_first_directory"

//rm /tmp/my_first_directory/betty - deletes the file named "betty"

//rm -r /tmp/my_first_directory - deletes "my_first_directory" directory in th /tmp directory.

//cd - - changes the working directory to the previous one

//ln -la . .. /boot - lists all files even ones beginning woth a period character which are nirmally hidden in the current and the parent directory an the /boot directory in long format

//file /tmp/iamafile - prints the type of the file names "iamafile" in the /tm directory

//ln -s /bin/ls __ls__ - creates a symbolic link to bin/ls with name "__ls__" in the working directory.

//cp -u *html .. - copies all the HTML files from the current working dirctory to the parent of the working directory, but only copies files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory

//mv [[:upper:]]* /tmp/u - moves all files beginning with an uppercase letter to the directory.

//rm *~ - deletes all files in the working directory that ends with the character "~".

//mkdir -p welcome/to/school - creates the directories welcome/ welcome/to/ and welcome/to/school/ in the the current directory in just one line.

//ls -xamp - lists all files and directories of the the current dirctory, separated by comms ","

//0 string SCHOOL School
!:mime School 
file -C -m filename.type - creates a magic file School that can be used with the command "file" to detect "School" data files and school data files always contain the string "SCHOOL" at offset 0.
