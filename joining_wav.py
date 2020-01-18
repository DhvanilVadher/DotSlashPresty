# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 13:00:45 2020

@author: Gulshan Rana
"""

import audiolab, scipy
a, fs, enc = audiolab.wavread('audio1.wav')
b, fs, enc = audiolab.wavread('beep.wav')
c = scipy.vstack((a,b))
audiolab.wavwrite(c, 'ab.wav', fs, enc)

d, fs, enc = audiolab.wavread('ab.wav')
e, fs, enc = audiolab.wavread('ab.wav')

f = scipy.vstack((d,e))
audiolab.wavwrite(f, 'finaud1.wav', fs, enc)