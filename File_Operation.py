
# Syntax ---file object = open(file_name [, access_mode][, buffering])


'''with open("/Users/apple/PycharmProjects/Analytics_Event/File_Operation.txt","wb") as filename :

    #print(filename.seekable())

    print(filename.tell())

    print(filename.seek(100))

    filename.write(b'a') # tell to python we are adding binary data

    print(filename.fileno())

    print(filename.mode)

    print(filename.name)

    #filename.


with open("/Users/apple/PycharmProjects/Analytics_Event/File_Operation.txt","rb") as filename :

    #print(filename.seekable())

    print(filename.tell())

    print(filename.seek(100))

    print(filename.readlines()) # tell to python we are adding binary data

    print(filename.fileno())

    print(filename.mode)

    print(filename.name)

'''

with open("/Users/apple/PycharmProjects/Analytics_Event/File_Operation.txt","ab") as filename :

    #print(filename.seekable())

    print(filename.tell())

    print(filename.seek(100))

    filename.write(b'AMIT SAXENA') # tell to python we are adding binary data

    print(filename.fileno())

    print(filename.mode)

    print(filename.name)

    #filename.


