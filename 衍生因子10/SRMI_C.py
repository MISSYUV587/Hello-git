#! /usr/bin/env python
# -*- coding :utf-8 -*-
# author: YU time :2018/5/2
def run_formula(dv, param = None):
    defult_param = {'t':15}
    if not param:
        param = defult_param

    t = param['t']


    SRMI_C = dv.add_formula("SRMI_C",
                      "(close-Delay(close,%s))/Max(open,Delay(open,%s))"%(t,t)
                      ,is_quarterly=False, add_data=True
                       )

    return SRMI_C