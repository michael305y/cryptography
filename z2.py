import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Base64-encoded key, IV, and ciphertext
key_base64 = "VGhpc0lzU2ltcGxlMjU2Qml0QVNDSUlLZXlPZkNNS0w="
iv_and_ciphertext_base64 = "e/2s4fv6PVBdrW715VQ7sOJqiQikt6V6Ee1bzbb6k7GJXoERs7XRUJnFaA=="

# Decode the base64 data
key = base64.b64decode(key_base64)
iv_and_ciphertext = base64.b64decode(iv_and_ciphertext_base64)

print(f'lenth of key is {len(key)} bytes')
print(f'lenth of byte enc msg is {len(iv_and_ciphertext)} bytes')

# Extract IV, ciphertext, and authentication tag
iv = iv_and_ciphertext[:12]  # 96 bits (12 bytes)
ciphertext = iv_and_ciphertext[12:-16]  # The rest is ciphertext
auth_tag = iv_and_ciphertext[-16:]  # 128 bits (16 bytes)

# Decrypt the ciphertext
cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
plain_text = cipher.decrypt_and_verify(ciphertext, auth_tag)

print("Decrypted Message:", plain_text.decode('utf-8'))
