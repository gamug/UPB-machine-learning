import os, pickle
import pandas as pd
from typing import Any


def get_config_vars() -> dict[str, Any]:
    config_vars = dict()
    config_vars['pages'] = ["Readme", "Model", "Model Metrics", "Data"]
    with open(os.path.join('files', 'html_content', 'readme.html'), mode='r', encoding='utf-8') as f:
        config_vars['readme'] = f.read()
    config_vars['models'] = [file.split('.')[0] for file in os.listdir(os.path.join('models', 'pickles'))]
    config_vars['models'].remove('LabelEncoder')
    config_vars['datasets'] = ['Raw', 'Precurated', 'Curated']
    config_vars['datasets_disposables'] = ['Data', 'Profiling']
    mode_metrics = pd.read_csv(os.path.join('models', 'metrics', 'metrics.csv'))
    config_vars['model_metrics'] = mode_metrics.groupby('model').mean().sort_values('roc', ascending=False).round(2)
    return config_vars

def get_metrics_plot(model: str, typ: str) -> str:
    with open(os.path.join('models', 'metrics', f'{typ}-{model}.html'), mode='r', encoding='utf-8') as f:
        html = f.read()
    return html

def charge_models(model: str) -> tuple:
    with open(os.path.join('models', 'pickles', f'{model}.pkl'), mode='rb') as f:
        pipeline = pickle.loads(f.read())
    with open(os.path.join('models', 'pickles', 'LabelEncoder.pkl'), mode='rb') as f:
        le = pickle.loads(f.read())
    return le, pipeline