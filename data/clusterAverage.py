import pandas as pd
import sys

path = sys.argv[1]
colsMerger = sys.argv[2:]

file = pd.read_csv(path)
file = file.drop(columns=['[run number]'])

def clusterAverage(data, cols):
    if len(cols) == 0:
        return data.mean(axis = 'index').to_frame().T
    else:
        first = cols[0]
        rest = cols[1:]
        uniqueFirst = data[first].unique()
        df = pd.DataFrame(columns=file.columns)
        for val in uniqueFirst:
            filtered = data[data[first] == val]
            df = pd.concat([df, clusterAverage(filtered, rest)], ignore_index=True)
        return df

df = clusterAverage(file, colsMerger)

newFileName = "processed_" + path.split('\\')[-1]
df.to_csv(newFileName)
