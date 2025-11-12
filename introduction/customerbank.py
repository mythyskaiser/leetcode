import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> list[int]:
    a = [players.index.shape[0],players.shape[1]]
    return a

df = pd.DataFrame([[1,2],[1,2],[2,3]], columns=['g','f'])
getDataframeSize(df)