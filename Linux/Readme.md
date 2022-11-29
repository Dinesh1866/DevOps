# Linux

## Linux Commands

ls - list files and directories
ls -l - list files and directories in long format
ls -a - list all files and directories including hidden files
ls -la - list all files and directories in long format including hidden files
ls -lh - list files and directories in long format with human readable file sizes
ls -lha - list all files and directories in long format with human readable file sizes including hidden files

cd - change directory
cd .. - change directory to parent directory
cd ~ - change directory to home directory
cd / - change directory to root directory

pwd - print working directory

mkdir - make directory
mkdir -p - make parent directories as needed
mkdir -m - make directory with specific permissions
mkdir folder1 folder2 folder3 - make multiple directories
mkdir folder1/folder2/folder3 - make nested directories

rmdir - remove empty directory
rmdir -p - remove parent directories as needed
rmdir folder1 folder2 folder3 - remove multiple directories
rmdir folder1/folder2/folder3 - remove nested directories

rm - remove file
rm -r - remove directory and all its contents
rm -f - force remove file
rm -rf - force remove directory and all its contents
rm -i - prompt before removing each file
rm -v - explain what is being done
rm -p - remove parent directories as needed
rm -f file1 file2 file3 - remove multiple files
rm -rf folder1 folder2 folder3 - remove multiple directories
rm -rf folder1/folder2/folder3 - remove nested directories
rm -r * - remove all files and directories in current directory
rm -r .* - remove all hidden files and directories in current directory
rm -r *.ext - remove all files with specific extension in current directory
rm -r *.ext1 *.ext2 *.ext3 - remove all files with specific extensions in current directory
rm -r *./ - remove all files and directories in current directory except the current directory

cp - copy file
cp -r - copy directory and all its contents
cp -i - prompt before overwriting
cp -v - explain what is being done
cp source_file destination_file - copy file
cp source_file1 source_file2 source_file3 destination_folder - copy multiple files to a folder
cp source_file1 source_file2 source_file3 destination_folder/ - copy multiple files to a folder
cp source_file1 source_file2 source_file3 destination_folder/new_file_name - copy multiple files to a folder with new file names
> copy will not overwrite the destination file if it already exists

mv - move file
mv file1 file2 - rename file1 to file2
mv file1 file2 file3 destination_folder - move multiple files to a folder
mv file1 file2 file3 destination_folder/ - move multiple files to a folder
mv file1 file2 file3 destination_folder/new_file_name - move multiple files to a folder with new file names

touch - create file
touch file1 file2 file3 - create multiple files
> touch will not overwrite the destination file if it already exists and we should give extension to the file

cat - concatenate files and print on the standard output
cat file1 file2 file3 - concatenate multiple files and print on the standard output
cat file1 file2 file3 > new_file - concatenate multiple files and write to new_file
cat file1 file2 file3 >> new_file - concatenate multiple files and append to new_file
> cat will overwrite the destination file if it already exists and this will show the content of the file in the terminal


### Linux File System

#### Linux File System Hierarchy

```bash
# Linux File System Hierarchy
# /bin -> Contains essential commands for all users
# /boot -> Contains files required to boot the system
# /dev -> Contains device files
# /etc -> Contains system configuration files
# /home -> Contains home directories for users
# /lib -> Contains libraries required by the binaries in /bin and /sbin
# /media -> Contains mount points for removable media
# /mnt -> Contains mount points for temporary file systems
# /opt -> Contains optional add-on application software packages
# /proc -> Contains information about processes
# /root -> Contains home directory for the root user
# /sbin -> Contains essential system binaries
# /srv -> Contains data for services provided by the system
# /sys -> Contains information and configuration for the system
# /tmp -> Contains temporary files
# /usr -> Contains read-only user data
# /var -> Contains variable data
```

#### Linux File System Hierarchy Standard

```bash
# Linux File System Hierarchy Standard
# /bin -> Essential command binaries
# /boot -> Static files of the boot loader
# /dev -> Device files
# /etc -> Host-specific system-wide configuration files
# /home -> User home directories
# /lib -> Essential shared libraries and kernel modules
# /media -> Mount points for removable media
# /mnt -> Mount points for temporary file systems
# /opt -> Add-on application software packages
# /proc -> Virtual file system
# /root -> Home directory for the root user
# /sbin -> Essential system binaries
# /srv -> Data for services provided by the system
# /sys -> Virtual file system
# /tmp -> Temporary files
# /usr -> Read-only user data
# /var -> Variable data
```
