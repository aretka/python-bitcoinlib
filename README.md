# Python-bitcoinlib implementation

Programos atliktos naudojant python-bitcoinlib biblioteką

## Transaction fee programos veikimas

Programa nuskaito įvestos transakcijos hash'ą. Suskaičiuoja išvedamų bitcoinų skaičių (output_value) paprasčiausiai einant per transakcijos 'vout' objektus ir sumuojant 'value' vertes. Tada skaičiuojamas įvesties (input_value) suma: pirma pereinama per visus input objektus ir sudedama į input_vouts masyvą input['vout'], o į input_tx_ids sudedama input['txid'], tada pereinama per kiekvieną įvesties transakcijų id (input_tx_ids), paimama raw transaction, ji dekoduojama bei paimama tos transakcijos output pagal atitinkama vout iš input_vouts masyvo. Mokęstis atspindi įvesties ir išvesties skirtumą.

## Validation programos veikimas

Programa sukuria header hex, kuris susidaro vykdant littleEndian funkciją elementams: versionHex, previousblockhash, merkleroot, time, bits, nonce, bei juos susumuojant. Tada dekoduojamas header_hex, bei hashCheck elementui prilyginamas sha256 hash'uotas header_hex ir tikrinama ar sukurtas hash'as prilygsta buvusiam.
