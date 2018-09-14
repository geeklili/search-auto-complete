from collections import defaultdict


def create_dict():
    di = defaultdict(list)
    with open('./data_out/confidence.data', 'r', encoding='utf-8') as f1:
        cont = f1.readlines()
        for i in cont:
            line_li = eval(i)
            one = line_li[0]
            two = line_li[1]
            three = line_li[2]

            tp = (two, three)
            di[one].append(tp)

    with open('./data_out/predict.data', 'w', encoding='utf-8') as f2:
        f2.write(str(dict(di)))


def read_predict_dict(word):
    with open('./data_out/predict.data', 'r', encoding='utf-8') as f3:
        di = eval(f3.read())
        ret = di.get(word, list())
        li = sorted(ret, key=lambda x:x[1], reverse=True)
        print(li[:5])


if __name__ == '__main__':
    create_dict()

