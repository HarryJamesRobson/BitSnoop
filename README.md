# BitSnoop
Command line program for the analysis of a Bitcoin address.

## Usage:
BitSnoop can be run in a command line on a device with [Python](https://www.google.com) with the filename, a choice of '--es', '--bs' or '--help' and a target Bitcoin address. '--bs' (basic search) provides the balance, number of transactions, all the addresses within one hop of the target address and all addresses within one hop which match all specified addresses in the 'addresses_of_interest.txt' file. '--es' (extensive search) provides the balance, number of transactions, all transactions within a user specified amount of hops and all of those addresses which match those in the 'addresses_of_interest.txt' file. (Extensive snoop is currently under development and will be released within 2 weeks)

#### Example:
    BitSnoop.py --bs 1GyJS5JeQMKm8zVcbwp6XUQCukrABV8Fts
    
You will then be prompted to provide an api code. This is not required unless you are making a request on an address with an extremely large number of transactions or lots of requests on different addresses. To request an api code, click [here](https://api.blockchain.info/customer/signup).

## Other:
This program was written by Harry Robson. If you wish to ask any questions or help with its production in any way, please contact me. If this project comes in handy and you want to make a donation, my Bitcoin address is: 1GyJS5JeQMKm8zVcbwp6XUQCukrABV8Fts
