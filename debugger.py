#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sabae
import pprint
import requests

r = requests.get('https://www.lib006.nexs-service.jp/sabae/webopac/searchdetail.do?biblioid=1491878')
x = sabae.mapping(r.content, '')
print x['status']

pprint.pprint(x)
