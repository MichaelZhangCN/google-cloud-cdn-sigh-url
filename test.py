#!/usr/bin/env python
import datetime
import signurl

# https://www.epochconverter.com/
expire_ts = 1594189564
key_code = 'SBSNBdd57Makbbn1PlvzRw==' # head -c 16 /dev/urandom | base64 | tr +/ -_
key_name = 'michaelzhkey'

dingo_url = "http://35.241.61.244/1.txt"
dingo_url_prefix_1 = "http://35.241.61.244/cdn1"
dingo_url_prefix_2 = "http://35.241.61.244/cdn1/"

def test_sign_url():
    signurl.sign_url(
        dingo_url,
        key_name,
        key_code,
        datetime.datetime.utcfromtimestamp(expire_ts))

def test_sign_url_prefix():
    signurl.sign_url_prefix(
        dingo_url,
        dingo_url_prefix_1,
        key_name,
        key_code,
        datetime.datetime.utcfromtimestamp(expire_ts))

def test_sign_cookie():
    signurl.sign_cookie(
        dingo_url_prefix_2,
        key_name,
        key_code,
        datetime.datetime.utcfromtimestamp(expire_ts))

test_sign_url()
test_sign_url_prefix()
test_sign_cookie()