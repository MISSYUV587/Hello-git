
# coding: utf-8

# In[ ]:


def run_formula(dv):
    ROECut = dv.add_formula("ROECut","(TTM(PB))/(TTM(PE))",
                            is_quarterly=False, add_data=True)
    return ROECut 

