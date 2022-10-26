import pandas as pd
import numpy as np

df = pd.read_csv("Verbs.csv")
nparr = df.to_numpy()
pns_arr = ['infinitive', 'definition', 'yo', 'tú', 'él/ella/ud', 'nosotros', 'vosotros', 'ellos/ellas/uds']
print(len(nparr))
