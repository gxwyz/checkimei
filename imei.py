import sys
import os

def CalcImeiChecksum(imei):
    # checksum = ''
    resultInt = 0

    if(len(imei) == 14):
        for i in range(len(imei)):
            a = imei[i]
            if(i % 2 == 1):#偶数位计算
                t = 2 * int(a) #偶数位乘以2
                a = t % 10 + t / 10 #分离2个数字并相加
            resultInt = int(a) + resultInt #如果是奇数直接将数字相加
        # print(resultInt)
        x = resultInt % 10 #个位
        # print(x)
        # y = int((resultInt % 100 - x) / 10) #十位
        # print(y)
        if(x == 0):
            checksum = imei + '0'
        else:
            checksum = imei + str(10 - x)
    elif (len(imei) > 14):
        checksum = 'Null_' + imei
        print(imei[0,14])
    elif (len(imei) < 14):
        checksum = '长度不够_' + imei
    return checksum


if __name__ == '__main__':
    #批量python imei.py in.txt out.txt
    # imei = '35611511099913'
    with open(sys.argv[1],'r',encoding='utf-8') as f:
        for imei in f:
            imei = imei.replace('\n','')
            imei = imei.replace(' ', '')
            print('输入imei：{}'.format(imei))
            # imei = imei.replace(' ','')
            with open(sys.argv[2],'a',encoding='utf-8') as f2:
                f2.write(CalcImeiChecksum(imei))
                print('输出imei：{}'.format(CalcImeiChecksum(imei)))
                # print(CalcImeiChecksum(imei))
                f2.write('\n')
                f2.close()
            print('*'*50)
        f.close()

