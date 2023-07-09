import os
import pandas as pd

class CSVLoader:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def load_files(self):
        files = os.listdir(self.folder_path)
        dataframes = []

        for file in files:
            if file.endswith('.csv'):
                #file_path = os.path.join(self.folder_path, file)
                #df = pd.read_csv(file_path)
                dataframes.append(file)

        return dataframes

# Usage example
folder_path = 'files'
loader = CSVLoader(folder_path=folder_path)
dataframes = loader.load_files()
print(dataframes)

# Access individual dataframes
#for i, df in enumerate(dataframes):
   # print(f"DataFrame {i+1}:")
   # print(df.head())
