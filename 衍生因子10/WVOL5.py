#! /usr/bin/env python
# -*- coding :utf-8 -*-
# author: YU time :2018/5/2
def run_formula(dv, param = None):
    defult_param = {'t':5}
    if not param:
        param = defult_param

    t = param['t']

    WVOL5 = dv.add_formula("WVOL5","Decay_linear(turnover_ratio,%s)"%(param['t']), is_quarterly=False, add_data=True)

    return WVOL5