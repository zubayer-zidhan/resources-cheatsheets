#### Case Sensitive

#### ls
- ls : Lists all the files and directories inside the current directory in which you are.
- ls -R : Lists all the files and directories inside the current directory as well as all the files and
directories of the sub-directories as well.
- ls -a : Lists all the files and directories in the current directory and also lists the hidden files.
- ls -al : Lists files and directories of the current directory along with the details like permissions
(read, write, execute), owner, file/dir size, etc.

#### cd
- cd : This command is used to move to the root directory.
- cd .. : Move to one level up directory.
- cd directoryname : Move to a particular directory from the current directory.

#### pwd
- pwd : displays the current directory.

#### mkdir
- mkdir : This command creates a directory.

#### rmdir / rm
- rmdir : It deletes a directory.
- rm : It deletes a file

#### cat
- cat > filename : This command creates a file in the current directory.
- cat filename : This command displays the content in a file.
- cat file1 file2 > file3 : This command joins the content of two files and stores it in the third file.

#### mv
- mv filename new_path : It moves the file to the new path specified.
- mv oldname newname : This command changes the name of the file from the old name.

#### echo
- echo “string” : It is used to display line of text/string that are passed as an argument.
- echo “string” >> file : It appends the string to the file given. If the file doesn’t exists it creates
it.

#### Others
- sudo : Allows a regular user to run the programs with the security privileges of a superuser or
root.
- apt : This command is used to install and add new packages.
- date : This command is used to show the current date and time.
- cal : Shows the calendar of the current month.
- whoami : This command displays the name with which you are logged in.


#### Head and Tail
```bash
head -n 10 file.txt  # Display the first 10 lines
tail -n 20 file.txt  # Display the last 20 lines
```


```bash
echo hello
# Prints hello

whoami
# Prints username

history
# shows list of all commands

# install packages
apt update
apt upgrade # upgrade system
apt install vim # example

apt remove nano # uninstall


# File System
# In Linux everything is a file!!


# Navigation
pwd # where we are

ls # list all items, by default multiple items per line
ls -1 # one item per line
ls -l # long listing, with details
ls -a # all files, including hidden

cd ./test # relative bath
cd /home/user # absolute path

cd .. # move one directory up

# contents of another dir without navigating there
ls /path/to/dir
ls /bin # contains programs that can be run! pwd, whoami, all commands there?


cd ~ # home dir of current user, "root" for root user


# Manipulation of files
mkdir test1 # create a dir

# Rename how?
mv test1 test2 # rename or move

touch hello.txt # create a file, just create
vim hello.txt # opens existing, or, creates and opens if new

touch t1.txt t2.txt # multiple files in one go

# rename file?
# same
mv test1.txt t.txt
# or move to some location
mv test1.txt /path/to/destination

# remove a file
rm test1.txt

# mutliple
rm test1.txt test2.txt
# or

rm test*
# remove all files starting with test

rm dir/ # remove dir, won't work
rm -r dir/ # recursively remove


# Text Editing
cat test1.text # output contents of file to terminal
# cat is used if file short, fits in one page

# more is used when long files
cat /etc/adduser.conf # very long file, no scrolling

more /etc/adduser.conf # space = next page, enter = one line at a time, q = exit/quit
# problem with more, only scroll down

# Less is used for this
# maynot be already present, if not, then install
apt install less

less /etc/adduser.conf  
# up, down arrows = scroll up/down
# space, enter same as more
# when done q


head -n 5 /etc/adduser.conf  # number of lines = 5, show top 5 lines
tail -n 5 /etc/adduser.conf  # number of lines = 5, show last 5 lines

# CHMOD
sudo chown root:root test.txt
# change ownership to root
chmod u+x test.txt
chmod og+x+w-r test.txt
chmod 777 test.txt
chmod 400 test.txt

# Redirecting output/stream
cat test1.txt > test2.txt

cat test1.txt test2.txt # reads both and prints, (concatanates)

cat test1.txt test2.txt > combined.txt

echo hello > hello.txt

ls -l /etc > list.txt


# Searching
grep Hello hello.txt # case-sensitive, so no o/p
grep hello hello.txt
grep -i Hello hello.txt # case-insensitive


# Find
find # w/o args, all files and dirs in current dir
find -type d

find -type f -name "test*"
find -type f -iname "test*" # insensitive case

# all files from root
find / -type f -name "*.py" # find all python files in the entirety of image 
find / -type f -name "*.py" > python_files.txt # find all python files in the entirety of image


# Chaining
mkdir t1 ; cd t1 ; echo done
# all get executed, one fails, other is done

mkdir t1 && cd t1 && echo done
# one fails, after it stops

mkdir t1 || echo "exists"
# if else


# Piping (Advd ?)
ls /bin | less
# Output of ls, and send it to less, so look at that list using less



# Processes
ps # list all running processes








```