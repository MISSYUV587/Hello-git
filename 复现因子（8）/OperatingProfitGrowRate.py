
# coding: utf-8

# In[ ]:


OPGR = dv.add_formula("OPGR","((oper_profit)/Delay((oper_profit),365))-1",is_quarterly=False, add_data=True, overwrite=True)


# In[ ]:


def run_formula(dv,param = None):
    defult_param = {'t':365}
    if not param:
        param  = defult_param
        
    t = param['t']
    
    OperatingProfitGrowRate = dv.add_formula("OperatingProfitGrowRate",
                                             "((oper_profit)/Delay((oper_profit),%s))-1"%(t),
                                             is_quarterly=False, add_data=True)
    return OperatingProfitGrowRate

