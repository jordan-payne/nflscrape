from context import nflcollect
import pytest
import os

os.chdir('tests')

slow = pytest.mark.skipif(
    not pytest.config.getoption('--runslow'),
    reason='need --runslow option to run'
)

def test_get_driver():
    assert nflcollect.get_driver()

def test_login_nflgsis(username, password):
    driver = nflcollect.get_driver()
    driver = nflcollect.login_nflgsis(driver, username, password)
    assert driver.title == 'NFL GSIS'

@slow
def test_get_gamebooks_for_year(username, password):
    driver = nflcollect.get_driver()
    driver = nflcollect.login_nflgsis(driver, username, password)
    gamebooks = nflcollect.get_gamebooks_for_year(2015, driver)
    assert gamebooks != None

@slow
def test_write_gamebooks(username, password):
    driver = nflcollect.get_driver()
    driver = nflcollect.login_nflgsis(driver, username, password)
    gamebooks = nflcollect.get_gamebooks_for_year(2015, driver)
    nflcollect.write_gamebooks(gamebooks)

def test_derive_gamebook_name():
    name = nflcollect.derive_gamebook_name('http://nflgsis.com/2014/Reg/01/56170/Gamebook.pdf')
    assert name == '56170'
