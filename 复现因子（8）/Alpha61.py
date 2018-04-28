
# coding: utf-8

# In[ ]:


def run_formula(dv,param=None):
    defult_param = {'t1':1,'t2':12,'t3':80,'t4':8,'t5':17}
    if not param:
        param = defult_param
        
    
    alpha61 = dv.add_formula("Alpha61",
             "(Max(Rank(Decay_linear(Delta(vwap,%s),%s)),Rank(Decay_linear(Rank(Corr((low),Ts_Mean(volume,%s),%s)),%s))) * -1)"%(param['t1'],param['t2'],param['t3'],param['t4'],param['t5'])
               , is_quarterly=False, add_data=True)
    return alpha61

