import inspect
import logging


class LogGenerator():
    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler("D:\\credence\\Parabank_pytest_project\\log\\register.log")
        log_format = logging.Formatter("%(asctime)s:%(levelno)s:%(name)s:%(funcName)s:%(lineno)d:%(message)s")
        logfile.setFormatter(log_format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger