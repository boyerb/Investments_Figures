import gdown
import pandas as pd

from .dataset import DATA_DIR, Dataset

RAW_FILE_PATH = DATA_DIR + "/french_beta_portfolios_raw.csv"
CLEAN_FILE_PATH = DATA_DIR + "/french_beta_portfolios_clean.parquet"


class BetaPortfolios(Dataset):
    """
    Beta portfolios from Kenneth French data library.
    """

    def __init__(self, RAW_FILE_PATH=RAW_FILE_PATH, CLEAN_FILE_PATH=CLEAN_FILE_PATH) -> None:
        super().__init__(RAW_FILE_PATH, CLEAN_FILE_PATH)

    def download(self):
        file_id = "17EZ9qHcQoegialcImiJfeyd778PZE8n_"
        url = f"https://drive.google.com/uc?id={file_id}"

        gdown.download(url, RAW_FILE_PATH, quiet=False)

    def clean(self):
        df = pd.read_csv(RAW_FILE_PATH)

        # Year-month column
        df["mdt"] = pd.to_datetime(df["Date"], format="%Y%m").dt.strftime("%Y-%m")
        df = df.drop(columns=["Date", "Lo 20", "Qnt 2", "Qnt 3", "Qnt 4", "Hi 20"])

        columns = [
            "Lo 10",
            "2-Dec",
            "3-Dec",
            "4-Dec",
            "5-Dec",
            "6-Dec",
            "7-Dec",
            "8-Dec",
            "9-Dec",
            "Hi 10",
        ]

        # Rename decile columns
        df = df.rename(columns={col: f"port_{i+1}" for i, col in enumerate(columns)})

        # Reorder columns
        df = df[["mdt"] + df.columns.to_list()[:-1]]

        df.to_parquet(CLEAN_FILE_PATH)
