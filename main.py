from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import configparser


config = configparser.ConfigParser(interpolation=None)
config.read('config.cfg')


'''
key_pair = RSA.generate(3072)

public_key = key_pair.public_key()

public_key_PEM = key_pair.public_key().exportKey().decode('ascii')
private_key_PEM = key_pair.exportKey().decode('ascii')

print(public_key_PEM)
print(private_key_PEM)
'''

def encrypt_message(public_key, message):
    encryptor = PKCS1_OAEP.new(public_key)
    encrypted_message = encryptor.encrypt(message)
    return encrypted_message

def decrypt_message(key_pair, encrypted_message):
    decryptor = PKCS1_OAEP.new(key_pair)
    message = decryptor.decrypt(encrypted_message)
    return message


key_pair = RSA.import_key(config.get('KEYS', 'private_key'))

encrypted_message = encrypt_message(key_pair.public_key(), 'message')
print(decrypt_message(key_pair, encrypted_message))
