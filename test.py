def write_file(file_name):
    ptr=open(file_name,'w')
    ptr.write(data)
    ptr.close()
    
    
write_file('test.txt', "How are you.")
