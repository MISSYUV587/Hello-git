#! /usr/bin/env python
# -*- coding :utf-8 -*-
# author: YU time :2018/5/2
def run_formula(dv,param=None):
    defult_param = {'t1':23,'t2':2}
    if not param:
        param = defult_param

    def SMA(A,n,m):
        alpha = m/n
        return A.ewm(alpha=alpha, adjust=False).mean()

    EMAA22 = dv.add_formula('EMAA22',
               "SMA(((close+high+low+open)/4)*volume,%s,%s)"%(param['t1'],param['t2'])
             , is_quarterly=False, add_data=True,
             register_funcs={"SMA":SMA}
             )
    
    return EMAA22