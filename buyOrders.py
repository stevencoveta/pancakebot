import ray
from web3 import Web3
import json
import time
import datetime
import requests 
from web3.middleware import geth_poa_middleware
import pandas as pd
from datetime import datetime
import pickle


infura_url = "input wss infura url"

w3 = Web3(Web3.HTTPProvider(infura_url))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
f = open("/Users/steven/Desktop/jspkswap/python_swaps/abi.json")
abi = json.load(f)

       
caller = "caller address"
private_key = "caller private metamask key"  # To sign the transaction

# Initialize address nonce
nonce = w3.eth.getTransactionCount(caller)
# Initialize contract ABI and address
contract_address = "0x18B2A687610328590Bc8F2e5fEdDe3b582A49cdA"
# Create smart contract instance
contract = w3.eth.contract(address=contract_address, abi=abi)
Chain_id = w3.eth.chain_id

def BetBull(epoch):
    amount = w3.toWei("0.001","ether")
    call_function = contract.functions.betBull(epoch).buildTransaction({"value":amount,"from": caller,"chainId": Chain_id,"nonce": nonce,"gasPrice":8*10**9})
    signed_tx = w3.eth.account.sign_transaction(call_function, private_key=private_key)
    send_tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(send_tx)
    print(tx_receipt)

def BetBear(epoch):
    amount = w3.toWei("0.001","ether")
    call_function = contract.functions.betBear(epoch).buildTransaction({"value":amount,"from": caller,"chainId": Chain_id,"nonce": nonce,"gasPrice":8*10**9})
    signed_tx = w3.eth.account.sign_transaction(call_function, private_key=private_key)
    send_tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(send_tx)
    print(tx_receipt)

#BetBull(126350)
