#Commands and their uses
//su betty - Switches user to betty
//id -un - prints the effective username of the user
// groups - prints the current groups the current user is part of
//sudo chpwn hello - change the owner of the file to the user betty
//touch hello - prints an empty file called hello
//chmod u+x hello - adds execution permissions to the file hello
//chmod +114 hello - adds execution permission to the owner and the group owner and only read permissions to the users
//chmod +x hello - adds execution permissions to the owner, the file owner and other users
//chmod 007 hello - writes a script that sets the permission to the file hello as follows:
        -  Owner: no permission at all
        -  Group: no permission at all
        -  Other users: all the permissions
//chmod 753 hello - Write a script that sets the mode of the file hello to this:
         -rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
//chmod --reference=olleh hello - writes a script that sets the mode of the file hello the same as olleh’s mode.
