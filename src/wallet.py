from linecache import getline
from random import randint
from hashlib import sha256
from ecdsa import SigningKey, SECP256k1

def get_mnemonic(amount: int = 12) -> list[str]:
    indexes =  [randint(1, 2048) for _ in range(amount)] # Generate random indexes

    return [getline('../data/wordlist.txt', index).strip() for index in indexes]  # Get the words from the wordlist

def make_wallet():
    mnemonic = get_mnemonic()
    mnemonic_str = ' '.join(mnemonic)
    
    seed = sha256(mnemonic_str.encode()).digest()
    secp256k1_n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
    signin_key_int = int.from_bytes(seed, byteorder='big') % secp256k1_n

    
    signin_key = SigningKey.from_secret_exponent(signin_key_int, curve=SECP256k1)
    verifying_key = signin_key.get_verifying_key()

    addr = sha256(verifying_key.to_string()).hexdigest()

    return {
        'mnemonic': mnemonic_str,
        'address': addr,
        'private_key': signin_key.to_string().hex(),
        'public_key': verifying_key.to_string().hex()
    }
