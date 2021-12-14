#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 02:22:49 2021

@author: izuchukwumatthew
"""

import requests

"""Get Request for basic summmary"""

jsonresponse = requests.get('https://api.quarantine.country/api/v1/summary/latest')
jsonresponse.status_code
jsonresponse.json()

"""Get request"""

Jsonresponse2 = requests.get('https://api.quarantine.country/api/v1/spots/week?region=usa')
Jsonresponse2.status_code
Jsonresponse2.json()