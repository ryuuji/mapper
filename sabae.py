#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from bs4 import BeautifulSoup
import zenhan

data = u"""
320	a	一般	010	069
320	b	一般	070	134
5	a	一般	188	210
5	b	一般	210.0	210.4
6	a	一般	289	291.0
6	b	一般	291.0	294
7	a	一般	326	336
7	b	一般	336	364
8	a	一般	381	388
8	b	一般	389	426
9	a	一般	493.93	499
9	b	一般	500	527
10	a	一般	596	614
10	b	一般	615	653
11	a	一般	724	748
11	b	一般	748	760
12	a	一般	791	814
12	b	一般	815	908
13	a	一般	911.4	Fアケノ
13	b	一般	Fアサイ	Fウチダ
14	a	一般	Fサトウ	Fソネケ
14	b	一般	Fソノア	Fツジヒ
15	a	一般	Fフジタ	Fミンナ
15	b	一般	Fムコウ	Fヤマモ
16	a	一般	914.6	914.6
16	b	一般	915キ	916ヘ
17	a	一般	918.6ト	918.6ム
17	b	一般	918.6モ	928シ
18	a	一般	933ヒ	933ワ
18	b	一般	934	949
140	a	大活字	041	949
140	a	一般総記	014	014
140	a	一般	002	007
140	b	一般	134	158
141	a	一般	159	188
141	b	一般	210.4	222
142	a	一般	222	289
142	b	一般	295	310
143	a	一般	311	326
143	b	一般	365	369
144	a	一般	369	380
144	b	一般	427	483
145	a	一般	484	493.92
145	b	一般	527	588
146	a	一般	588	596
146	b	一般	653	699
147	a	一般	700ク	723
147	b	一般	760	778ハ
148	a	一般	778ハ	790
148	b	一般	908	910.2
149	a	一般	910.2	911.4
149	b	一般	Fウチダ	Fキタヤ
150	a	一般	Fキタユ	Fサトウ
150	b	一般	Fツジマ	Fニシオ
151	a	一般	Fニシカ	Fフジサ
151	b	一般	Fヤマモ	914.6エ
152	a	一般	914.6オ	914.6ト
152	b	一般	916ボ	918.6ワ
153	a	一般	918.6エ	918.6テ
153	b	一般	928チ	933キ
154	a	一般	933ク	933ヒ
154	b	一般	950	994
396	b	絵本	Eヤ	Eル
381	a	絵本	Eフ	Eマ
381	b	絵本	Eマ	Eモ
385	a	絵本	Eレ	Eワ
385	b	絵本
368	a	児童	94	95
367	b	児童	93マ	94
357	a	児童	93ト	93ホ
357	b	児童	93コ	93テ
406	a	児童	918	93ケ
406	b	児童	913ヤ	917
361	a	児童	913フ	913モ
361	b	児童	913ナ	913ヒ
407	a	児童	913シ	913ト
407	b	児童	913カ	913サ
408	a	児童	913ア	913オ
408	b	児童	82	912
408	b	児童洋書	YE	YE
409	a	児童	78	81
409	b	児童	66	77
412	a	児童	53	65
412	b	児童	48	52
413	a	児童	48	48
413	b	児童	45	47
369	a	児童	40	44
369	b	児童	37	39
371	a	児童	36	36
371	b	児童	31	35
372	a	児童	29	30
372	b	児童	28	28
373	a	児童	21	27
373	b	児童	15	20
374	a	児童	00	14
374	b	児童参考	R007	R999
"""


def callno_to_float(no):
    ret = 0
    x = 0
    tbl = u"アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲンジボダガギグパピプペポ"
    for word in tbl:
        no = re.sub(word, "%02d" % x, no)
        x += 1
    tmp_ = re.findall(u"^HF([0-9.]+)$", no)
    if len(tmp_) > 0:
        ret = float(tmp_[0]) + 1000000
        return ret
    tmp_ = re.findall(u"^H([0-9.]+)$", no)
    if len(tmp_) > 0:
        ret = float(tmp_[0]) + 2000000
        return ret
    tmp_ = re.findall(u"^R([0-9.]+)$", no)
    if len(tmp_) > 0:
        ret = float(tmp_[0]) + 3000000
        return ret
    tmp_ = re.findall(u"^S([0-9.]+)$", no)
    if len(tmp_) > 0:
        ret = float(tmp_[0]) + 4000000
        return ret
    tmp_ = re.findall(u"^E([0-9.]+)$", no)
    if len(tmp_) > 0:
        ret = float(tmp_[0]) + 5000000
        return ret
    tmp_ = re.findall(u"^W([0-9.]+)$", no)
    if len(tmp_) > 0:
        ret = float(tmp_[0]) + 6000000
        return ret
    tmp_ = re.findall(u"^F([0-9.]+)$", no)
    if len(tmp_) > 0:
        ret = float(tmp_[0]) / 100000000 + 913
        return ret

    tmp_ = re.findall(u"([0-9]{3})\.([0-9]+)", no)
    if len(tmp_) > 0:
        ret += float(tmp_[0][0] + "." + tmp_[0][1])
        return ret
    tmp_ = re.findall(u"([0-9]{3})([0-9]+)", no)
    if len(tmp_) > 0:
        ret += float(tmp_[0][0] + "." + tmp_[0][1])
        return ret
    tmp_ = re.findall(u"([0-9]{3})", no)
    if len(tmp_) > 0:
        ret += float(tmp_[0])
        return ret
    tmp_ = re.findall(u"([0-9]{2})", no)
    if len(tmp_) > 0:
        ret += float(tmp_[0])
        return ret
    return ret


