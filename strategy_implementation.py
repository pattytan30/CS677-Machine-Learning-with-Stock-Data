import pandas as pd
import numpy as np

def green_week(prediction):
    green_weeks = [ i for i in range(len(prediction)) if prediction[i] == "green"]
    return green_weeks

def profit_loss_balance(df, invest, green_week):
    df = df.copy()
    df["Profit/Loss"] = np.nan
    df["Account Balance"] = np.nan 
        
    for index, row in df.iterrows():
        if index == 0:
            df.loc[index,"Profit/Loss"] = 0
            df.loc[index,"Account Balance"] = invest
            continue
            
        if row["Week_Number"] in green_week:
            df.loc[index,"Profit/Loss"] = df.loc[index,"Return"] * df.loc[index-1,"Account Balance"]
                
            df.loc[index,"Account Balance"] = df.loc[index-1, "Account Balance"]\
            + df.loc[index, "Profit/Loss"]
                
        else:
            df.loc[index,"Profit/Loss"] = 0
            df.loc[index,"Account Balance"] = df.loc[index-1, "Account Balance"]
                
    return df


def final_balance(new_df):
    final_balance = new_df.loc[new_df.index[-1], "Account Balance"]
    return round(final_balance, 2)

def buy_hold(invest, buy_in_price, close_price):
    buy_in_amount = invest / buy_in_price
    end_value = buy_in_amount * close_price
    return round(end_value, 2)
