import pytest
import os
import yaml
from utils.request_handler import RequestHandler


@pytest.fixture(scope='session')
def config():
    config_paths = os.path.join(os.path.dirname(__file__), 'config', 'config.yaml')
    with open(config_paths) as f:
        cfg = yaml.safe_load(f)

    # env = os.getenv("TEST_ENV", "default")
    combined_cfg = {**cfg['default']}
    return combined_cfg


@pytest.fixture(scope='session')
def client(config):
    handler = RequestHandler(base_url=config['base_url'], headers=config.get('headers'), timeout=config['timeout'])
    if 'auth' in config:
        response = handler.post(config['auth']['endpoint'], json=config['auth']['payload'])
        response.raise_for_status()
        token = response.json().get('token')

    if token:
        handler.set_header('Authorization', token)
    yield handler
    handler.close()
