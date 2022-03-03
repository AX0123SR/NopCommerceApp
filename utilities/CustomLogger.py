import logging

class LogGen:

    @staticmethod
    def logGen():
        # logging.basicConfig(filename=".",
        #                      format="%(asctime)s: %(levelname)s: %(message)s", datefmt="%m/%d/%y %I:%M:%S, %p")
        # logger = logging.getLogger()
        # logger.setLevel(logging.INFO)
        # return logger

        logger = logging.getLogger()
        fileHandler = logging.FileHandler('.//Logs//logfile.log')
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s", datefmt="%m/%d/%y %I:%M:%S, %p")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger

