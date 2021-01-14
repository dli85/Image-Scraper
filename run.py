from imageCollector import imageCollector

global saveLocation

def getLink():
    result = []

    firstq = input('Collect images from a ONLY single link? [y/n] ').lower()

    if(firstq == 'y'):
        result.append(input('Input link: '))
    elif(firstq == 'n'):
        path = input('Provide path to textfile which contains links (there must be one link on each line): ')

        file = open(path, 'r')

        line = file.readline().replace('\n', '')

        while line:
            result.append(line)
            line = file.readline().replace('\n', '')

        file.close()

    return result

def importSettings():
    global saveLocation

    try:
        file = open('settings.txt', 'r')
        useSettings = input('Settings file found! Use them? [y/n] ').lower()

        result = []

        if (useSettings == 'y'):
            firstq = file.readline().replace('\n', '')
            path = file.readline().replace('\n', '')
            saveLocation = file.readline().replace('\n', '')

            chapterListFile = open(path, 'r')

            line = chapterListFile.readline().replace('\n', '')

            while line:
                result.append(line)
                line = chapterListFile.readline().replace('\n', '')

            chapterListFile.close()

            return result

        else:
            return []
    except:
        return []

if __name__ == '__main__':
    global saveLocation

    linklist = importSettings()
    if len(linklist) == 0:
        linklist = getLink()

        saveLocation = input('Where would you like to save the output (enter a path): ')

    for i in linklist:
        current = imageCollector(i, saveLocation)
        current.downloadImages()

        current.imgToPdf()
        input()
        current.deleteTemp()
        input('press a key to continue')