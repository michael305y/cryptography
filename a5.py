from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

# Generate a random 256-bit key
key = get_random_bytes(32)
IV = get_random_bytes(12)

# The plain text to encrypt
plain_text_name = 'PONGSIN POOSANKAM'

count = 0

while count <= 5:
    # Encrypt the plain text
    cipher = AES.new(key, AES.MODE_GCM)
    cipher.update(b64decode('VGhpc0lzU2ltcGxlMjU2Qml0QVNDSUlLZXlPZkNNS0w='))
    cipher_text, tag = cipher.encrypt_and_digest(bytes(plain_text_name, 'utf-8'))

    # The encrypted message
    encrypted_message = b64encode(cipher.nonce + cipher_text + tag).decode('utf-8')

    print('Encrypted Message:', encrypted_message)

    count += 1