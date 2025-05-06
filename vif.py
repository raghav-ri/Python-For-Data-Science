import pandas as pd
from statsmodels.tools.tools import add_constant
from statsmodels.stats.outliers_influence import variance_inflation_factor

features = df[
    [
        'GDP per capita(USD)',
        'Population density(people per sq.km of land area)',
        'Unemployment (% of total labor force) (modeled ILO estimate)'
    ]
]
features = features.dropna()

# Add constant (intercept) to the features for the VIF calculation
X = add_constant(features)

# Compute VIF for each feature (including the constant)
vif_result = pd.Series(
    [variance_inflation_factor(X.values, i) for i in range(X.shape[1])],
    index=X.columns
    name='VIF'
)

print(vif_result)
