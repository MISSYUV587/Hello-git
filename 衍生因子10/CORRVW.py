#! /usr/bin/env python
# -*- coding :utf-8 -*-
# author: YU time :2018/5/2
def run_formula(dv, param = None):
    defult_param = {'t':20}
    if not param:
        param = defult_param

    t = param['t']

    CORRVW = dv.add_formula("CORRVW","-1*Corr((high-Delay(high,%s)),volume,%s)"%(t,t),is_quarterly=False, add_data=True)

    return CORRVW