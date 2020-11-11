# %%
import random
import pandas as pd


def string():
    return ''.join([chr(97+random.randint(0, 25)) for _ in range(10)])


frame = pd.DataFrame()

for j in range(10):
    name = string().title()
    value = string()
    frame = frame.append(dict(name=name, value=value), ignore_index=True)

frame.index.name = 'Index'
frame.to_csv('data.csv')
frame

# %%
