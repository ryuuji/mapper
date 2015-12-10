# -*- coding: euc-jp -*-

from types import UnicodeType

ASCII = 1
DIGIT = 2
KANA  = 4
ALL = ASCII | DIGIT | KANA

__version__ = '0.4'

class zenhanError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

# list of ZENKAKU characters
z_ascii = [u"��", u"��", u"��", u"��", u"��", u"��", u"��", u"��", u"��",
           u"��", u"��", u"��", u"��", u"��", u"��", u"��", u"��", u"��",
           u"��", u"��", u"��", u"��", u"��", u"��", u"��", u"��",
           u"��", u"��", u"��", u"��", u"��", u"��", u"��", u"��", u"��",
           u"��", u"��", u"��", u"��", u"��", u"��", u"��", u"��", u"��",
           u"��", u"��", u"��", u"��", u"��", u"��", u"��", u"��",
           u"��", u"��", u"��", u"��", u"��", u"��", u"��", u"��", u"��",
           u"��", u"��", u"��", u"��", u"��", u"��", u"��", u"��", u"��",
           u"��", u"��", u"��", u"��", u"��", u"��", u"��", u"��", u"��",
           u"��", u"��", u"��", u"��", u"��", u"��"]

z_digit = [u"��", u"��", u"��", u"��", u"��",
           u"��", u"��", u"��", u"��", u"��"]

z_kana = [u"��", u"��", u"��", u"��", u"��",
          u"��", u"��", u"��", u"��", u"��",
          u"��", u"��", u"��", u"��", u"��",
          u"��", u"��", u"��", u"��", u"��",
          u"��", u"��", u"��", u"��", u"��",
          u"��", u"��", u"��", u"��", u"��",
          u"��", u"��", u"��", u"��", u"��",
          u"��", u"��", u"��",
          u"��", u"��", u"��", u"��", u"��",
          u"��", u"��", u"��",
          u"��", u"��", u"��", u"��", u"��",
          u"��", u"��", u"��", u"��", u"��",
          u"��", u"��", u"��", u"��", u"��",
          u"��", u"��", u"��", u"��", u"��",
          u"��", u"��", u"��", u"��", u"��",
          u"��", u"��", u"��", u"��", u"��",
          u"��", u"��", u"��", u"��", u"��",
          u"��", u"��", u"��", u"��", u"��", u"��", u"��", u"��"]

# list of HANKAKU characters
h_ascii = [u"a", u"b", u"c", u"d", u"e", u"f", u"g", u"h", u"i",
           u"j", u"k", u"l", u"m", u"n", u"o", u"p", u"q", u"r",
           u"s", u"t", u"u", u"v", u"w", u"x", u"y", u"z",
           u"A", u"B", u"C", u"D", u"E", u"F", u"G", u"H", u"I",
           u"J", u"K", u"L", u"M", u"N", u"O", u"P", u"Q", u"R",
           u"S", u"T", u"U", u"V", u"W", u"X", u"Y", u"Z",
           u"!", u'"', u"#", u"$", u"%", u"&", u"'", u"(", u")",
           u"*", u"+", u",", u"-", u".", u"/", u":", u";", u"<",
           u"=", u">", u"?", u"@", u"[", u"\\", u"]", u"^", u"_",
           u"`", u"{", u"|", u"}", u"~", u" "]

