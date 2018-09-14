import re

import jieba
import numpy as np
from collections import defaultdict
import pandas as pd


def stop_words_list(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


def write_(s, c, l):
    """把0，1，2，3，... 等字母代表的feature，转换成实体
    """
    print('=' * 50)
    print('Start writing...')

    support_sample_li = [[i[0][0], i[0][1], round(i[1], 6)] for i in s]
    confidence_sample_li = [[i[0][0], i[0][1], round(i[1], 6)] for i in c]
    lift_sample_li = [[i[0][0], i[0][1], round(i[1], 6)] for i in l]

    # 写入文件
    with open('./data_out/support.data', 'w', encoding='utf-8') as fs, \
            open('./data_out/confidence.data', 'w', encoding='utf-8') as fc, \
            open('./data_out/lift.data', 'w', encoding='utf-8') as fl:
        for a in support_sample_li:
            fs.write(str(a) + '\n')
        print('The file support.data is written...')

        for b in confidence_sample_li:
            word = b[0]

            fc.write(str(b) + '\n')
        print('The file confidence.data is written...')

        for d in lift_sample_li:
            fl.write(str(d) + '\n')
        print('The file lift.data is written...')


def calculate(file):
    support_dict = defaultdict(float)
    confidence_dict = defaultdict(float)
    lift_dict = defaultdict(float)

    with open(file, 'r', encoding='utf-8') as f:
        # with open('./data/feature_times_di.sql', 'w', encoding='utf-8') as f2:
            together_appear_dict = defaultdict(int)
            feature_num_dict = defaultdict(int)
            content_li = f.readlines()
            n_samples = len(content_li)
            for ind, item in enumerate(content_li):
                if ind % 10000 == 0:
                    print('Currently processed====', ind/10000, '万====line data...')
                line_li = list(jieba.cut(item.strip()))
                # print(line_li)
                # line_li = list(set(line_li)-set(stop_word))

                # 有方向的数据理解
                # print(line_li)
                # for index_1, item_1 in enumerate(line_li):
                #     feature_num_dict[item_1] += 1
                #     if index_1 >= len(line_li)-1:
                #         continue
                #     if (item_1 not in stop_word) and (line_li[index_1+1] not in stop_word):
                #         tp = (item_1, line_li[index_1 + 1])
                #         together_appear_dict[tp] += 1
                #
                # for index_2, item_2 in enumerate(line_li):
                #     if index_2 > 1:
                #         new_item = ''.join(line_li[:index_2])
                #         behind_new_item = line_li[index_2]
                #         tp_2 = (new_item, behind_new_item)
                #         feature_num_dict[new_item] += 1
                #         together_appear_dict[tp_2] += 1

                # for index_3, item_3 in enumerate(line_li):
                #     if index_3 > 0:
                #         new_item_3 = ''.join(line_li[:index_3])
                #         behind_item_3 = ''.join(line_li[index_3:])
                #         tp_3 = (new_item_3, behind_item_3)
                #
                #         feature_num_dict[new_item_3] += 1
                #         feature_num_dict[behind_item_3] += 1
                #         together_appear_dict[tp_3] += 1

                # 全切分
                line_li = ''.join(line_li)
                for index_4, item_4 in enumerate(line_li):
                    if index_4 > 0:
                        behind_item_4 = ''.join(line_li[index_4:])

                        feature_num_dict[line_li] += 1

                        split_item = ''.join(line_li[:index_4])
                        for g, h in enumerate(split_item):
                            item = split_item[g:]

                            feature_num_dict[item] += 1

                            tp_4 = (item, line_li)
                            together_appear_dict[tp_4] += 1

                # # 按单词切分
                # for index_4, item_4 in enumerate(line_li):
                #     if index_4 > 0:
                #         behind_item_4 = ''.join(line_li[index_4:])
                #
                #         feature_num_dict[behind_item_4] += 1
                #
                #         split_item = line_li[:index_4]
                #         for g, h in enumerate(split_item):
                #             item = ''.join(split_item[g:])
                #
                #             feature_num_dict[item] += 1
                #
                #             tp_4 = (item, behind_item_4)
                #             together_appear_dict[tp_4] += 1

                # 没有方向的数据理解
                # for i in line_li:
                #     feature_num_dict[i] += 1
                #     for j in line_li:
                #         if i == j:
                #             continue
                #         else:
                #             tp = (i, j)
                #         # print(tp)
                #         together_appear_dict[tp] += 1
                #         # break

            # print(together_appear_dict)
            # print(feature_num_dict)
            print('Two dict is evaluated...')

            # 通过遍历together_appear_dict，计算出两两特征的支持度，置信度，提升度
            print('Start calculating...')
            num = 0
            for k, v in together_appear_dict.items():
                if num % 10000 == 0:
                    print('Calculated====', num/10000, '万==== data...')
                support_dict[k] = v / n_samples
                confidence_dict[k] = v / feature_num_dict[k[0]]
                # print(k[0],k[1])
                lift_dict[k] = v * n_samples / (feature_num_dict[k[0]] * feature_num_dict[k[1]])
                num += 1

            print('Data calculated...')
            return support_dict, confidence_dict, lift_dict


# def count_word(origin_file, stop_word):
#     with open(origin_file, encoding='utf-8') as f:
#         cont = f.read()
#         li = list(jieba.cut(cont))
#         # li = list(set(li)-set(stop_word))
#         di = defaultdict(int)
#
#         for word in li:
#             di[word] = di.get(word, 0) + 1
#
#         return di


if __name__ == '__main__':
    # 加载用户词典
    # 配置路径，如果数据没有经过处理，就配置origin_data_file
    # 如果数据已经经过处理，为0，1数据，就可以直接配置ready_data_file
    origin_data_file = './data/idioms.txt'
    # ready_data_file = './data/input_data/sample.data'

    # 如果数据已经构建好了，可以直接读取数组进行计算
    # data = pd.read_csv(ready_data_file)
    # data_array = np.array(data)

    # feature_di = create_feature_di(origin_data_file)
    # print(feature_di)
    support_di, confidence_di, lift_di = calculate(origin_data_file)

    # print('support_di: ', support_di)
    # print('confidence_di: ', confidence_di)
    # print('lift_di: ', lift_di)

    support = sorted(support_di.items(), key=lambda x: x[1], reverse=True)
    confidence = sorted(confidence_di.items(), key=lambda x: x[1], reverse=True)
    lift = sorted(lift_di.items(), key=lambda x: x[1], reverse=True)
    # print('support_li: ', support)
    # print('confidence_li: ', confidence)
    # print('lift_li: ', lift)

    # num_di = count_word(origin_data_file,stop_words)

    write_(support, confidence, lift)


