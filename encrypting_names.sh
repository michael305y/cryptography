#! /bin/bash/

# Your plaintext
plaintext="PONGSIN POOSANKAM"

# Your 256-bit base64 key
key="VGhpc0lzU2ltcGxlMjU2Qml0QVNDSUlLZXlPZkNNS0w="

# Generate a random 96-bit IV (Initialization Vector)
iv=$(openssl rand -hex 12)

# Encrypt the plaintext using AES-GCM-256
encrypted_data=$(echo -n "$plaintext" | openssl enc -aes-256-gcm -a -A -iv "$iv" -K "$(echo -n "$key" | base64 -d)")

# Extract the ciphertext and authentication tag from the result
ciphertext="${encrypted_data%%:*}"
tag="${encrypted_data##*:}"

# Print the IV, ciphertext, and tag in base64 encoding
echo "IV: $iv"
echo "Ciphertext: $ciphertext"
echo "Tag: $tag"
