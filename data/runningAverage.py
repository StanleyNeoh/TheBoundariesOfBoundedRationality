import pandas as pd
import sys

path = sys.argv[1]
period = int(sys.argv[2])
runningCol = sys.argv[3]
colsMerger = sys.argv[4:]

file = pd.read_csv(path)

def runningAverage(data, cols):
    if len(cols) == 0:
        return data.rolling(period, min_periods = 1, center = True, on = runningCol).mean()
    else:
        first = cols[0]
        rest = cols[1:]
        uniqueFirst = data[first].unique()
        df = pd.DataFrame(columns=file.columns)
        for val in uniqueFirst:
            filtered = data[data[first] == val]
            df = pd.concat([df, runningAverage(filtered, rest)], ignore_index=True)
        return df

df = runningAverage(file, colsMerger)

newFileName = "smoothed_" + path.split('\\')[-1]
df.to_csv(newFileName)
