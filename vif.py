# import pandas as pd
# from statsmodels.tools.tools import add_constant
# from statsmodels.stats.outliers_influence import variance_inflation_factor

# features = {
    
#         'GDP per capita(USD)': [40000,42000,45000,47000,50000],
#         'Population density(people per sq.km of land area)': [100,150,200,250,350],
#         'Unemployment (% of total labor force) (modeled ILO estimate)': [5,6,7,8,9]
    
# }
# df=pd.DataFrame(features)

# features = df.dropna()

# # Add constant (intercept) to the features for the VIF calculation
# X = add_constant(features)

# # Compute VIF for each feature (including the constant)
# vif_result = pd.Series(
#     [variance_inflation_factor(X.values, i) for i in range(X.shape[1])],
#     index=X.columns,
#     name='VIF'
# )

# print(vif_result)




import pandas as pd
from statsmodels.tools.tools import add_constant
from statsmodels.stats.outliers_influence import variance_inflation_factor



feature= {
    "Sq. Ft": [100,150,200,250,300,350,400],
    "Bed Room":[1,2,3,4,5,6,7],
    "Parking":[1,1,1,2,2,2,3]
}
df=pd.DataFrame(feature)
feature=df.dropna()
X=add_constant(feature)

vif_res=pd.Series(
    [variance_inflation_factor(X.values,i) for i in range(X.shape[1])],
    index=X.columns,
    name="VIF"
)
print(vif_res)