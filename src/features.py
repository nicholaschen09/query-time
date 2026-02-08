import pandas as pd
import os

from dotenv import load_dotenv                        

load_dotenv()

DATA_PATH = os.getenv('DATA_PATH')

df = pd.read_csv(DATA_PATH)
print(df)
