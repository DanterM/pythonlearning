import os

def new():
    os.chdir("/Users/Jarvis/Desktop")
    f = open("filename.txt",'ab')
    testnote = 'private String username'
    f.write(testnote.encode('utf-8'))
    f.close()
pass

new()

