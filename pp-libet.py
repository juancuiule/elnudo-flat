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

    df = pd.DataFrame(raw, columns=["pc", "user", "won"])

    values = pd.Series(df["user"]).value_counts()
    histograma = []
    for x in range(0, 51):
        if x in values.keys():
            histograma.append([x, values[x]])
        else:
            histograma.append([x, 0])
    pd.DataFrame(histograma).to_csv("libet.csv", index=False, header=["puntos", "partidas"])

    df["user"].hist(grid=False, bins=50)
    plt.xlabel('Puntos usuarie')
    plt.ylabel('Número de partidas')
    plt.title('Puntos de usuaries por partida')
    plt.savefig("hist.png")
