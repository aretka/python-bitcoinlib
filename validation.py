from bitcoin.rpc import RawProxy
import hashlib

p = RawProxy()

#taking block hash input
blockHash = raw_input('Enter block hash: ')

# creating little endian function
def littleEndian(data):
        changedData = ""
        length = len(data)/2
        for i in range(0, length):
                swapData = data[2*i] + data[2*i+1]
                changedData = swapData + changedData
        return changedData

block = p.getblock(blockHash)
#calculating header_hex using function little endian and taking as inputs versionHex, previousblockhash, merkleroot, time, bits, nonce
#time and nonce have to be created into hex using format function
header_hex = (
        littleEndian(block["versionHex"]) +
        littleEndian(block["previousblockhash"]) +
        littleEndian(block["merkleroot"]) +
        littleEndian('{:08x}'.format(block["time"])) +
        littleEndian(block["bits"]) +
        littleEndian('{:08x}'.format(block["nonce"]))
    )
#header is decoded
header_bin = header_hex.decode('hex')

#creating hash using sha256 
hashCheck = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()

#checking manually created header hash and header hash which already exists
if hashCheck[::-1].encode('hex_codec')== block['hash']:
    print("Hash is validated")
else:
    print("Hashas is not validated")
print("Hash being checked:\n" +
        str(hashCheck[::-1].encode('hex_codec')) +
        "\nReal block hash: \n" +
        str(block['hash']))
