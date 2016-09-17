import os.path
import logging


class FileHandler(object):
    def __init__(self, file_path):
        self.__file_path = file_path

    def open_file(self):
        logging.info("Trying to find file: %s", self.__file_path)
        if os.path.isfile(self.__file_path):
            logging.info("File found: %s", self.__file_path)
            return open(self.__file_path, "r")

        logging.error("File cannot be found: %s", self.__file_path)

    def close_file(self, file):
        logging.info("Trying to close file: %s", self.__file_path)
        file.close()
        logging.info("File closed: %s", self.__file_path)
