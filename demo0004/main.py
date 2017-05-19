def findStr(key):
    count = 0
    with open('demo0004/novel.txt', 'r') as f:
        for line in f.readlines():
            count += line.strip().count(key)
    
    print('all \"' + key + '\" counts : ' + str(count))

if __name__ == '__main__':
    findStr('all')