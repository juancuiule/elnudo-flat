import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Simple script to show the parameters sent to the script, and generate a dummy file

MIN_TIME = 1000 * 10 # 10 secs
MAX_TIME = 1000 * 60 * 4 # 4 mins
BW_WIDTH = 0.15

if __name__ == "__main__":
    json = pd.read_json('./data.json')
    
    raw = []
    for x in json["data"]:
        if "clicks" in x.keys() and "time" in x.keys() and "tip" in x.keys():
            raw.append([x["clicks"], x["time"], x["tip"]])
    pd.DataFrame(raw).to_csv("raw-data.csv", index=True, header=["clicks", "time", "tip"])

    values = np.array([])
    for x in json["data"]:
        time = x["time"]
        if "clicks" in x.keys() and time < MAX_TIME and time > MIN_TIME:
            values = np.append(values, time / 1000)
    
    f = stats.gaussian_kde(values, BW_WIDTH)

    pairs = []
    average = int(round(np.average(values)))
    total = len(values)
    for x in range(0, int(values.max() + 200)):
        y = f(x)[0]
        pairs.append([x, y, average, total])
        if x > average and y < 0.0001 and x % 60 == 0:
            break;

    pd.DataFrame(pairs).to_csv("change-blindness.csv", index=False, header=["time", "area", "average", "total"])
    
    f.covariance_factor = lambda : BW_WIDTH
    f._compute_covariance()
    rango = range(0, pairs[-1][0])
    plt.plot(rango, f(rango))
    plt.savefig("curva.png")
