
        
def run_formula(dv, param = None):
    defult_param = {'t':4}
    if not param:
        param = defult_param
    
    StaticPE = dv.add_formula('StaticPE', 
           '''Delay(pe_ttm,%s)'''%(param['t']),
           is_quarterly=False)
    
    return StaticPE

