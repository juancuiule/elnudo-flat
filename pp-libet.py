import pandas as pd
# import numpy as np
# from scipy import stats
import matplotlib.pyplot as plt

if __name__ == "__main__":
    json = pd.read_json('./libet-data.json')
    
    raw = []
    for x in json["data"]:
        if "pc" in x.keys() and "user" in x.keys() and "won" in x.keys():
            pc = x["pc"]
            user = x["user"]
            won = x["won"]
            if pc <= 50 and user <= 50 and (won == "pc" or won == "user"):
                raw.append([pc, user, won])
    pd.DataFrame(raw).to_csv("libet-raw-data.csv", index=True, header=["pc", "user", "won"])

    df["user"].hist(grid=False, bins=50)
    plt.xlabel('Puntos usuarie')
    plt.ylabel('Número de partidas')
    plt.title('Puntos de usuaries por partida')
    plt.savefig("hist.png")
