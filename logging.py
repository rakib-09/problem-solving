import logging


class Logger:

    def __init__(self):
        logging.basicConfig(filename='test.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)
        logging.info('We are calling our add function.')
        logging.info('add function executed, task completed.')
        logging.info('We are calling our is_even funcion.')
        logging.info('is_even function executed, task completed.')


if __name__ == '__main__':
    log = Logger()