import math
from Cryptodome.PublicKey import RSA
from Cryptodome import Random
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Hash import SHA256

#open file
with open('10.txt', 'r') as file:
    data = file.read()


class RsaEncryption:
    #generating key pair
    @staticmethod
    def get_keys():
        random_generator = Random.new().read                            #define random generator
        key_pair = RSA.generate(1024, random_generator)                 #generate key pair
        private_key = key_pair.export_key('PEM').decode()               #get private key
        public_key = key_pair.publickey().export_key('PEM').decode()    #get public key

        return private_key, public_key

    #encrypting message
    @staticmethod
    def encrypt(key, message):
        message = message.encode()                                  #encode to UTF-8

        key = RSA.importKey(key)                                    #import key
        cipher = PKCS1_OAEP.new(key)                                #define PKCS1_OAEP cypher(Public Key Cryptography Standarts 1 Optimal Asymmetric Encryption Padding)
        encrypted = cipher.encrypt(message)                         #encrypt message with PKCS1_OAEP

        return encrypted

    #decrypting message
    @staticmethod
    def decrypt(key, encoded_message):                              
        key = RSA.importKey(key)                                    #import key
        decipher = PKCS1_OAEP.new(key)                              #define PKCS1_OAEP decypher
        decrypted = decipher.decrypt(encoded_message)               #decrypting

        return decrypted


class TranspositionCypher:
    @staticmethod
    def encrypt(key, message):
        ciphertext = [''] * key

        for col in range(key):
            pointer = col
            while pointer < len(message):
                ciphertext[col] += message[pointer]
                pointer += key

        return ''.join(ciphertext)

    @staticmethod
    def decrypt(key, encoded_message):
        numOfColumns = math.ceil(len(encoded_message) / key)
        numOfRows = key
        numOfShadedBoxes = (numOfColumns * numOfRows) - len(encoded_message)
        plaintext = [''] * numOfColumns
        col = 0
        row = 0

        for symbol in encoded_message:
            plaintext[col] += symbol
            col += 1
            if (col == numOfColumns) or (col == numOfColumns - 1
                                         and row >= numOfRows - numOfShadedBoxes):
                col = 0
                row += 1

        return ''.join(plaintext)


def main():
    transposition_key = 10 + (10 + 81) % 7                                     #width of table for transposition cypher
    hash_object = SHA256.new(data=data.encode())                               #computing hash
    print('\n\nSHA256: ', hash_object.hexdigest())

    encrypted_hash = TranspositionCypher.encrypt(                              #encrypt hash using transposition sypher
        transposition_key, hash_object.hexdigest())
    transposition_key = str(transposition_key)
    print('\nTransposition key: ', transposition_key)
    print('\nEncrypted hash: ', encrypted_hash)

    private_key, public_key = RsaEncryption.get_keys()                         #get keys
    encrypted_tr_key = RsaEncryption.encrypt(public_key, transposition_key)    #encrypt public key RSA key transposition key
    print('\nEncrypted transposition key: ', encrypted_tr_key)

    decrypted_tr_key = int(RsaEncryption.decrypt(                              #decrypt transposition key with public key RSA
        private_key, encrypted_tr_key).decode())
    print('\nDerypted transposition key: ', decrypted_tr_key)
    decrypted_hash = TranspositionCypher.decrypt(                              #decrypt hash with decrypted transposition key
        decrypted_tr_key, encrypted_hash)
    print('\nDecrypted hash: ', decrypted_hash)


if __name__ == "__main__":
    main()