h_digit = [u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9"]

h_kana = [u"��", u"��", u"��", u"��", u"��",
          u"��", u"��", u"��", u"��", u"��",
          u"��", u"��", u"��", u"��", u"��",
          u"��", u"��", u"��", u"��", u"��",
          u"��", u"��", u"��", u"��", u"��",
          u"��", u"��", u"��", u"��", u"��",
          u"��", u"��", u"��", u"��", u"��",
          u"��", u"��", u"��",
          u"��", u"��", u"��", u"��", u"��",
          u"��", u"��", u"��",
          u"��", u"��", u"��", u"��", u"��",
          u"��", u"��", u"��", u"��", u"����",
          u"����", u"����", u"����", u"����", u"����",
          u"����", u"����", u"����", u"����", u"����",
          u"����", u"����", u"��", u"�Î�", u"�Ď�",
          u"�ʎ�", u"�ˎ�", u"�̎�", u"�͎�", u"�Ύ�",
          u"�ʎ�", u"�ˎ�", u"�̎�", u"�͎�", u"�Ύ�",
          u"��", u"��", u"��", u"��", u"��", u"��", u"��", u"��"]

# maps of ascii
zh_ascii = {}
hz_ascii = {}

for (z, h) in zip(z_ascii, h_ascii):
    zh_ascii[z] = h
    hz_ascii[h] = z

del z_ascii, h_ascii

# maps of digit
zh_digit = {}
hz_digit = {}

for (z, h) in zip(z_digit, h_digit):
    zh_digit[z] = h
    hz_digit[h] = z

del z_digit, h_digit

# maps of KANA
zh_kana = {}
hz_kana = {}

for (z, h) in zip(z_kana, h_kana):
    zh_kana[z] = h
    hz_kana[h] = z

del z_kana, h_kana

# function check text
# argument and return: unicode string
def _check_text(t):
    if isinstance(t, UnicodeType) or t == '':
        return t
    else:
        raise zenhanError, "Sorry... You must set UNICODE String."

# function check convertion mode and make transform dictionary
# argument: integer
# return: transform dictionary
def _check_mode_zh(m):
    t_m = {}
    if isinstance(m, int) and m >= 0 and m <= 7:
        return _zh_trans_map(m)
    else:
        raise zenhanError, "Sorry... You set invalid mode."

def _check_mode_hz(m):
    t_m = {}
    if isinstance(m, int) and m >= 0 and m <= 7:
        return _hz_trans_map(m)
    else:
        raise zenhanError, "Sorry... You set invalid mode."

#
def _zh_trans_map(m):
    tm = {}
    if m >=4:
        tm.update(zh_kana)
        m -= 4
    if m >= 2:
        tm.update(zh_digit)
        m -= 2
    if m:
        tm.update(zh_ascii)
    return tm

def _hz_trans_map(m):
    tm = {}
    if m >=4:
        tm.update(hz_kana)
        m -= 4
    if m >= 2:
        tm.update(hz_digit)
        m -= 2
    if m:
        tm.update(hz_ascii)
    return tm


# function convert from ZENKAKU to HANKAKU
# argument and return: unicode string
def z2h(text="", mode=ALL, ignore=()):
    converted = []

    text = _check_text(text)
    zh_map = _check_mode_zh(mode)

    for c in text:
        if c in ignore:
            converted.append(c)
        else:
            converted.append(zh_map.get(c, c))

    return ''.join(converted)

# function convert from HANKAKU to ZENKAKU
# argument and return: unicode string
def h2z(text, mode=ALL, ignore=()):
    converted = ['']

    text = _check_text(text)
    hz_map = _check_mode_hz(mode)

    prev = ''
    for c in text:
        if c in ignore:
            converted.append(c)
        elif c in (u"��", u"��"):
            p = converted.pop()
            converted.extend(hz_map.get(prev+c, [p, hz_map.get(c, c)]))
        else:
            converted.append(hz_map.get(c, c))

        prev = c

    return ''.join(converted)

if __name__ == "__main__":
    teststr = unicode("��abc�ģŎޣ�123�����������ގ����ʥХӎ̎ߎ͎ߎ�", "euc-jp")

    print "original:", teststr.encode("euc-jp")
    print "h2z ascii only:", h2z(teststr, ASCII).encode("euc-jp")
    print "h2z ascii and kana:", h2z(teststr, ASCII|KANA).encode("euc-jp")
    print "z2h digit only:", z2h(teststr, DIGIT).encode("euc-jp")
    print "z2h digit and kana:", z2h(teststr, DIGIT|KANA).encode("euc-jp")
    print "z2h digit and kana, but '��':", z2h(teststr, DIGIT|KANA, (u"��")).encode("euc-jp")
