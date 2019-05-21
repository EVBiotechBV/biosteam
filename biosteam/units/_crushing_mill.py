# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 22:14:01 2018

@author: yoelr
"""
from .. import Unit
from .decorators import cost, design
from .metaclasses import splitter
from ._splitter import Splitter

@cost('Flow rate', cost=1.5e6, CE=541.7, exp=0.6, S=335e3, kW=0.006)
@design('Flow rate', 'kg/hr', lambda self: self.ins[0].massnet)
class CrushingMill(Unit, metaclass=splitter):
    _run = Splitter._run
    
