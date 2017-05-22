def calculateFat():
    sex = input('性别(男/女 M/W)：')
    waist = float(input('腰围(cm)：'))
    weight = float(input('体重(kg)：'))

    if (sex == 'M'):
        result = (waist * 0.74 - weight * 0.082 - 44.74) / weight * 100
        print('您的体脂率：%.2f' % result + '%')
    elif (sex == 'W'):
        result = (waist * 0.74 - weight * 0.082 - 34.89) / weight * 100
        print('您的体脂率：%.2f' % result + '%')
    else:
        print('不男不女...')

if __name__ == '__main__':
    calculateFat()