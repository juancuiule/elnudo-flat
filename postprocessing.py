import pandas as pd
import numpy as np
from scipy import stats

# Simple script to show the parameters sent to the script, and generate a dummy file

if __name__ == "__main__":
    json = pd.read_json('./data.json')

    values = np.array([])
    for x in json["data"]:
        values = np.append(values, x["time"] / 1000)
    
    f = stats.gaussian_kde(values, 0.5)

    pairs = []
    for x in range(0, int(values.max())):
        pairs.append([x, f(x)[0], int(round(np.average(values)))])
    
    pd.DataFrame(pairs).to_csv("change-blindness.csv", index=False, header=["time", "area", "average"])
