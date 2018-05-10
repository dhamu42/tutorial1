import sys

def write_file(file_name, data):
    ptr=open(file_name,'w')
    ptr.write(data)
    ptr.close()
    
    
write_file('test.txt', sys.argv[1])
