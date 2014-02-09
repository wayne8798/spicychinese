#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json
import re
import string
import codecs

DEBUG = False

def debug(msg):
    if DEBUG:
        print msg

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

if len(sys.argv) != 2:
    print 'Please provide the file name to be analyzed.'
    sys.exit()

fullPath = sys.argv[1]
slashPos = string.rfind(fullPath, '/')

dataDir = fullPath[:(slashPos + 1)]
fileName = fullPath[(slashPos + 1):]
engFile = dataDir + "eng/" + fileName
uniFile = dataDir + "uni/" + fileName

f = codecs.open(fullPath, encoding='utf-8')
engF = open(engFile, 'w')
uniF = open(uniFile, 'w')

lines = f.readlines()
for line in lines:
    if len(line.strip()) == 1:
        continue
    msg = line
    debug('msg: ' + msg)
    if is_ascii(msg) == False:
        msg = msg.replace(u'，', ',')
        msg = msg.replace(u'。', '.')
        msg = msg.replace(u'《', '<')
        msg = msg.replace(u'》', '>')
        msg = msg.replace(u'：', ':')
        msg = msg.replace(u'；', ';')
        msg = msg.replace(u'“', '"')
        msg = msg.replace(u'‘', '\'')
        msg = msg.replace(u'”', '"')
        msg = msg.replace(u'’', '\'')
        msg = msg.replace(u'【', '[')
        msg = msg.replace(u'】', ']')
        msg = msg.replace(u'『', '{')
        msg = msg.replace(u'』', '}')
        msg = msg.replace(u'～', '~')
        msg = msg.replace(u'！', '!')
        msg = msg.replace(u'？', '?')
        msg = msg.replace(u'（', '(')
        msg = msg.replace(u'）', ')')
        
    for sentence in re.split('!|\?|\.|\n', msg):
        if len(sentence.strip()) > 1:
            if is_ascii(sentence):
                engF.write(sentence + '\n')
                debug('ENG: ' + sentence)
            else:
                uniF.write(sentence.encode('utf8') + '\n')
                debug('UNI: ' + sentence)
engF.close()
uniF.close()
