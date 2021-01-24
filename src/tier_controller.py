import pandas as pd

tiers = pd.read_csv('data/pokemon_tiers.csv', index_col=0)

def get_tier(id):
    if not id in tiers.index:
        return

    return tiers.loc[id].Tier
