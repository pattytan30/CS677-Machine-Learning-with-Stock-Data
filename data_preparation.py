def year_data(df, year):
    df_year = df.loc[df["Year"] == year].reset_index()
    return df_year
    
def X(df):
    X = df.loc[:, ["mean_return", "volatility"]].values
    return X

def Y(df):
    Y = df.loc[:, "label"].values
    return Y
