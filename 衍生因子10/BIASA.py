#! /usr/bin/env python
# -*- coding :utf-8 -*-
# author: YU time :2018/5/2
def run_formula(dv, param = None):
    defult_param = {'t':60}
    if not param:
        param = defult_param

    t = param['t']


    BIASA = dv.add_formula('BIASA', "(close/(Decay_linear(close,%s))-1)*100"%(t), add_data=True, is_quarterly=True)

    return BIASA