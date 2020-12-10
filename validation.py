from bitcoin.rpc import RawProxy
import hashlib

p = RawProxy()

blockHash = raw_input('Iveskite bloko hasha: ')

def littleEndian(data):
        changedData = ""
        length = len(data)/2
        for i in range(0, length):
                swapData = data[2*i] + data[2*i+1]
                changedData = swapData + changedData
        return changedData

block = p.getblock(blockHash)
header_hex = (
        littleEndian(block["versionHex"]) +
        littleEndian(block["previousblockhash"]) +
        littleEndian(block["merkleroot"]) +
        littleEndian('{:08x}'.format(block["time"])) +
        littleEndian(block["bits"]) +
        littleEndian('{:08x}'.format(block["nonce"]))
    )
header_bin = header_hex.decode('hex')
hashCheck = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
if hashCheck[::-1].encode('hex_codec')== block['hash']:
    print("Hash is validated")
else:
    print("Hashas is not validated")
print("Hash being checked:\n" +
        str(hashCheck[::-1].encode('hex_codec')) +
        "\nReal block hash: \n" +
        str(block['hash']))
