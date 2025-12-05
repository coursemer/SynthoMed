import os
import pandas as pd
from sdv.single_table import GaussianCopulaSynthesizer
from sdv.metadata import SingleTableMetadata
import kaggle

class DataEngine:
    def __init__(self, download_path='data/raw'):
        self.download_path = download_path
        if not os.path.exists(download_path):
            os.makedirs(download_path)

    def download_dataset(self, dataset_name):
        """
        Downloads a dataset from Kaggle.
        dataset_name: 'owner/dataset-slug' e.g. 'ronitf/heart-disease-uci'
        """
        try:
            kaggle.api.authenticate()
            kaggle.api.dataset_download_files(dataset_name, path=self.download_path, unzip=True)
            return True
        except Exception as e:
            print(f"Error downloading {dataset_name}: {e}")
            return False

    def generate_synthetic_data(self, csv_path, num_rows=100):
        """
        Generates synthetic data based on a CSV file.
        """
        try:
            real_data = pd.read_csv(csv_path)
            
            metadata = SingleTableMetadata()
            metadata.detect_from_dataframe(data=real_data)
            
            synthesizer = GaussianCopulaSynthesizer(metadata)
            synthesizer.fit(real_data)
            
            synthetic_data = synthesizer.sample(num_rows=num_rows)
            return synthetic_data
        except Exception as e:
            print(f"Error generating data: {e}")
            return None

# Example usage
if __name__ == "__main__":
    engine = DataEngine()
    # engine.download_dataset('ronitf/heart-disease-uci')
    # synthetic = engine.generate_synthetic_data('data/raw/heart.csv')
    # print(synthetic.head())
