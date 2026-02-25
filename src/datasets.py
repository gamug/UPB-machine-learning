import os
import pandas as pd
from typing import Any

def get_dataset_data(dataset: str, show: str) -> Any:
    if show=='Data':
        return pd.read_csv(os.path.join('files', 'data', 'datasets', f'salinity_{dataset.lower()}.csv'))
    elif show=='Profiling':
        with open(os.path.join('files', 'data', 'profiling', f'{dataset.lower()}-salinity_report.html'), mode='r') as f:
            html = f.read()
        return html
