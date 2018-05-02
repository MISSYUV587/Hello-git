#! /usr/bin/env python
# -*- coding :utf-8 -*-
# author: YU time :2018/5/2
def run_formula(dv):
    ACCAP = dv.add_formula('ACCAP',
               "(ncf_oper_ttm-provisions)/tot_assets"
               , is_quarterly=True, add_data=True)
    return ACCAP