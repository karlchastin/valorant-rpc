import logging, os

class Logger:
    # Dossier du projet (là où tu lances main.py) = où sont écrits les logs
    _LOG_DIR = os.path.abspath(".")

    @staticmethod
    def create_logger():
        log_path = os.path.join(Logger._LOG_DIR, "rpc.log")
        logging.basicConfig(
            filename=log_path,
            filemode="a",
            format="%(asctime)s.%(msecs)d %(name)s %(levelname)s %(message)s",
            datefmt="%H:%M:%S",
            level=logging.DEBUG,
        )
        logger = logging.getLogger("rpc")
        logger.debug("created log")

    @staticmethod 
    def debug(data):
        logger = logging.getLogger('rpc')
        logger.debug(data)