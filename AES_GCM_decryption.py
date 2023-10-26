"""
========= Decrypts a message using AES-GCM-256 encryption==================

This code decrypts a message that was previously encrypted using AES-GCM-256 encryption. 
It takes a base64-encoded key, IV, and ciphertext, and decrypts the message to obtain the plain text.

Usage:
1. Provide a base64-encoded key, IV, and ciphertext.
2. Decode the key, IV, and ciphertext to obtain binary data.
3. Extract the Initialization Vector (IV), ciphertext, and authentication tag from the binary data.
4. Create a new cipher object with the key, IV, and AES-GCM mode.
5. Decrypt the ciphertext and verify the authentication tag(aka MAC)
6. Print the decrypted message.

Example:

    import base64
    from Crypto.Cipher import AES

    key_base64 = "VGhpc0lzU2ltcGxlMjU2Qml0QVNDSUlLZXlPZkNNS0w="
    iv_and_ciphertext_base64 = "e/2s4fv6PVBdrW715VQ7sOJqiQikt6V6Ee1bzbb6k7GJXoERs7XRUJnFaA=="

    key = base64.b64decode(key_base64)
    iv_and_ciphertext = base64.b64decode(iv_and_ciphertext_base64)

    # Extract IV, ciphertext, and authentication tag

    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
    plain_text = cipher.decrypt_and_verify(ciphertext, auth_tag)

    print("Decrypted Message:", plain_text.decode('utf-8'))

PS: all the sleep() and print() stmsts are optional and can be removed, was just using for testing purposes
"""


import base64
from time import sleep
from Crypto.Cipher import AES


print('Converting base64_encoded string into byte format')
sleep(1)

# Convert base64-encoded key, IV, and ciphertext to binary
base64_key_string = "VGhpc0lzU2ltcGxlMjU2Qml0QVNDSUlLZXlPZkNNS0w="
base64_byte_key = base64.b64decode(base64_key_string)   # convet key to bytes
print(f'length of key is {len(base64_byte_key)} bytes')

enc_msg = "e/2s4fv6PVBdrW715VQ7sOJqiQikt6V6Ee1bzbb6k7GJXoERs7XRUJnFaA==" 
byte_enc_msg = base64.b64decode(enc_msg)     # to bytes
print(f'lenth of byte enc msg is {len(byte_enc_msg)} bytes')

# Split the ciphertext into three parts.
iv = byte_enc_msg[:12]   # 96 bits which is alos the nonce
ciphertext = byte_enc_msg[12:-16]
auth_tag = byte_enc_msg[-16:]   # 128-bit MAC

print('Creating a new cipher block for decryption')
sleep(1)
decrypting_cipher = AES.new(base64_byte_key, AES.MODE_GCM, nonce=iv)  # create a new decrypting cipher object

# colors
GREEN_COLOR = "\033[32m"  # ANSI escape sequence for green color
RESET_COLOR = "\033[0m"

# Verify the authentication tag
try:
    print('Starting to decrypt')
    sleep(1)
    print('Verifying....')
    plain_text = decrypting_cipher.decrypt_and_verify(ciphertext, auth_tag)
    sleep(1)
    print("Decryption successful!")
    # print("Decrypted Message:", plain_text.decode('utf-8'))    # simple one without color
    print(f"Decrypted Message:  {GREEN_COLOR} {plain_text.decode('utf-8')} {RESET_COLOR}")

except ValueError:
    print("Decryption failed - authentication tag mismatch.")
