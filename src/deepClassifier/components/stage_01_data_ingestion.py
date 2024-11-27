import os
import urllib.request as request
from zipfile import ZipFile
from deepClassifier import logger
from pathlib import Path
from tqdm import tqdm
from deepClassifier.entity import DataIngestionConfig
from deepClassifier.utils import utils


class DataIngestion:
    def __init__(self,config:data_ingestion_config):
        self.config = config

        pass
    def download_file(self):
        pass
    def get_updated_list_of_files(self):
        pass
    def preprocess(self):
        pass
    def unzip_and_clean(self):
        pass
    

