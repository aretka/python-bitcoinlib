from bitcoin.rpc import RawProxy

p = RawProxy()

tx_id = raw_input('Enter transaction id: ')
raw_tx = p.getrawtransaction(tx_id)
decoded_tx = p.decoderawtransaction(raw_tx)

#calculating total output value
output_value = 0
for output in decoded_tx['vout']:
    output_value = output_value + output['value']

#calculating total input value
input_vouts = []
input_tx_ids = []
for inputs in decoded_tx['vin']:
    input_vouts.append(inputs['vout'])
    input_tx_ids.append(inputs['txid'])

input_index = 0
input_value = 0
for inputs in input_tx_ids:
    raw_tx = p.getrawtransaction(inputs)
    decoded_tx = p.decoderawtransaction(raw_tx)
    input_value = input_value + decoded_tx['vout'][input_vouts[input_index]]['value']
    input_index +=1

#calculating fee
fee = input_value - output_value
print("Transaction fee:  " + str(fee))
