############### READ FROM FILE (BINARY) ######################

with open("sample.txt",'bw') as bin_file: #bw -> binary write
    for i in range(15):
        bin_file.write(bytes([i])) #bytes used for converting to byte object. non byte like is not allowed in binary mode

with open("sample.txt", 'br') as binFile: #br -> binary read
    for b in binFile:
        print(b)

a = 65535 # FF FE -> 2 bytes
b = 65536 # 00 01 00 00 -> 4 bytes
c = 2998302 # 02 2D C0 1E

with open("sample.txt",'bw') as bin_file:
    bin_file.write(a.to_bytes(2,'big')) # 2 -> 2 bytes, big -> most significant byte in start, little -> least significnt byte in start. depends on CPU
    bin_file.write(b.to_bytes(4,'big')) # 4 -> 4 bytes
    bin_file.write(c.to_bytes(4,'big'))
    bin_file.write(c.to_bytes(4,'little'))

with open("sample.txt", 'br') as binFile:
    x1 = int.from_bytes(binFile.read(2), 'big')
    x2 = int.from_bytes(binFile.read(4), 'big')
    x3 = int.from_bytes(binFile.read(4), 'big')
    x4 = int.from_bytes(binFile.read(4), 'little')
    x5 = int.from_bytes(binFile.read(4), 'big') #altering the format from actual
    print("{} {} {} {} {}".format(x1,x2,x3,x4,x5))



##################### USE OF PICKLE LIBRARY #########################

import pickle

album = ('Title', 'Singer', 2014, ((1, 'Track 1'), (2, 'Track 2')), 'somevalue')

with open("sample.txt",'bw') as pickleFile:
    pickle.dump(album, pickleFile)
    pickle.dump(299786, pickleFile)

# we can use protocol to dump these data
# protocol ranges in 0,1,2,3,4 with 4 as highest. Default is 3 for python 3.
#    --> pickle.dump(299786, pickleFile, protocol=0)
#    --> pickle.dump(299786, pickleFile, protocol=pickle.HIGHEST_PROTOCOL)
#    --> pickle.dump(299786, pickleFile, protocol=pickle.DEFAULT_PROTOCOL)

with open("sample.txt",'br') as pickleFile:
    album2 = pickle.load(pickleFile)
    num2 = pickle.load(pickleFile)

print(album2)
print(num2)


#use pickle to load system command. This will delete the sample.txt file in current location
pickle.loads(b"cos\nsystem\n(S'del sample.txt'\ntR.") #for windows, for mac/linux, replace del with rm


