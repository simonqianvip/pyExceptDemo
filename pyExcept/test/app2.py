# -*- coding:utf-8 -*-
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
fh = logging.FileHandler('../log/app2.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)


class App2:
    def app_test(self):
        print 'aaa'
        logger.info('aa')


if __name__ == '__main__':
    app_ = App2()
    app_.app_test()
