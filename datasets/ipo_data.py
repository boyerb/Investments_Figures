import gdown
import pandas as pd

from .dataset import DATA_DIR, Dataset

RAW_FILE_PATH = DATA_DIR + "/ipo_data.csv"
CLEAN_FILE_PATH = DATA_DIR + "/ipo_data.parquet"


class IPOData(Dataset):
    """
    IPO data from Jay R. Ritter.
    """

    def __init__(self, RAW_FILE_PATH=RAW_FILE_PATH, CLEAN_FILE_PATH=CLEAN_FILE_PATH) -> None:
        super().__init__(RAW_FILE_PATH, CLEAN_FILE_PATH)

    def download(self):
        file_id = "1NglwsXleT99STRk9rm8qNg7crfil9-2D"
        url = f"https://drive.google.com/uc?id={file_id}"

        gdown.download(url, RAW_FILE_PATH, quiet=False)

    def clean(self):
        df = pd.read_csv(RAW_FILE_PATH)
        df.to_parquet(CLEAN_FILE_PATH)
