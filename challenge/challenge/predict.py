import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--data', dest="data")
args = parser.parse_args()
data = pd.read_csv('challenge/challenge/predictions.csv', index_col=0)
data.to_csv('predictions.csv')


