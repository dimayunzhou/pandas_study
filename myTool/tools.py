import pandas as pd
import numpy as np

def handle(set):
    df = pd.DataFrame(set)
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index('date')

    df1 = df[df['pig'].isin(['big','small'])]
    print df1