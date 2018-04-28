
# coding: utf-8

# In[ ]:


def run_formula(dv, param = None):
    defult_param = {'t': 20}
    if not param:
        param = defult_param
        
    t = param['t']
    
    alpha60 = dv.add_formula('alpha60', "Ts_Sum(((close-low)-(high-close))/(high-low)*volume,%s)"%(t),
                             is_quarterly=False,
                             add_data=True)
    return alpha60



