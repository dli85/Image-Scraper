from imageCollector import imageCollector

def getLink():
    result = []

    firstq = input('Collect images from a single link? [y/n] ').lower()

    if(firstq == 'y'):
        result.append(input('Input link: '))
    elif(firstq == 'n'):
        path = input('Provide path to textfile which contains links (there must be one link on each line): ')

        file = open(path, 'r')

        line = file.readline().replace('\n', '')

        while line:
            result.append(line)
            line = file.readline().replace('\n', '')

    return result

if __name__ == '__main__':

    linklist = getLink()

    for i in linklist:
        current = imageCollector(i)

        input('press a key to continue')