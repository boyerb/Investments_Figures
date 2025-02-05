import gdown
import pandas as pd

from .dataset import DATA_DIR, Dataset

RAW_FILE_PATH = DATA_DIR + "/fama_french_factors_raw.csv"
CLEAN_FILE_PATH = DATA_DIR + "/fama_french_factors_clean.parquet"


class FamaFrenchFactors(Dataset):
    """
    Factor data from Fama and French.
    """

    def __init__(self, RAW_FILE_PATH=RAW_FILE_PATH, CLEAN_FILE_PATH=CLEAN_FILE_PATH) -> None:
        super().__init__(RAW_FILE_PATH, CLEAN_FILE_PATH)

    def download(self):
        file_id = "17EZ9qHcQoegialcImiJfeyd778PZE8n_"
        url = f"https://drive.google.com/uc?id={file_id}"

        gdown.download(url, RAW_FILE_PATH, quiet=False)

    def clean(self):
        df = pd.read_csv(RAW_FILE_PATH)

        # Year month column
        df["mdt"] = pd.to_datetime(df["DATE"], format="%Y%m").dt.strftime("%Y-%m")

        # Drop DATE column
        df = df.drop(columns=["DATE"])

        # Rename columns
        df = df.rename(columns={col: col.replace("-", "_").lower() for col in df.columns})

        # Reorder columns
        df = df[["mdt"] + df.columns.to_list()[:-1]]

        # Add mkt column
        df["mkt"] = df["mkt_rf"] - df["rf"]

        df.to_parquet(CLEAN_FILE_PATH)
