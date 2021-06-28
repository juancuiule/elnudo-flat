import pandas as pd
import numpy as np
from scipy import stats

# Simple script to show the parameters sent to the script, and generate a dummy file

MIN_TIME = 1000 * 30 # 30 secs
MAX_TIME = 1000 * 60 * 6 # 6 mins

if __name__ == "__main__":
    json = pd.read_json('./data.json')

    values = np.array([])
    for x in json["data"]:
        time = x["time"]
        if x < MAX_TIME and x > MIN_TIME:
            values = np.append(values, x["time"] / 1000)
    
    f = stats.gaussian_kde(values, 0.5)

    pairs = []
    for x in range(0, int(values.max() + 200)):
        pairs.append([x, f(x)[0], int(round(np.average(values))), len(values)])
        if x > values.mean() and f(x)[0] < 0.0001 and x % 60 == 0:
            break;

    pd.DataFrame(pairs).to_csv("change-blindness.csv", index=False, header=["time", "area", "average", "total"])
