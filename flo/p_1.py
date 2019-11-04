import pandas as pd

df_orders = pd.read_csv('../data/orders.csv')

df_orders['Profit']

# ----- HELPERS ----- 

def strToNumeric(val):
    _,b = val.split('$')
    b = b.replace(',','')
    return float(b)


# ---- MAIN ------
# column PROFIT to numeric
df_orders[['Profit']] = df_orders[['Profit']].applymap(strToNumeric)


# column SALE to numerif
df_orders[['Sales']] = df_orders[['Sales']].applymap(strToNumeric)