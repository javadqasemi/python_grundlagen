#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
####################################################
#
# Uebung:
# Erstellen Sie ein Programm, welches die folgenden
# Unicode Werte als Text liefert.
#
# 72,97,108,108,111
#
####################################################

#### Lösung: ####

for i in (72, 97, 108, 108, 111):
    print(chr(i), end=' ')

# Charakter ausserhalb des Standard ASCII-Ranges (>127)
# print unichr(228)

# So erstellen Sie die Unicode Werte
# for i in ('H','a','l','l','o'):
#   print ord(i),
