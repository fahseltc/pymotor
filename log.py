import logging

def setup_logs():
    logging.basicConfig(level=logging.INFO)
    logging.info("Logging initialized")

def log(className):
    return logging.getLogger(className)