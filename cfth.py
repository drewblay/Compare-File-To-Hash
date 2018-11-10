#!/usr/bin/env python3
import argparse
import subprocess
import sys
from pathlib import Path

parser = argparse.ArgumentParser(description="CFTH (Compare File To Hash)")
parser.add_argument('--digest', help="The hash digest. Valid options: md5sum, sha1sum, sha224sum, sha256sum, sha512sum")
parser.add_argument('--file', help="The file you want to check")
parser.add_argument('--hash', help="The hash you want to compare")
args = parser.parse_args()

if len(sys.argv) == 1: 
	parser.print_help()
	sys.exit(1)

hash_digest = args.digest.lower()
file_to_hash = Path(args.file)
hash_to_check = args.hash.lower()

if hash_digest != "md5sum" and hash_digest != "sha1sum" and hash_digest != "sha224sum" and hash_digest != "sha256sum" and hash_digest != "sha512sum":
    print("Not a valid hash digest, see --help for list of valid values.")
    sys.exit(1)
elif file_to_hash.is_file() == False:
    print("{} is not a file.".format(file_to_hash))
    sys.exit(1)
else:
    file_hash = subprocess.run([hash_digest, file_to_hash], stdout=subprocess.PIPE)
    file_hash = str(file_hash.stdout).split(' ')[0]
    file_hash = file_hash[2:]

print("----------")
print("Hash of file: {}".format(file_hash))
print("Hash to check: {}".format(hash_to_check))
print("Hashes are the same: {}".format(file_hash == hash_to_check.lower()))
print("----------")
