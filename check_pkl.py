import pickle
import pandas as pd

df = pd.read_pickle("checkpoints/mbert_test_entries.pkl")
print(type(df))
print(df.shape if hasattr(df, 'shape') else len(df))
print(df[0] if isinstance(df, list) else df.iloc[0])