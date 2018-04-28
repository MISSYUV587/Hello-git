
# coding: utf-8

def run_formula(dv, param = None):
    defult_param = {'t':60}
    if not param:
        param = defult_param
        
    
    VOL60 = dv.add_formula("VOL60", "Ts_Mean(turnover_ratio,%s)"%(param['t']),
                           is_quarterly=False, add_data=True)
    return VOL60

