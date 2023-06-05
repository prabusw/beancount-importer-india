"""Import configuration file for Zerodha, an Indian stock broker and  ICICI Bank, a bank in India .
This script is heavily based on the script config.py  by Matt Terwilliger. 
Original script can be found here https://gist.github.com/mterwill/7fdcc573dc1aa158648aacd4e33786e8
"""
__copyright__ = "Copyright (C) 2020  Prabu Anand K"
__license__ = "GNU GPLv3"
__Version__ = "0.1"

import os, sys

# beancount doesn't run from this directory
sys.path.append(os.path.dirname(__file__))

# importers located in the importers directory
from importers.icici import icici
from importers.sbi import sbi
from importers.zerodha import zerodha
from importers.rksv import rksv

# The 7875 can be the last four character of your ICICI savings account. By suitably changing you can import from any ICICI account.
# All the six accounts i.e Assets:IN:Investment:ILFSSS etc must be declared already in your my.beancount file, to make use of this.
#

CONFIG = [
    icici.IciciBankImporter('Assets:IN:ICICIBank:Savings', '7875'),
    sbi.SBIImporter('Assets:IN:SBI:Savings', '8169'),

    zerodha.ZerodhaImporter("INR",
                        "Assets:IN:Investment:ILFSSS",
                        "Assets:IN:Investment:Zerodha:Cash",
                        "Income:IN:Investment:Dividend",
                        "Income:IN:Investment:PnL",
                        "Expenses:Financial:Taxes:Zerodha",
                        "Assets:IN:ICICIBank:Savings"),

    rksv.RKSVImporter("INR",
                        "Assets:IN:Investment:RKSV",
                        "Assets:IN:Investment:RKSV:Cash",
                        "Income:IN:Investment:Dividend",
                        "Income:IN:Investment:PnL",
                        "Expenses:Financial:Taxes:RKSV",
                        "Assets:IN:ICICIBank:Savings"),
]

