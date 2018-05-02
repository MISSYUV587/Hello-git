#! /usr/bin/env python
# -*- coding :utf-8 -*-
# author: YU time :2018/5/2
def run_formula(dv,param=None):
    defult_param = {'t1':14,'t2':14,'t3':61,'t4':2}
    if not param:
        param = defult_param

    def SMA(A,n,m):
      alpha = m/n
      return A.ewm(alpha=alpha, adjust=False).mean()


    CoppockCurve_J = dv.add_formula('CoppockCurve_J',"SMA((((high+low)/Delay((high+low),%s))-((high+low)/Delay((high+low),%s))),%s,%s)"%(param['t1'],param['t2'],param['t3'],param['t4']),
                   is_quarterly=True, add_data=True,
                   register_funcs={"SMA":SMA}
                   )

    return CoppockCurve_J