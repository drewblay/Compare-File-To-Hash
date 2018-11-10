# Compare File To Hash
So you downloaded a file and see that file hash digest listed next to it. You could check the file's hash and compare it to the onle listed on the site, but meh, who has time for that? It's probably fine, right? 

With cfth you canquickly check the files hash to the hash provided by the publisher. 

Should work on any Linux distro, BSD distro, and MacOS.

Requires:
Python 3

Usage:
`cfth.py --digest= --file= --hash=`

Supported hash digests:
 md5sum
 sha1sum
 sha224sum
 sha256sum
 sha512sum
