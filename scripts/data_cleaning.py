import pandas as pd
import numpy as np

train = pd.read_csv("data/raw data/train.csv")
test = pd.read_csv("data/raw data/test.csv")

print(train.shape)
print(test.shape)