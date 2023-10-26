from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode


# The key in base64 format
base64_key = "VGhpc0lzU2ltcGxlMjU2Qml0QVNDSUlLZXlPZkNNS0w="
key = b64decode(base64_key)

print(key)
print(len(key))

# The plain text to encrypt
plain_text_name = 'PONGSIN POOSANKAM'

count = 0

while count <= 5:
    IV = get_random_bytes(12)  # we generate a 96 bit IV which is now 12bytes to use for encryption
    # Encrypt the plain text
    cipher = AES.new(key, AES.MODE_GCM, IV)
    
    cipher_text, tag = cipher.encrypt_and_digest(bytes(plain_text_name, 'utf-8'))

    # print(cipher_text)  # just for testing
    # print(tag)

    # The encrypted message
    encrypted_message = b64encode(cipher.nonce + cipher_text + tag).decode('utf-8')
    
    print('Encrypted Message:', encrypted_message)

    count += 1
