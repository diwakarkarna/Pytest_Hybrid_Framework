import logging
import platform


class Logger:
    @staticmethod
    def logger():

        if platform.system() == "Windows":
            logging.basicConfig(filename="Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                            force=True)
        elif platform.system() == "Linux":

            logging.basicConfig(filename="./Logs/automation.log",
                                format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                                force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger