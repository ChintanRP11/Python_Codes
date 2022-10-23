'''
File Input/Output
    -Opening Files --> Open file for doing operations on it
    -Closing Files --> Closing file is compulsory after completion of operations because files are loaded into memory
    -Write and Read Files
    -Create Files
    -Rename Files --> it is method from module 'os'
    -Delete Files --> it is method from module 'os'

Attributes of File Objects:
    -fileObject.closed = true if file closed
    -fileObj.mode = return mode with file name
    -fileObj.name = return file name
    -fileObj.softspace
    -fileObj.seek = use for changing offset of reading
    -fileObj.tell = use to check seek-offset value


function --> open(filename, accessmode)
    -Access Modes:
        - r = read only
        - rb = binary format of r
        - r+ = read and write ----> not overwrite file if exists
        - rb+ = binary format of r+
		
        - w = only write ----> overwrite file if exists and create if not exists
        - wb = binary format of w
        - w+ = both write and read ----> not overwrite file if exists
        - wb+ = binary of w+
		
		- a = append in file
        - ab = binary format of a
        - a+ = append and reading
        - ab+ = binary of a+
        

.read() --> to read file contents
.write() --> to write and append in file
'''

#Open Function
abc = open('fileops.txt', 'r')
print(abc.read())
print(abc.seek(10))
print(abc.tell())
print(abc.read(20))         #--> Read 20 characters or numbers
print(abc.tell())
abc.close()

new2 = open('fileops1.txt', 'w')
new2.write('This is new File for write ')
new2.close()

newf = open('fileops1.txt', 'a+')
newf.write('append completed')
newf.close()

print(newf.mode)
print(newf.name)

new3 = open('fileops1.txt', 'r+')
print(new3.read())
new3.write('This is append using r+')
new3.close()