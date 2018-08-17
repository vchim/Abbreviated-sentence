#-*-coding:utf-8-*-
'''
    Vinson 17 Aug 2018
'''

import codecs
import jieba.posseg as pseg
from PreSelect import PreSelect
from Deep_Select import start_end, position
import pandas as pd

def select_combine(file):
    target = PreSelect()
    SinSen = target.SinSen(file)
    ComSen = target.ComSen(file)
    DunSen = target.DunSen(file)
    ComDunSen = target.ComDunSen(file)
    DunComSen = target.DunComSen(file)
    sentences = SinSen + ComSen + DunSen + ComDunSen + DunComSen
    return sentences

def word_tag(list):

    list_word = []
    list_tag = []
    for i in list:
        words = pseg.cut(i)
        list1 = []
        list2 = []
        for word, tag in words:
            list1.append(word)
            list2.append(tag)
        list_word.append(list1)
        list_tag.append(list2)
    return list_word, list_tag

def list_2_series(list):
    s = pd.Series(list)
    return s

if __name__ == '__main__':

    file_1 = codecs.open('primaryschool_textbook_total.txt', "r", "utf-8").read()
    file_2 = codecs.open('primaryschool_writings_total.text', "r", "utf-8").read()

    file_1_sentences = select_combine(file_1)
    file_2_sentences = select_combine(file_2)

    sentences = file_1_sentences + file_2_sentences
    sentences_only = list(set(sentences)) # drop_duplicated sentences
    print '# of pre-selected sentences :',len(sentences_only)

    words, tags = word_tag(sentences_only)

    Sen_Tag = {}
    for i in range(len(sentences_only)):
        Sen_Tag[sentences_only[i]] = tags[i]

    keywords = ['n', 'nr', 'ns', 'nz', 'nrt', 'r', 'a']
    Sen_Tag = start_end(keywords, Sen_Tag.keys(), Sen_Tag)
    print '# of deep-selected sentences1.0 :', len(Sen_Tag)

    Sen_Tag = position(Sen_Tag.keys(), Sen_Tag)
    print '# of deep-selected sentences1.1 :', len(Sen_Tag)

    words_new, tags_new = word_tag(Sen_Tag.keys())

    result_sen = list_2_series(Sen_Tag.keys())
    result_tag = list_2_series(tags_new)
    result_word = list_2_series(words_new)
    result = pd.concat([result_sen, result_word, result_tag], axis=1)

    df = pd.DataFrame(result.values, columns=['sen', 'word', 'tag'])
    df = df.sort_values('sen')
    print df
    # df.to_csv('result_v12.csv', encoding='utf-8', index=False)

