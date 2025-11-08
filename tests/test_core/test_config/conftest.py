"""Фикстуры для тестирования APIConfig."""
import pytest
import tempfile
import os


@pytest.fixture
def env_file_content():
    """Содержимое тестового .env файла."""
    return """OZON_SELLER_CLIENT_ID=file_client
OZON_SELLER_API_KEY=file_key
OZON_SELLER_BASE_URL=https://file-api.ozon.ru
OZON_SELLER_MAX_REQUESTS_PER_SECOND=40
"""


@pytest.fixture
def temp_env_file(env_file_content):
    """Создает временный .env файл."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.env', delete=False) as f:
        f.write(env_file_content)
        temp_env_file = f.name

    yield temp_env_file
    os.unlink(temp_env_file)