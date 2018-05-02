#! /usr/bin/env python
# -*- coding :utf-8 -*-
# author: YU time :2018/5/2
def run_formula(dv, param = None):
    defult_param = {'t':20}
    if not param:
        param = defult_param

    t = param['t']

    VolatilityC = dv.add_formula('VolatilityC',"StdDev(close,%s)/Ts_Mean(close,%s)"%(t,t),
                             is_quarterly=True, add_data=True)

    return VolatilityC