# -*- coding:utf-8 -*-
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
fh = logging.FileHandler('log/app.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

class App:
    '''
    第五种，异常用的最多
    '''
    muffled = False
    def calc(self,expr):
        '''
        捕捉异常
        :param expr:
        :return:
        '''
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print 'Division by zero is illegal'
            else:
                raise #抛出异常，程序终止运行
                print 'continus'


    def calc2(self):
        while True:
            try:
                x = input('Enter the first number:')
                y = input('Enter the second number:')
                value = x/y
            except:
                print 'Invalid input. Please try again.--------------'
            else:
                break

    def calc3(self):
        '''
        用一个块捕捉多个类型异常，这个块可以作为元组
        捕捉异常，程序可以正常执行
        :return:
        '''
        try:
            x = input('Enter the first number:')
            y = input('Enter the second number:')
            print x/y
        except(ZeroDivisionError,TypeError ,NameError):
            print 'Your numbers were bogus...'

    def calc4(self):
        '''
        用一个块捕捉多个类型异常，这个块可以作为元组
        打印异常信息
        :return:
        '''
        try:
            x = input('Enter the first number:')
            y = input('Enter the second number:')
            print x/y
        except(ZeroDivisionError,TypeError ,NameError),e:
            print e

    def calc5(self):
        '''
        用一个块捕捉多个类型异常，这个块可以作为元组
        打印异常信息
        :return:
        '''
        logging.info('2')

        try:
            x = input('Enter the first number:')
            y = input('Enter the second number:')
            print x/y
        except Exception,e:
            # print 'Something wrong happened...'
            print e #打印异常信息，程序正常运行
            logger.info(e)

if __name__ == '__main__':
    app = App()
    # app.muffled = True
    # app.calc('10/0')

    # app.calc2()
    # app.calc3()
    # app.calc4()
    app.calc5()
