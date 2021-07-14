# -*- coding: UTF-8 -*-

from lxml import etree


def parseXml(ParseFunc, inFile="", outFile="", **kwargs):
    ns = '{http://www.drugbank.ca}'
    count = 0
    print('解析开始---------------------------')

    with open(outFile, 'w') as out:
        for event, drug in etree.iterparse(inFile, events=('end',), tag=ns+'drug'):

            # 条件一判断
            if (drug.get('type') != 'small molecule'):
                continue

            # 条件二判断
            flag = False
            groups = drug.find(ns + 'groups')
            for group in groups.iter(ns + 'group'):
                if(group.text == 'approved'):
                    flag = True
                    break
            if (not flag):
                continue

            result_str = ''
            # 当前drug的id
            drug_act=drug.find(ns+'atc-codes')
            if(drug_act==None or len(drug_act)==0):
                drug_Act=" "
            else:
                drug_Act=drug_act[0].get('code')
                print(drug_Act)
            drug_pri_id = drug.find(ns + 'drugbank-id').text

            # 解析当前drug 得到输出的字符串
            result_str = ParseFunc(
                drug_Act=drug_Act,drugElement=drug, drug_pri_id=drug_pri_id, ns=ns, **kwargs)

            # 清理引用，减少内存占用
            drug.clear()
            while drug.getprevious() is not None:
                del drug.getparent()[0]

            # 写入文件
            out.write(result_str)

            # 记数
            count += 1
            print(count)
            # if(count == 10):
            #     return 0
    print('解析结束---------------------------')

def parseInteraction(drug_Act,drugElement, drug_pri_id, ns):
    result_str = ''
    drug_interactions = drugElement.find(ns + 'drug-interactions')
    result_str += drug_pri_id + ' ' + drug_Act + "\n"
    # for drug_interaction in drug_interactions.iter(ns + 'drug-interaction'):
    #     # 拼装字符串
    #     result_str += drug_pri_id + ' ' + drug_Act + "\n"
    #
    #     # 药物相互作用的说明
    #     # result_str += drug_interaction[2].text
    #
    #     # increase 为1, decrease 为-1
    #     # if (drug_interaction[2].text.find('increase') != -1):
    #     #     result_str += '1'
    #     # elif (drug_interaction[2].text.find('decrease') != -1 or drug_interaction[2].text.find('reduce') != -1):
    #     #     result_str += '-1'
    #     # else:
    #     #     result_str += drug_interaction[2].text
    #     #
    #     # result_str += '\n'
    return result_str


def parsePolypeptide(drugElement, drug_pri_id, ns, lableName=""):
    result_str = ''
    lables = drugElement.find(ns + lableName)
    for lable in lables.iter(ns + lableName[0:-1]):
        result_str += drug_pri_id + ' '

        polypeptide = lable.find(ns + 'polypeptide')
        if (polypeptide is not None):
            result_str += polypeptide.get('id') + ' '
        else:
            result_str += ' ' * 6 + ' '

        for action in lable.find(ns + 'actions').iter(ns + 'action'):
            result_str += action.text + '/ '

        result_str += '\n'
    return result_str


if __name__ == '__main__':
    # lableNames = ['targets', 'enzymes', 'carriers', 'transporters']
    # for lableName in lableNames:
    #     parseXml(parsePolypeptide,
    #             inFile="full database.xml",
    #             outFile='drug_polypeptide_' + lableName + '.txt',
    #             lableName=lableName)
    parseXml(parseInteraction, inFile='C:/Users/82533/Desktop/fulldatabase.xml', outFile='C:/Users/82533/Desktop/act.txt')
    print('done')
