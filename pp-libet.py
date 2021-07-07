import pandas as pd
# import numpy as np
# from scipy import stats
# import matplotlib.pyplot as plt

if __name__ == "__main__":
    json = pd.read_json('./libet-data.json')
    
    raw = []
    for x in json["data"]:
        if "pc" in x.keys() and "user" in x.keys() and "won" in x.keys():
            raw.append([x["pc"], x["user"], x["won"]])
    pd.DataFrame(raw).to_csv("libet-raw-data.csv", index=True, header=["pc", "user", "won"])
