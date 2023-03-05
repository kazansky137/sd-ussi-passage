#! /usr/bin/env python3

"""Extract useful data for 'passage' project from a LDIF file"""

import sys
import hashlib
from config import Config
from params import Params
from ldif import LDIFParser

PASS_SERVICE = "{SSHA}4iM5QyVhHf4x+pNHLVxMs9YMqEItP9dHskJEcQ=="

config = Config("ldap.conf")
params = Params(config)
params.add_argument("--fours")
params.parse()
FOURNISSEURS  = params.range('fours')


def _dn_process(dname, record):
    _dn = str(dname)
    if _dn.lower().startswith("employeenumber=", 0, 16):
        uid = record["uid"][0]
        fgs = record["employeeNumber"][0]

        try:  # "mail" attribute must exists
            mail = record["mail"][0]
        except KeyError:
            return

        if "UCLInactif" not in record:
            try:
                _upass = record["userPassword"]
            except KeyError:
                return
            _fours = sorted([int(_f) for _f in record["UCLFournisseur"]])
            _nfour = 0
            for four in _fours:
                if four in FOURNISSEURS:
                    _nfour = _nfour + 1
            if _nfour > 0:
                _h = hashlib.md5(mail.encode("ascii")).hexdigest()
                for _pass in _upass:
                    if _pass == PASS_SERVICE:
                        return
                    # print("u" + _h[4:12], mail, uid, fgs, _pass, _fours)
                    print(mail.lower(), _pass)


if __name__ == "__main__":

    with open(0, "rb") as _fh:
        parser = LDIFParser(_fh)
        for _dn, _rec in parser.parse():
            _dn_process(_dn, _rec)

sys.exit(0)
