"""Import configuration file for Zerodha, an Indian stock broker and  ICICI Bank, a bank in India .
This script is heavily based on the script config.py  by Matt Terwilliger. 
Original script can be found here https://gist.github.com/mterwill/7fdcc573dc1aa158648aacd4e33786e8
Added SBI, RKSV and ETrade in V0.2
Added KGI in V0.3
Made further changes to KGI in V0.4 to handle dividends
Added iOCBC handling in V0.5
Added IOB in V0.6
"""
__copyright__ = "Copyright (C) 2020  Prabu Anand K"
__license__ = "GNU GPLv3"
__Version__ = "0.6"

import os, sys

# beancount doesn't run from this directory
sys.path.append(os.path.dirname(__file__))

# importers located in the importers directory
from importers.icici import icici
from importers.sbi import sbi
from importers.zerodha import zerodha
from importers.rksv import rksv
from importers.etrade import etrade
from importers.kgi import kgi
from importers.iocbc import iocbc
from importers.iob import iob
from importers.kvb import kvb

# The 7875 can be the last four character of your ICICI savings account. By suitably changing you can import from any ICICI account.
# All the six accounts i.e Assets:IN:Investment:ILFSSS etc must be declared already in your my.beancount file, to make use of this.
#

CONFIG = [
    icici.IciciBankImporter('Assets:IN:ICICIBank:Savings', '1585'),
    sbi.SBIImporter('Assets:IN:SBI:Savings', '8169'),
    iob.IOBImporter('Assets:IN:IOB:Savings:Aniruth', '3319'),
    iob.IOBImporter('Assets:IN:IOB:Savings:Aadhirai', '3320'),
    iob.IOBImporter('Assets:IN:IOB:Savings:Prabu', '3286'),
    kvb.KVBImporter('Assets:IN:KVB:Savings', '0880'),

    zerodha.ZerodhaImporter("INR",
                        "Assets:IN:Investment:Zerodha",
                        "Assets:IN:Investment:Zerodha:Cash",
                        "Income:IN:Investment:Dividend:{}",
                        "Income:IN:Investment:PnL:{}",
                        "Expenses:Financial:Fees:Zerodha",
                        "Assets:IN:ICICIBank:Savings"),

    rksv.RKSVImporter("INR",
                        "Assets:IN:Investment:RKSV",
                        "Assets:IN:Investment:RKSV:Cash",
                        "Income:IN:Investment:Dividend:{}",
                        "Income:IN:Investment:PnL:{}",
                        "Expenses:Financial:Fees:RKSV",
                        "Assets:IN:ICICIBank:Savings"),

    etrade.ETradeImporter("USD",
                        "Assets:US:Investment:ETrade",
                        "Assets:US:Investment:ETrade:Cash",
                        "Income:US:Investment:Dividend:{}",
                        "Income:US:Investment:PnL:{}",
                        "Expenses:Financial:Fees:ETrade",
                        "Income:US:Interest:ETrade"),

    kgi.KGIImporter("THB",
                        "Assets:TH:Investment:KGI",
                        "Assets:TH:Investment:KGI:Cash",
                        "Income:TH:Investment:Dividend:{}",
                        "Income:TH:Investment:PnL:{}",
                        "Expenses:Financial:Fees:KGI",
                        "Income:TH:Interest:KGI",
                        "Expenses:Financial:Fees:TSD",
                        "Assets:SG:Investment:DBS:Savings:Prabu",
                        "Expenses:TH:WithholdingTax:{}"),
    
    iocbc.IocbcImporter("SGD",
                        "Assets:SG:Investment:IOCBC",
#Assets:SG:Investment:IOCBC:Cash
#Assets:SG:Investment:CPF:CPFIS:Cash
#Assets:SG:Investment:SRS:Cash                             
                        "Assets:SG:Investment:IOCBC:Cash",
                        "Income:SG:Investment:Dividend:CPFIS:{}",
                        "Income:SG:Investment:PnL:{}",
                        "Expenses:Financial:Fees:IOCBC",
                        "Income:SG:Interest:IOCBC",
                        "Assets:SG:Investment:CPF:CPFIS:Cash"),
#Assets:SG:Investment:CPF:CPFIS:Cash
#Assets:SG:Investment:SRS:Cash
#Assets:SG:Investment:DBS:Savings:Prabu    
]

