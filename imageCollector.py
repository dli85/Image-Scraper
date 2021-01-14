from bs4 import BeautifulSoup
import requests
import shutil
import os
from PIL import Image

class imageCollector:
    def __init__(self, link, path):
        self.link = link
        self.path = path
        self.tempPath = self.path + '\\temp\\'
        self.soupData = BeautifulSoup(requests.get(link).text, 'html.parser')
        self.title = self.soupData.findAll('h1')[0].getText().replace(',', '')

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

        #print(picturesList)

        PILList = []

        initImg = Image.open(self.tempPath + picturesList[0])

        for i in range(1, len(picturesList)):
            curImg = Image.open(self.tempPath + picturesList[i])
            PILList.append(curImg)

        #print(self.path + '\\' + self.title + '.pdf')

        initImg.save(self.path + '\\' + self.title + '.pdf', "PDF", resolution=100.0, save_all=True, append_images=PILList)

        #TODO take the list of images and convert them into a pdf (https://datatofish.com/images-to-pdf-python/)
        #TODO don't forget to add the complete path first, self.tempPath + picturesList[i]
        #TODO also store the pdf in the self.path folder, not the self.tempPath folder

