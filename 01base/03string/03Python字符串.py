#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
python字符串:
"""
# S = ''                      # Empty string
# S = "spam's"                # Double quotes, same as single
# S = 's\np\ta\x00m'          # Escape sequences,转义序列
# S = """...multiline..."""   # Triple-quoted block strings
# S = r'\temp\spam'           # Raw strings (no escapes)
# B = b'sp\xc4m'              # Byte strings in 2.6, 2.7, and 3.X
# U = u'sp\u00c4m'            # Unicode strings in 2.X and 3.3+
# S1 + S2 ,S * 3                          # Concatenate, repeat（合并、重复）
# S[i],S[i:j],len(S)                       # Index, slice, length（索引、分片、长度）
# "a %s parrot" % kind        # String formatting expression
# "a {0} parrot".format(kind) # String formatting method in 2.6, 2.7, and 3.X
# S.find('pa')                # String methods (see ahead for all 43): search
# S.rstrip()                  # remove whitespace,
# S.replace('pa', 'xx')       # replacement,
# S.split(',')                # split on delimiter
# S.isdigit()                 # 内容测试
# S.lower()                   # case conversion
# S.endswith('spam')          # end test,
# 'spam'.join(strlist)        # delimiter join
# S.encode('latin-1')         # Unicode encoding,
# B.decode('utf8')            # Unicode decoding
# for x in S: print(x)        # Iteration, membership
# 'spam' in S                 # 检查S中是都带有S的字符串
# [c * 2 for c in S]          #
# map(ord, S)                 #
# re.match('sp(.*)am', line)  # Pattern matching: library module


#  python自动再任意的表达式中合并相邻的字符串
title = "python" ' of ' "Title"
print(title)

# 特殊字符串
t = 'a\nb\tc'
print(t)
print(len(t))   # 长度是5而不管其如何展现,即a、\n、b、\t、c，返回这5个字符长度

# 字符串


