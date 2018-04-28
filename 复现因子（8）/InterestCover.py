
# coding: utf-8

# In[ ]:


def run_formula(dv):
    InterestCover = dv.add_formula("InterestCover",
                                "((tot_profit)-(less_int_exp)+(int_income))/(((less_int_exp)+(int_income))*-1)",
                                is_quarterly=False, add_data=True)
    return InterestCover

