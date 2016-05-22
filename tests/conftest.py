import pytest

def pytest_addoption(parser):
    parser.addoption('--username', action='store', help='username for NFLGSIS')
    parser.addoption('--password', action='store', help='username for NFLGSIS')
    parser.addoption('--runslow', action='store_true', help='runs slow tests')

@pytest.fixture
def username(request):
    return request.config.getoption('--username')

@pytest.fixture
def password(request):
    return request.config.getoption('--password')
