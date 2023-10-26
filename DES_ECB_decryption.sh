# decrypting files using DES-ECB
#! /bin/bash
 
plain_text=$(openssl enc -des-ecb -d -in cipher.bin -out plain_text.txt -K $(cat key.bin | xxd -p))

echo  "Lol, decrypted the cipher successfully, check for file named plain_tex in your directory"

# Checking the checksum
md5=$(md5sum plain_text.txt)

echo 'Now cheking the  checksum, please wait...'
sleep 2
echo  '........................'
sleep 1
echo '.....................'
sleep 1
echo '.........'
echo 'completed'

echo "MD5 checksum is: $md5"
