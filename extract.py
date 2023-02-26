#! /usr/bin/env python3

from ldif import LDIFParser
from pprint import pprint
import sys
import hashlib

parser = LDIFParser(open(0, "rb"))

for dn, record in parser.parse():
    dn=str(dn)
    if dn.startswith("employeenumber=",0,16):
        uid=record["uid"][0]
        fgs=record["employeeNumber"][0]

        try:
            mail=record["mail"][0]
        except:
            mail=None

        try:
            ina=record["UCLInactif"][0]
        except:
            ina=None

        if mail is not None and ina is None:
            try:
                _fours=sorted([int(_f) for _f in record["UCLFournisseur"]])
                _nfour=0
                for four in _fours:
                    if four in [1, 2, 3, 8]:
                        _nfour = _nfour + 1
                if _nfour > 0:
                    hash=hashlib.md5(mail.encode("ascii")).hexdigest()
                    _upass=record["userPassword"]
                    for _pass in _upass:
                        print("u" + hash[4:12], mail, uid, fgs, _pass, _fours)
            except:
                pass

sys.exit(0)
