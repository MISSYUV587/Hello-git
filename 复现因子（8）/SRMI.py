
# coding: utf-8

# In[ ]:


def run_formula(dv, param = None):
    defult_param = {'t':10}
    if not param:
        param = defult_param
        
    t = param['t']
    
    SRMI = dv.add_formula("SRMI",
                      "(close-Delay(close,%s))/Max(close,Delay(close,%s))"%(t,t),
                       is_quarterly=False, add_data=True)
    return SRMI

