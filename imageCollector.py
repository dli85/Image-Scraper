from bs4 import BeautifulSoup
import requests
import shutil
import os
import PIL

class imageCollector:
    def __init__(self, link, path):
        self.link = link
        self.path = path
        self.tempPath = self.path + '\\temp\\'
        self.soupData = BeautifulSoup(requests.get(link).text, 'html.parser')
        self.title = self.soupData.findAll('h1')[0].getText().replace(',', '')
        print(self.title)

        self.imageLinks = []

        for i in self.soupData.find_all('img'):
            self.imageLinks.append(i['src'])

    def deleteTemp(self):
        shutil.rmtree(self.tempPath)

    def downloadImages(self):

        if not os.path.exists(self.tempPath):
            os.makedirs(self.tempPath)

        for i in range(len(self.imageLinks)):
            currentImageLink = self.imageLinks[i]
            currFileName = str(i+1)

            saveImagePathComplete = self.tempPath + currFileName + '.jpg'

            r = requests.get(currentImageLink, stream = True)
            if r.status_code == 200:
                r.raw.decode_content = True

                with open(saveImagePathComplete, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)


    def imgToPdf(self):
        picturesList = os.listdir(self.tempPath)

        for i in range(len(picturesList)):
            picturesList[i] = picturesList[i].replace('.jpg', '')

        picturesList.sort(key=int)

        for i in range(len(picturesList)):
            picturesList[i] = picturesList[i] + '.jpg'

        print(picturesList)
