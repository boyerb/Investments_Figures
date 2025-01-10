import gdown
import pandas as pd

from .dataset import DATA_DIR, Dataset

RAW_FILE_PATH = DATA_DIR + "/CH7_7.3.1_data_raw.csv"
CLEAN_FILE_PATH = DATA_DIR + "/CH7_7.3.1_data_clean.parquet"


class CH7_731(Dataset):
    def __init__(self, RAW_FILE_PATH=RAW_FILE_PATH, CLEAN_FILE_PATH=CLEAN_FILE_PATH) -> None:
        super().__init__(RAW_FILE_PATH, CLEAN_FILE_PATH)

    def download(self):
        file_id = "15lJQ7NP-sVFAcWGbdM314QwPei1iRU7k"
        url = f"https://drive.google.com/uc?id={file_id}"

        gdown.download(url, RAW_FILE_PATH, quiet=False)

    def clean(self):
        # Raw file
        df = pd.read_csv(RAW_FILE_PATH, index_col=0)
        df.to_parquet(CLEAN_FILE_PATH)
