import os
from typing import Any


def get_config_vars() -> dict[str, Any]:
    config_vars = dict()
    config_vars['pages'] = ["Readme", "Model", "Model Metrics", "Data"]
    with open(os.path.join('files', 'html_content', 'readme.html'), mode='r', encoding='utf-8') as f:
        config_vars['readme'] = f.read()
    config_vars['models'] = [file.split('.')[0] for file in os.listdir(os.path.join('models', 'pickles'))]
    config_vars['datasets'] = ['Raw', 'Precurated', 'Curated']
    config_vars['datasets_disposables'] = ['Data', 'Profiling']
    return config_vars

def get_metrics_plot(model: str, typ: str) -> str:
    with open(os.path.join('models', 'metrics', f'{typ}-{model}.html'), mode='r', encoding='utf-8') as f:
        html = f.read()
    return html