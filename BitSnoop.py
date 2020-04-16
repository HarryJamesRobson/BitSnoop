import argparse
import requests
import json

def get_one_hop(transactions):
    addr_list = []
    tx_count = 0
    for transaction in transactions:
        transaction = transactions[(tx_count)]
        inputs = transaction["inputs"]
        outs = transaction["out"]
        in_counter = 0
        out_counter = 0
        for input in inputs:
            input = inputs[(in_counter)]
            in_counter = in_counter+1
            addr_list.append(input['prev_out']['addr'])
        for out in outs:
            out = outs[(out_counter)]
            out_counter = out_counter=1
            addr_list.append(out['addr'])
        tx_count = tx_count+1

def get_address_balance(decoded_request):
    sat_balance = decoded_request["final_balance"]
    btc_balance = str(sat_balance/100000000)
    print("Balance: " + btc_balance)

def get_tx_count(decoded_request):
    tx_count = str(decoded_request["n_tx"])
    print("No. Transactions: " + tx_count)
    
def basic_snoop(address, api_code):
    print("Basic snoop in progress...")
    print("Address: " + (address))
    if api_code != "N/A":
        request = requests.get("https://blockchain.info/rawaddr/" + (address) + "?api_code=" + (api_code))
    else:
        request = requests.get("https://blockchain.info/rawaddr/" + (address))
    decoded_request = json.loads(request.text)
    transactions = decoded_request["txs"]
    get_address_balance(decoded_request)
    get_tx_count(decoded_request)
    get_one_hop(transactions)

BitSnoop = argparse.ArgumentParser(description="BitSnoop allows easy analysis of a Bitcoin address.")
BitSnoop.add_argument('address', action='store', type=str, nargs=1, help="Holds target Bitcoin address")
BitSnoop.add_argument('--bs', dest='basic_snoop', action='store_true', help="Basic snoop option")
BitSnoop.add_argument('--es', dest='extensive_snoop', action='store_true', help="Extensive snoop option")
args = BitSnoop.parse_args()

address_raw = str(args.address)
address = address_raw[2:-2]

use_api = input("Would you like to use an api key? (y/n) ")
if use_api == "y":
    api_code = input("Enter your api code: ")
else:
    api_code = "N/A"

if args.basic_snoop == True:
    basic_snoop(address, api_code)
elif args.extensive_snoop == True:
    extensive_snoop(address, api_code)
else:
    print("You must enter an option. Type --help for help.")

