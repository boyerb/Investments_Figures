import gdown
import pandas as pd

from .dataset import DATA_DIR, Dataset

RAW_FILE_PATH = DATA_DIR + "/points_per_game_raw.csv"
CLEAN_FILE_PATH = DATA_DIR + "/points_per_game_clean.parquet"


class PointsPerGame(Dataset):
    def __init__(self, RAW_FILE_PATH=RAW_FILE_PATH, CLEAN_FILE_PATH=CLEAN_FILE_PATH) -> None:
        super().__init__(RAW_FILE_PATH, CLEAN_FILE_PATH)

    def download(self):
        file_id = "1bQPUMdqgpNClK3Qql6NJS5Cf7Ej1B3xG"
        url = f"https://drive.google.com/uc?id={file_id}"

        gdown.download(url, RAW_FILE_PATH, quiet=False)

    def clean(self):
        # Raw file
        df = pd.read_csv(RAW_FILE_PATH, index_col=0)
        df.to_parquet(CLEAN_FILE_PATH)
