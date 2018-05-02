#! /usr/bin/env python
# -*- coding :utf-8 -*-
# author: YU time :2018/5/2
def run_formula(dv,param=None):
    defult_param = {'t1':1,'t2':20,'t3':8,'t4':17}
    if not param:
        param = defult_param

    alpha007 = dv.add_formula("alpha007",
             "(Min(Rank(Decay_linear(Delta(vwap,%s),%s)),Rank(Decay_linear(Rank(Corr((low),Ts_Mean(volume,%s), %s)), %s))) * -1)"%(param['t1'],param['t2'],param['t2'],param['t3'],param['t4'])
               , is_quarterly=False, add_data=True,overwrite=True )

    return alpha007