# Compare File To Hash
So you downloaded a file and see that the publisher listed the files hash. You could check the file's hash and compare it to the onle listed on the site, but meh, who has time for that? It's probably fine, right? 

With cfth (compare file to hash)  you canquickly check the files hash to the hash provided by the publisher. 

Should work on any Linux distro, BSD distro, and MacOS.

### Requires:
Python 3

### Usage:
```
cfth.py [digest] [file] [hash]
```

### Supported hash digests:
* md5
* sha256
* sha512
* sha1
* sha224

### Examples:

###### Run manually:
```
$ python3 cfth.py md5 README.md 795ce9c6e754d746225ad1352aa7bf55
----------
Hash of file: 795ce9c6e754d746225ad1352aa7bf55
Hash to check: 795ce9c6e754d746225ad1352aa7bf55
Hashes match: True
----------
```

###### Make executable:
If you use this method you won't have prefix the command with python3, however you will have to be in the directory where cfthy.py resides.
```
$ chmod +x cfth.py
$ ./cfth.py md5 README.md 795ce9c6e754d746225ad1352aa7bf55
----------
Hash of file: 795ce9c6e754d746225ad1352aa7bf55
Hash to check: 795ce9c6e754d746225ad1352aa7bf55
Hashes match: True
----------
```

###### Make executable and make availbe globally:
If you use this method you can just call cfth from anywhere.
```
$ chmod +x cfth.py
$ sudo ln -s cfth.py /usr/local/bin/cfth
$ cfth md5 README.md 795ce9c6e754d746225ad1352aa7bf55
----------
Hash of file: 795ce9c6e754d746225ad1352aa7bf55
Hash to check: 795ce9c6e754d746225ad1352aa7bf55
Hashes match: True
----------
```
