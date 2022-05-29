import json
import requests

wallet_address = 'OIMI5ZYU5XSSNK23VTOJNGBVT7AS5ME7TOFD76BKPRJJGXSKH2QU2V53FU'

class Tx:

	  def __init__(self, tx_type, asset_id, amount, fee):

	  	    self.tx_type = tx_type
	  	    self.asset_id = asset_id
	  	    self.amount = amount
	  	    self.fee = fee

	  def details():

	  	print("ID: "+self.asset_id+" AMT: "+self.amount+" FEE: "+self.fee)

response = requests.get("https://algoindexer.algoexplorerapi.io/v2/accounts/OIMI5ZYU5XSSNK23VTOJNGBVT7AS5ME7TOFD76BKPRJJGXSKH2QU2V53FU/transactions")
todos = json.loads(response.text)
#print(json.dumps(todos['transactions'][3],sort_keys=True,indent=2))

tx_list = []

for tx in todos['transactions']:

	if(tx['tx-type'] == "axfer"):
		#print(tx.keys())
		details = tx['asset-transfer-transaction']	
		#print(details.keys())
		tx_list.append(Tx(tx['tx-type'],details['asset-id'],details['amount'],tx['fee']))
	elif(tx['tx-type'] == "pay"):
		payment = tx['payment-transaction']
		if(payment['reciever'] == wallet_address)
		tx_list.append(Tx(tx['tx-type'],0,tx['payment-transaction']['amount'],tx[]))

#for tx in tx_list:
	#print("ID: "+str(tx.asset_id)+" AMT: "+str(tx.amount)+" FEE: "+str(tx.fee))

