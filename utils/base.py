from random import randint
import string
import os
import time
from requests import request


class IGUtils(object):
    
    @staticmethod
    def base36(x: int, base: int) -> str:
        base_36 = string.digits + string.ascii_letters

        if x < 0:
            sign = -1
        elif x == 0:
            return base_36[0]
        else:
            sign = 1
        x *= sign
        digits = []
        while x:
            digits.append(base_36[x % base])
            x = x // base
        if sign < 0:
            digits.append("-")
        digits.reverse()
        return "".join(digits)
    
    
    @staticmethod
    def encrypt_password(password: str) -> str:
        return f"#PWD_INSTAGRAM_BROWSER:0:{int(time())}:{password}"
    
    @staticmethod
    def __x_mid() -> str:
        return "".join([IGUtils.base36(randint(2**29, 2**32), 36) for _ in range(8)])


class IgEncryptions(): # Idk how long his apis would work & Credits to godxgamer for the api.
    @staticmethod
    def _igapp(password: str, version: int) -> str:
        try:
            return request("GET", "http://128.140.99.16:5634/api/pass_enc/?p={}&v={}&m=igapp".format(password, version)).json()['password']
        except:
            return False
    
    @staticmethod
    def __webenc(password: str, version: int) -> str:
        try:
            return request("GET", "http://128.140.99.16:5634/api/pass_enc/?p={}&v={}&m=igweb".format(password, version)).json()['password']
        except:
            return False
    
