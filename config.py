#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6005960715:AAHB9INP_OzN_b4gZzKeRMOM--X8H6wfkAc")
    API_ID = int(os.environ.get("API_ID", "27881923"))
    API_HASH = os.environ.get("API_HASH", "79abda5e46a51fc0dce1313f2548ce19")
    

