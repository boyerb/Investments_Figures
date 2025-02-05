import gdown
import pandas as pd

from .dataset import DATA_DIR, Dataset

RAW_FILE_PATH = DATA_DIR + "/french_momentum_portfolios_raw.csv"
CLEAN_FILE_PATH = DATA_DIR + "/french_momentum_portfolios_clean.parquet"


class MomentumPortfolios(Dataset):
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

        columns = ["Lo PRIOR"] + [f"PRIOR {i}" for i in range(2, 10)] + ["Hi PRIOR"]

        # Rename decile columns
        df = df.rename(columns={col: f"port_{i+1}" for i, col in enumerate(columns)})

        # # Reorder columns
        df = df[["mdt"] + df.columns.to_list()[:-1]]

        df.to_parquet(CLEAN_FILE_PATH)
