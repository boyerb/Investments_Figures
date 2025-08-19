import os
import time
from datetime import datetime

import numpy as np
import pandas as pd
import wrds
from dateutil.relativedelta import relativedelta


#############################################################################################################################
def msf_first_load():
    db = wrds.Connection(wrds_username="boyerb")

    query = """
    SELECT a.permno, a.permco, a.date, b.ncusip, b.ticker, b.shrcd, b.exchcd, b.siccd,
           a.prc, a.ret, a.retx, a.vol, a.shrout, a.cfacshr
    FROM crspm.msf a INNER JOIN crspm.msenames b
    ON a.permno = b.permno and a.date >= b.namedt and a.date <= b.nameendt
    """

    start_time = time.time()
    stk = db.raw_sql(query, date_cols=["date"])
    print(f"SQL: {time.time() - start_time:.1f} seconds\n")

    db.close()

    stk = stk.sort_values(["permno", "date"])
    stk = stk.drop_duplicates(subset=["permno", "date"], keep="last")
    stk = stk.query("prc == prc").reset_index(drop=True)  # drop Nans and reset index

    # change = {'date': 'caldt', 'ncusip': 'cusip', 'exchcd': 'excd', 'shrout': 'shr', 'cfacshr': 'cumfacshr'}
    # stk = stk.rename(columns=change)

    stk["permno"] = stk["permno"].astype(int)
    stk["permco"] = stk["permco"].astype(int)
    stk["shrcd"] = stk["shrcd"].astype(int)
    stk["exchcd"] = stk["exchcd"].astype(int)
    stk["siccd"] = stk["siccd"].astype(int)

    print(stk.info())

    stk.to_parquet(
        "msf.parquet"
    )  # stk.to_csv('/tmp/mstk.csv', index=False, date_format='%Y-%m-%d', float_format='%.6g')


def msf_update():
    # Connect to WRDS
    db = wrds.Connection(wrds_username="boyerb")

    # Get the current date
    today = datetime.now()

    first_day_of_current_month = today.replace(day=1)
    first_day_of_last_month = first_day_of_current_month - relativedelta(months=1)
    last_day_of_last_month = first_day_of_current_month - relativedelta(days=1)

    first_day_of_last_month = first_day_of_last_month.strftime("%Y-%m-%d")
    last_day_of_last_month = last_day_of_last_month.strftime("%Y-%m-%d")

    query = f"""
        SELECT a.permno, a.permco, a.date, b.ncusip, b.ticker, b.shrcd, b.exchcd, b.siccd,
               a.prc, a.ret, a.retx, a.vol, a.shrout, a.cfacshr
        FROM crspm.msf a INNER JOIN crspm.msenames b
        ON a.permno = b.permno
        WHERE a.date >= '{first_day_of_last_month}' AND a.date <= '{last_day_of_last_month}'
        """
    new_data = db.raw_sql(query)
    db.close()

    new_data = new_data.sort_values(["permno", "date"])
    new_data = new_data.drop_duplicates(subset=["permno", "date"], keep="last")
    new_data = new_data.query("prc == prc").reset_index(drop=True)  # drop Nans and reset index

    # change = {'date': 'caldt', 'ncusip': 'cusip', 'exchcd': 'excd', 'shrout': 'shr', 'cfacshr': 'cumfacshr'}
    # new_data = new_data.rename(columns=change)

    new_data["permno"] = new_data["permno"].astype(int)
    new_data["permco"] = new_data["permco"].astype(int)
    new_data["shrcd"] = new_data["shrcd"].astype(int)
    new_data["exchcd"] = new_data["exchcd"].astype(int)
    new_data["siccd"] = new_data["siccd"].astype(int)

    file_path = f"msf.parquet"
    existing_data = pd.read_parquet(file_path)

    # make sure date is in datetime format
    existing_data["date"] = pd.to_datetime(existing_data["date"])
    new_data["date"] = pd.to_datetime(new_data["date"])

    # Check for new data that is not already in the existing data
    new_data = new_data[~new_data["date"].isin(existing_data["date"])]
    new_data["date"] = pd.to_datetime(new_data["date"], format="%Y-%m-%d")

    if not new_data.empty:
        # Concatenate new data with existing data
        updated_data = pd.concat([existing_data, new_data], ignore_index=True)
        updated_data.to_parquet(file_path, index=False)
        note = "new data added"
        N = len(updated_data)
        max_date = updated_data["date"].max()
    else:
        note = "no new data"
        N = len(existing_data)
        max_date = existing_data["date"].max()

    diagnostic_row = pd.DataFrame(
        {
            "NUMOBS": [N],  # True if each CUSIP has only one associated PERMNO
            "Date Last Ran": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
            "Status": [note],
            "Max_Date": [max_date],
        }
    )

    try:
        summary_df = pd.read_csv("msf_diag.csv")
    except FileNotFoundError:
        summary_df = pd.DataFrame(columns=["NUMOBS", "Date Last Ran", "Max_Date", "Status"])

    # Append the new entry to the summary DataFrame
    summary_df = pd.concat([summary_df, diagnostic_row], ignore_index=True)

    # Save the updated summary DataFrame to the CSV file
    summary_df.to_csv("msf_diag.csv", index=False)
