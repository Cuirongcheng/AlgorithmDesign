import pandas as pd
import numpy as np

wi = [35, 30, 60, 50, 40, 10, 25]
pi = [10, 40, 30, 50, 35, 40, 30]
status = [0, 0, 0, 0, 0, 0, 0]
data = pd.DataFrame(columns=["weight", "price", "density"])
data["weight"] = wi
data["price"] = pi
data["density"] = data["price"] / data["weight"]
data["status"] = status
reason = "price"  # weight or density
rest = 150
values = 0
data = data.sort_values(by=reason, ascending=False).reset_index().drop(["index"], axis=1)
index = 0


def best_weight(data, reason, rest, values, index):
    #print(reason, rest, values, index)

    if rest < np.min(data.loc[range(index, len(data)), "weight"]) or (index == len(data)):
        return values
    else:
        if rest >= data["weight"][index]:
            data.loc[index, 'status'] = 1 # 用data["status"][index] = 1会有warning
            rest = rest - data["weight"][index]
            values = values + data["price"][index]
            index = index + 1
            values=best_weight(data, reason, rest, values, index)
            return values
        else:
            index = index + 1
            values=best_weight(data, reason, rest, values, index)
            return values
yyt = best_weight(data, reason, rest, values, index)
print(yyt)

