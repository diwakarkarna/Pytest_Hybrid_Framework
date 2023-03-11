from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from utils.customlogger import Logger
from selenium.common.exceptions import *
import pytest


@pytest.fixture()
def setup():
    logger = Logger.logger()
    try:
        logger.info("**************************Driver is being initialized**********************")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        yield driver
        logger.info("**************************Driver is being closed**********************")
        driver.close()
        driver.close()
    except WebDriverException as e:
        logger.info("**************************Something went wrong**********************")
        logger.error(e.msg)
    except SessionNotCreatedException as e:
        logger.error(e.msg)
    except InvalidSessionIdException as e:
        logger.error(e.msg)

