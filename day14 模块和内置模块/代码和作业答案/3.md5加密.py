"""
sssssdff
"""
import os
import sys
import random
import hashlib

import requests
import openpyxl

from commons.utils import encrypt



def md5(origin, salt="ljapsdiukqhjpoifjas;dkfhjpoaisjf;akj;dlf"):
    hash_object = hashlib.md5(salt.encode('utf-8'))
    hash_object.update(origin.encode('utf-8'))
    result = hash_object.hexdigest()
    return result


