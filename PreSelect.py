#-*-coding:utf-8-*-
''' This is a Class try to find some basic sentences by RE
    Vinson 17 Aug 2018
'''

import re

class PreSelect:
    '''Pre-select sentences from files'''

    def __init__(self):
        self.__list = []

    def SinSen(self, text):
        '''Single sentences end with full stop.
        11 characters
        '''
        self.__list = re.findall(u'。+([\u4E00-\u9FA5]{11,}。)', text)
        print '# of single sentence', len(self.__list)
        return self.__list

    def ComSen(self, text):
        '''Single sentences with a comma inside, end with full stop.
        xxxx,xxxxxxxx.
        '''
        # target = re.findall(u'。+([\u4E00-\u9FA5]+，[\u4E00-\u9FA5]+。)', text)
        self.__list = re.findall(u'。+([\u4E00-\u9FA5]{3,}，[\u4E00-\u9FA5]{8,}。)', text)
        print '# of comma sentence', len(self.__list)
        return self.__list

    def DunSen(self, text):
        '''Single sentences with a dunhao inside, end with full stop.
        xxxx`xxxxxxxx.
        '''
        # target = re.findall(u'。+([\u4E00-\u9FA5]+、[\u4E00-\u9FA5]+。)', text)
        self.__list = re.findall(u'。+([\u4E00-\u9FA5]{2,}、[\u4E00-\u9FA5]{2,}。)', text)
        print '# of dunhao sentence', len(self.__list)
        return self.__list

    def ComDunSen(self, text):
        '''xxxx,xxxx`xxxxx.'''
        self.__list = re.findall(u'。+([\u4E00-\u9FA5]{2,}，[\u4E00-\u9FA5]+、[\u4E00-\u9FA5]+。)', text)
        print '# of ComDun sentence', len(self.__list)
        return self.__list

    def DunComSen(self, text):
        '''xxxx`xxxx,xxxxx.'''
        self.__list = re.findall(u'。+([\u4E00-\u9FA5]{2,}、[\u4E00-\u9FA5]+，[\u4E00-\u9FA5]+。)', text)
        print '# of DunCom sentence', len(self.__list)
        return self.__list