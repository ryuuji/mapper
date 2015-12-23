#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import zenhan
import json
from bs4 import BeautifulSoup

_DEBUG = True

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
16	a	一般	914.6ナ	914.6ワ
16	b	一般	915キ	916ホ
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
312		カセットブック
313		カセットブック
314		カセットブック
426			L$	L$
19	a	参考	R033ア	R196ボ
19	b	参考	R002ミ	R031
155	a	参考	R031	R031
155	b	郷土	S920	S920
156	a	参考	R202	R291.0
157	a	参考	R337	R459
157	b	参考	R291.0	R337
158	a	参考	R570	R780
158	b	参考	R460	R569
159	a	参考	R830	R991
159	b	参考	R780ニ	R829
160	a	郷土	S221	S284
160	b	郷土	S002	S216
161	a	郷土	S336	S498
161	b	郷土	S284	S335
162	a	郷土	S900	S919
162	a	郷土	S921	S990
162	b	郷土	S500	S830
310		雑郷
167	a	ビジネス	007	914.6
166		一般洋書	Y000	Y991イ
165	a	大型	W723	W933
165	b	大型	W708	W723
169	a	大型	W702	W708
169	b	大型	W291.0	W702
168	a	大型	W210.1	W290
168	b	大型	W012	W210.0
170	a	ビジＤＶＤ
170	b	ビジネスめがね
170	b	ビジネス	007	914.6
255	a	コミック	H726	H726
255	b	コミック	H726	H726
256	a	コミック	H726	H726
256	b	コミック	H726	H726
257	a	コミック	H726	H726
257	b	文庫	H953	H999
258	a	文庫	H933ラ	H953
258	b	文庫	H933ハ	H933ヨ
259	a	文庫	H933ク	H933ハ
259	b	文庫	H923ウ	H933ク
260	a	文庫	HFヤマダ	HFワレモ
260	b	文庫	HFマツモ	HFヤマザ
261	a	文庫	HFハイク	HFマツム
261	b	文庫	HFトウド	HFノリス
262	a	文庫	HFソウダ	HFテンド
262	b	文庫	HFサワキ	HFセンソ
291	a	文庫	HFクロカ	HFサムク
291	b	文庫	HFカイキ	HFクロイ
292	a	文庫	HFイシカ	HFカイオ
292	b	文庫	HFアイカ	HFイシイ
405	a	絵本	Eア	Eイ
405	b	絵本	Eク	Eサ
404	a	絵本	Eイ	Eオ
404	b	絵本	Eカ	Eク
403	a	絵本	Eシ	Eセ
403	b	絵本	Eニ	Eハ
402	a	絵本	Eソ	Eチ
402	b	絵本	Eツ	Eナ
396	a	絵本	Eハ	Eフ
396	b	絵本	Eヤ	Eル
381	a	絵本	Eフ	Eマ
381	b	絵本	Eマ	Eモ
385	a	絵本	Eレ	Eワ
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
375		紙芝居	K	K
377		紙芝居	K	K
401		紙芝居	K	K
388		雑誌児童
251		雑誌$
252		雑誌$
253		雑誌$
254		雑誌$
168		CD
466		ブックスタート
467		ブックスタート
389		ビデオ
390		ビデオ
391		ビデオ
392		ビデオ
"""


def callno_to_float(no):
    if no == '':
        return 0

    # ラミネート向けの特別処理
    if no == 'L$' or re.search(u'L$', no):
        return 11000000

    # 2桁 + 文字列の場合
    tmp_ = re.findall(
            u"^([0-9]{2})([アァイィウゥエェオォカガキギクグケゲコゴサザシジスズセゼソゾタダチヂツッヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモヤャユュヨョラリルレロワヲン]+)", no)
    if len(tmp_) > 0:
        no = "%02s0.00000%s" % tmp_[0]
    # 2桁のみの場合
    tmp_ = re.findall(u"^([0-9]{2})$", no)
    if len(tmp_) > 0:
        no = "%02s0" % tmp_[0]

    # 3桁 + 文字列の場合
    tmp_ = re.findall(
            u"^([0-9]{3})([アァイィウゥエェオォカガキギクグケゲコゴサザシジスズセゼソゾタダチヂツッヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモヤャユュヨョラリルレロワヲン]+)", no)
    if len(tmp_) > 0:
        no = "%03s.00000%s" % tmp_[0]

    x = 0
    tbl = u"アァイィウゥエェオォカガキギクグケゲコゴサザシジスズセゼソゾタダチヂツッヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモヤャユュヨョラリルレロワヲン"
    for word in tbl:
        no = re.sub(word, "%02d" % x, no)
        x += 1

    tmp_ = re.findall(u"^F([0-9.]+)$", no)
    if len(tmp_) > 0:
        ret = float('913.600%s' % tmp_[0])
        return ret

    # 別置の処理
    ts = [
        {'prefix': 'HF', 'shift': 1000000, 'ndc': False},
        {'prefix': 'R', 'shift': 3000000, 'ndc': True},
        {'prefix': 'S', 'shift': 4000000, 'ndc': True},
        {'prefix': 'W', 'shift': 6000000, 'ndc': True},
        {'prefix': 'Y', 'shift': 9000000, 'ndc': True},
        {'prefix': 'H', 'shift': 2000000, 'ndc': False},
        {'prefix': 'E', 'shift': 5000000, 'ndc': False},
        {'prefix': 'YE', 'shift': 8000000, 'ndc': False},
        {'prefix': 'K', 'shift': 10000000, 'ndc': False},
    ]
    for t in ts:
        if not t['ndc']:
            tmp_ = re.findall(u"^" + t['prefix'] + "([.0-9]*)", no)
            if len(tmp_) > 0:
                if tmp_[0] == '':
                    ret = t['shift']
                else:
                    if tmp_[0].find('.') != -1:
                        ret = float(tmp_[0]) + t['shift']
                    else:
                        ret = float('0.' + tmp_[0]) + t['shift']
                return ret
        else:
            tmp_ = re.findall(u"^" + t['prefix'] + "([0-9]{3})([.0-9]*)", no)
            if len(tmp_) > 0:
                if tmp_[0][1].find('.') != -1:
                    ret = float(tmp_[0][0] + tmp_[0][1]) + t['shift']
                else:
                    ret = float(tmp_[0][0] + ".0000" + tmp_[0][1]) + + t['shift']
                return ret

    tmp_ = re.findall(u"^([0-9]{3})\.([0-9]+)", no)
    if len(tmp_) > 0:
        ret = float(tmp_[0][0] + "." + tmp_[0][1])
        return ret
    tmp_ = re.findall(u"^([0-9]{3})([0-9]+)", no)
    if len(tmp_) > 0:
        ret = float(tmp_[0][0] + "." + tmp_[0][1])
        return ret
    tmp_ = re.findall(u"^([0-9]{3})", no)
    if len(tmp_) > 0:
        ret = float(tmp_[0])
        return ret
    tmp_ = re.findall(u"^([0-9]{2})", no)
    if len(tmp_) > 0:
        ret = float(tmp_[0])
        return ret
    raise Exception('unknown:' + no)


tables = []
for params in data.splitlines():
    p = params.split('\t')
    if len(p) > 3:
        start = callno_to_float(p[3])
        end = callno_to_float(p[4])
        f = u'1階'
        if p[2] == u'絵本' or p[2] == u'紙芝居' or re.search(u'^児童|^ビデオ|^雑誌児童', p[2]):
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
    else:
        if p[0] != '':
            f = u'1階'
            if p[2] == u'絵本' or p[2] == u'紙芝居' or re.search(u'^児童|^ビデオ|^雑誌児童', p[2]):
                f = u'2階'
            tmp = {
                'shelf_id': int(p[0]),
                'side': p[1],
                'place': p[2],
                'start': -1,
                'end': -1,
                'floor': f
            }
            tables.append(tmp)


def parse(place, no):
    import math
    result = []
    flag = {}
    if _DEBUG:
        print "search:", no
    for line in tables:
        tmp_float = callno_to_float(no)
        regex = '^' + line['place']
        if re.search(regex, place):
            if math.floor(line['end']) == line['end']:
                end = line['end'] + 1
            else:
                end = float(str(line['end']) + '9999999999999999999999999999')
            if (line['start'] <= tmp_float < end) or (line['start'] == -1 and line['end'] == -1):
                if _DEBUG:
                    print line, tmp_float
                if not flag.has_key(str(line['shelf_id']) + line['side']):
                    flag[str(line['shelf_id']) + line['side']] = 1
                    result.append({
                        'rule': line,
                        'shelf_id': line['shelf_id'],
                        'side': line['side'],
                        'floor': line['floor']
                    })
    return result


# HTMLから所蔵情報を抽出する
def extract_call_numbers(html):
    result = []
    soup = BeautifulSoup(html, "lxml")
    for tr in soup.find_all('tr'):
        td = tr.find_all('td', False)
        if len(td) == 6:
            libkey = td[1].get_text().strip()
            status = td[4].get_text().strip()
            location = td[3].get_text().strip().replace(u'（', '(').replace(u'）', ')')
            if td[2].get_text().strip() == u"雑郷" and not re.search(u'閉架', location):
                location = u"雑郷"

            tmp_ = re.findall(u'\((.*)\)', location)
            if len(tmp_) > 0:
                location = re.sub(u'\((.*)\)', '', location)
                location = zenhan.h2z(location, zenhan.KANA)
                number = tmp_[0]
                number = zenhan.h2z(number, zenhan.KANA)
                number = number.replace(' ', '')
            else:
                number = ''
            result.append({
                'libkey': libkey,
                'status': status,
                'location': location,
                'number': number
            })
    return result


# 所蔵情報に所蔵場所を注入する
def mapping(holdings):
    results = []
    for item in holdings:
        tmp = {
            'source': item,
            'result': parse(item['location'], item['number'])
        }
        results.append(tmp)
    return results


def html(data, url, version):
    x = extract_call_numbers(data)
    if _DEBUG:
        print json.dumps(x, ensure_ascii=False, indent=2)
        print "----------------------"
    x = mapping(x)
    if _DEBUG:
        print json.dumps(x, ensure_ascii=False, indent=2)
        print "----------------------"
    if re.search(u'&#39894;&#27743;&#38306;&#20418;&#12288;&#26032;&#32862;&#20999;&#12426;&#25244;&#12365;',
                 data) and len(x) > 0 and len(x[0]['result']) > 0:
        x[0]['result'][0] = {
            'shelf_id': 307,
            'side': '',
            'place': u'新聞切り抜き',
            'floor': u'1階'
        }
        x[0]['source']['location']=u"新聞切り抜き"

    is_rent = False
    is_backyard = False
    is_other = False
    is_unknown = False
    is_cd = False

    stocks = []
    shelf_flags = []
    for item in x:
        if item['source']['status'] == u"貸出中です":
            is_rent = True
            continue
        if item['source']['libkey'] != u"本館":
            is_other = True
            continue
        if re.search(u"書庫|閉架", item['source']['location']):
            is_backyard = True
            continue
        if item['source']['status'] == u"貸出できます" or item['source']['status'] == u"帯出禁止" or item['source'][
            'status'] == u"館内利用の資料です" or item['source']['status'] == u'最新号のため貸出できません':
            if len(item['result']) > 0:
                if item['source']['location'] == 'CD':
                    is_cd = True
                message = item['source']['number'] + "/"
                shelves = []
                for t in item['result']:
                    message += str(t['shelf_id'])
                    if t['side']:
                        message += u"【" + t['side'] + u"面】"
                    message += ' '
                    shelves.append({'id': t['shelf_id'], 'side': t['side']})
                key = str(t['shelf_id']) + t['side']
                if key not in shelf_flags:
                    stocks.append(
                            {'message': message, 'shelfId': item['result'][0]['shelf_id'], 'floorId': 7,
                             'side': item['result'][0]['side'],
                             'no': item['source']['number'],
                             'place': item['result'][0]['floor'] + " " + item['source']['location'],
                             'floor': item['result'][0]['floor'], 'shelves': shelves})
                    shelf_flags.append(key)
            else:
                is_unknown = True

    html = ""
    if len(stocks) > 0:
        for x in stocks:
            if version == '1.3.0':
                j = json.dumps(x['shelves'])
                j = j.replace('"', '&quot;')
                if x['shelfId']:
                    if x['floor'] == u"1階":
                        js = "navigateShelf('7'," + j + ");"
                    else:
                        js = "navigateShelf('8'," + j + ");"
                else:
                    js = ""
                html += u"<div class=stockbox onclick=\"" + js + u"\"><div class=place>" + x[
                    'place'] + u"</div><div class=no>" + x[
                            'message'] + u"</div><div class=open><i class=\"fa fa-map\"></i> マップを開く</div></div>"

            else:
                if x['shelfId']:
                    if x['floor'] == u"1階":
                        js = "navigateShelf('7'," + str(x['shelfId']) + ");"
                    else:
                        js = "navigateShelf('8'," + str(x['shelfId']) + ");"
                else:
                    js = ""
                html += u"<div class=stockbox onclick=\"" + js + u"\"><div class=place>" + x[
                    'place'] + u"</div><div class=no>" + x[
                            'message'] + u"</div><div class=open><i class=\"fa fa-map\"></i> マップを開く</div></div>"
    else:
        if is_unknown:
            html += u"<a href=\"" + url + u"\" target=\"_blank\"><div class=reserve><div class=place>本棚にあります</div><div class=no>所蔵場所データが未整備</div><div class=open><i class=\"fa fa-globe\"></i> OPACを開く</div></div></a>"
        elif is_backyard:
            html += u"<a href=\"" + url + u"\" target=\"_blank\"><div class=reserve><div class=place>書庫にあります</div><div class=no>カウンターまで</div><div class=open><i class=\"fa fa-globe\"></i> OPACを開く</div></div></a>"
        elif is_other:
            html += u"<a href=\"" + url + u"\" target=\"_blank\"><div class=reserve><div class=place>他館にあります</div><div class=no>カウンターまで</div><div class=open><i class=\"fa fa-globe\"></i> OPACを開く</div></div></a>"
        elif is_rent:
            if is_cd:
                html += u"<a href=\"" + url + u"\" target=\"_blank\"><div class=rental><div class=place>貸出中です</div></div></a>"
            else:
                html += u"<a href=\"" + url + u"\" target=\"_blank\"><div class=rental><div class=place>貸出中です</div><div class=no>予約できます</div><div class=open><i class=\"fa fa-globe\"></i> OPACを開く</div></div></a>"
        else:
            html += u"<a href=\"" + url + u"\" target=\"_blank\"><div class=reserve><div class=place>エラーが発生</div><div class=no>予約できます</div><div class=open><i class=\"fa fa-globe\"></i> OPACを開く</div></div></a>"

    return {'html': html}

# print callno_to_float(u'S200L')
# print callno_to_float(u'Fタカハ')
