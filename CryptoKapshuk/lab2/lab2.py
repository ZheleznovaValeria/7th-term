from Crypto.Cipher import DES
from Crypto.Cipher import DES3
from Crypto import Random

with open('10.txt', 'r') as file:
	data = file.read()


iv = Random.new().read(DES3.block_size)

cipher_triple_des = DES3.new(
	bytes('ЖелезноваВалерия', 'windows-1251'), 
	DES3.MODE_CFB,
    iv
	)

cipher_des = DES.new(
	bytes('Железнов', 'windows-1251'), 
	DES.MODE_CFB,
    iv
	)

decrypt_triple_des = DES3.new(
	bytes('ЖелезноваВалерия', 'windows-1251'), 
	DES3.MODE_CFB,
    iv
	)

decrypt_des = DES.new(
	bytes('Железнов', 'windows-1251'), 
	DES.MODE_CFB,
    iv
	)

print('\n\nText: ', data)

triple = cipher_triple_des.encrypt(str.encode(data))
common = cipher_des.encrypt(str.encode(data))

print("\n\nDes")
print('\nEncrypted: ', common)
print('\nDecrypted: ', decrypt_des.decrypt(common))

print("\nTripleDes")
print('\nEncrypted: ', triple)
print('\nDecrypted: ', decrypt_triple_des.decrypt(triple))
