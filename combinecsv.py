import pandas as pd




goodf1 = pd.read_csv("feats/goodf1.csv")
badf = pd.read_csv("feats/badf.csv")

new = goodf1.append(badf, sort=False)

new.to_csv("feats/combined.csv")