#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sabae
import requests
import json

url = 'https://www.lib006.nexs-service.jp/sabae/webopac/searchdetail.do?biblioid=92344'
r = requests.get(url)
print json.dumps(sabae.html(r.content, url,'1.3.0'), ensure_ascii=False, indent=2)
