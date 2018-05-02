#! /usr/bin/env python
# -*- coding :utf-8 -*-
# author: YU time :2018/5/2
def run_formula(dv, param = None):
    import pandas as pd
    default_param = {'indu':'sw1'}
    if not param:
        param = default_param

    indu = param['indu']


    dv.add_field(indu)
    dv.add_field('ps')

    _indu = dv.get_ts(indu).stack()
    ps = dv.get_ts('PS').stack()

    ps_indu = pd.concat([_indu,ps],axis=1,keys=[indu,'ps'])
    ps_sw1 = pd.concat([sw1,ps],axis=1,keys=[sw1,'ps'])

    Indu_max = ps_sw1.groupby(['sw1']).max().ps.to_dict()
    Indu_min = ps_sw1.groupby(['sw1']).min().ps.to_dict()


    ps_sw1['PSIndu_Max'] = [Indu_max[c] for c in ps_sw1['sw1'].values]
    ps_sw1['PSIndu_Min'] = [Indu_min[c] for c in ps_sw1['sw1'].values]

    ps_sw1['PSMIndu'] = (ps_sw1['ps']-ps_sw1['PSIndu_Min'])/ps_sw1['PSIndu_Max']

    PSMIndu = ps_sw1.PSMIndu.unstack()

    dv.append_df(PSMIndu, 'PSMIndu')
    return dv.get_ts('PSMIndu')