tables = []
for params in data.splitlines():
    p = params.split('\t')
    if len(p) > 3:
        start = callno_to_float(p[3])
        end = callno_to_float(p[4])
        f = u'1階'
        if p[2] == u'絵本' or p[2] == u'紙芝居' or re.search(u'^児童', p[2]):
            f = u'2階'
        tmp = {
            'shelf_id': int(p[0]),
            'side': p[1],
            'place': p[2],
            'start': start,
            'end': end,
            'floor': f
        }
        tables.append(tmp)


def parse(place, no):
    for line in tables:
        tmp_float = callno_to_float(no)
        if re.search('^' + line['place'], place):
            if line['start'] <= tmp_float < line['end']:
                return line


def mapping(data_, url):
    # メッセージのパターン
    # ・貸出中です
    # ・本棚にあります
    # ・書庫にあります

    is_rent = False
    is_backyard = False
    is_other = False
    is_unknown = False

    soup = BeautifulSoup(data_, "lxml")

    stocks = []
    shelf_flags = []
    for tr in soup.find_all('tr'):
        td = tr.find_all('td', False)
        if len(td) == 6:
            libname = td[1].get_text().strip()
            place = td[3].get_text().strip()
            status = td[4].get_text().strip()
            if status == u"貸出中です":
                is_rent = True
                continue

            if libname != u"本館":
                is_other = True
                continue

            no = ''
            place = place.replace(u'（', '(').replace(u'）', ')')
            tmp_ = re.findall(u'\((.*)\)', place)
            if len(tmp_) > 0:
                if re.search('\.', tmp_[0]):
                    no = tmp_[0].replace(' ', '')
                else:
                    no = tmp_[0].replace(' ', '.', 1)
                    no = no.replace(' ', '')

                place = re.sub(u'\((.*)\)', '', place)
            no = zenhan.h2z(no, zenhan.KANA)

            if re.search(u"書庫|閉架", place):
                is_backyard = True
                continue

            if status == u"貸出できます" or status == u"帯出禁止":
                tana = parse(place, no)
                if tana is not None:
                    message = u"本棚にあります" + u"(" + place + "/" + no + u")"
                    message += u"【" + tana['side'] + u"面】"
                    if no not in shelf_flags:
                        stocks.append(
                            {'message': message, 'shelfId': tana['shelf_id'], 'floorId': 7, 'side': tana['side'],
                             'no': no, 'place': tana['floor'] + " " + place, 'floor': tana['floor']})
                        shelf_flags.append(no)
                else:
                    is_unknown = True

    html = ""
    if len(stocks) > 0:
        message = u"本棚にあります"
        for x in stocks:
            if x['shelfId']:
                if x['floor'] == u"1階":
                    js = "navigateShelf('7'," + str(x['shelfId']) + ");"
                else:
                    js = "navigateShelf('8'," + str(x['shelfId']) + ");"
            else:
                js = ""
            html += u"<div class=stockbox onclick=\"" + js + u"\"><div class=place>" + x[
                'place'] + u"</div><div class=no>" + x['no'] + u" / " + x[
                        'side'] + u"面</div><div class=open><i class=\"fa fa-map\"></i> マップを開く</div></div>"
    else:
        if is_unknown:
            message = u"本棚にあります（所蔵場所データが未整備）"
            html += u"<a href=\"" + url + u"\" target=\"_blank\"><div class=reserve><div class=place>本棚にあります</div><div class=no>所蔵場所データが未整備</div><div class=open><i class=\"fa fa-globe\"></i> OPACを開く</div></div></a>"
        elif is_backyard:
            message = u"書庫にあります（カウンターにお問い合わせください）"
            html += u"<a href=\"" + url + u"\" target=\"_blank\"><div class=reserve><div class=place>書庫にあります</div><div class=no>カウンターまで</div><div class=open><i class=\"fa fa-globe\"></i> OPACを開く</div></div></a>"
        elif is_other:
            message = u"他館にあります（カウンターにお問い合わせください）"
            html += u"<a href=\"" + url + u"\" target=\"_blank\"><div class=reserve><div class=place>他館にあります</div><div class=no>カウンターまで</div><div class=open><i class=\"fa fa-globe\"></i> OPACを開く</div></div></a>"
        elif is_rent:
            message = u"貸出中です（予約できます）"
            html += u"<a href=\"" + url + u"\" target=\"_blank\"><div class=rental><div class=place>貸出中です</div><div class=no>予約できます</div><div class=open><i class=\"fa fa-globe\"></i> OPACを開く</div></div></a>"
        else:
            message = u"エラーが発生しました"
            html += u"<a href=\"" + url + u"\" target=\"_blank\"><div class=reserve><div class=place>エラーが発生</div><div class=no>予約できます</div><div class=open><i class=\"fa fa-globe\"></i> OPACを開く</div></div></a>"
    return {'status': message, 'stocks': stocks, 'html': html}
