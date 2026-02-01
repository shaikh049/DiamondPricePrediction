# Machine Learning project -- Diamond Price Prediction

# git add .
# git commit -m "Initial commit"
# git branch -M main
# git push -u origin main

# git branch

# python -m src.logger
# python -m src.exception



"""| Goal                             | Code                        |
| -------------------------------- | --------------------------- |
| Find NaNs in each column         | `df.isna().sum()`           |
| Drop rows with NaN in one column | `df.dropna(subset=["col"])` |
| Drop rows with NaN anywhere      | `df.dropna()`               |
| Drop rows only when all are NaN  | `df.dropna(how="all")`      |
| Replace NaNs with value          | `df.fillna(value)`          |
"""