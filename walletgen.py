
from eth_account import Account
import json
# Generate a new random private key
private_key = Account.create().key.hex()  # Keep this safe!

# Encrypt it into a keystore file
password = "your_strong_password_here"  # Prompt securely in production
keystore = Account.encrypt(private_key, password)

# Save to file
with open("keystore.json", "w") as f:
    json.dump(keystore, f)

print(f"Keystore saved to 'keystore.json'. Address: {Account.from_key(private_key).address}")
