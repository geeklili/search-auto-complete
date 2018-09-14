import re

with open('./data/origin_data.txt', encoding='utf-8') as f:
    with open('./data/idioms.txt', 'w', encoding='utf-8') as f2:
        for i in f:
            try:
                a = re.findall('（.*?）', i)[0].replace('）', '').replace('（', '')
                print(a)
                f2.write(a+'\n')
            except:
                pass
