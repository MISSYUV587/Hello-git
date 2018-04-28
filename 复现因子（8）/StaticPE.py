
# coding: utf-8

# In[ ]:


def run_forumla(dv, param = None):
    defult_param = {'t':4}
    if not param:
        param = defult_param
        
    t = param['t']
    
    StaticPE_J= dv.add_formula("StaticPE", 
                          "Delay(pe_ttm,%s)"%(t),
                          is_quarterly=False, add_data=True)
    return StaticPE

