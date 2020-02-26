import sys
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import *
from PyQt5 import uic
import getInfoFromApi
import kiprisPlus
import xml_test
from PyQt5.QtGui import *


form_class = uic.loadUiType("gui_ui_getAdvancedSearch_v2.ui")[0]

class MyWindow(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #위젯 연결
        self.btn_search.clicked.connect(self.mark_search)



    def mark_search(self):
          # le_trademarkName = self.le_trademarkName.text()
        # le_similarityCode = self.le_similarityCode.text()
        # self.textBrowser_searched.clear()
        # query = {
        #     "trademarkName": le_trademarkName,
        #     "classification": "",
        #     "asignProduct": "",
        #     "applicationNumber": "",
        #     "registerNumber": "",
        #     "publicationNumber": "",
        #     "registrationPublicNumber": "",
        #     "internationalRegisterNumber": "",
        #     "priorityNumber": "",
        #     # "applicationDate": applicationDate_le,
        #     "registerDate": "",
        #     "publicationDate": "",
        #     "registrationPublicDate": "",
        #     "priorityDate": "",
        #     "internationalRegisterDate": "",
        #     "applicantName": "",
        #     "agentName": "",
        #     "viennaCode": "",
        #     "regPrivilegeName": "",
        #     "freeSearch": "",
        #     "similarityCode": le_similarityCode,
        #     "application": "true",
        #     "registration": "true",
        #     "refused": "true",
        #     "expiration": "true",
        #     "withdrawal": "true",
        #     "publication": "true",
        #     "cancel": "true",
        #     "abandonment": "true",
        #     "trademark": "true",
        #     "serviceMark": "true",
        #     "trademarkServiceMark": "true",
        #     "businessEmblem": "true",
        #     "collectiveMark": "true",
        #     "internationalMark": "true",
        #     "character": "true",
        #     "figure": "true",
        #     "compositionCharacter": "true",
        #     "figureComposition": "true",
        #     "numOfRows": "20",
        #     "pageNo": "1"
        # }
        # api = kiprisPlus.api_getAdvancedSearch
        # service_key = kiprisPlus.service_key
        # params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding="UTF-8", errors=None)
        # url = api + "?" + params + "&ServiceKey=" + service_key
        # request = urllib.request.urlopen(url)
        # xml = request.read()
        xml = xml_test.xml
        soup = BeautifulSoup(xml, 'html.parser')
        items = soup.select("item")
        for item in items[:1]:

            # one mark layout
            img_Label = QLabel("")
            indexno_Label = QLabel("")
            title_Label = QLabel("")
            applicantName_Label = QLabel("")
            applicationstatus_Label = QLabel("")
            applicationnumber_Label = QLabel("")
            applicationDate_Label = QLabel("")

            left_vbox = QVBoxLayout()
            left_vbox.addWidget(img_Label)
            middle_vbox = QVBoxLayout()
            middle_vbox.addWidget(indexno_Label)
            middle_vbox.addWidget(QLabel('출원인'))
            middle_vbox.addWidget(QLabel('상태'))
            middle_vbox.addWidget(QLabel('출원번호'))
            middle_vbox.addWidget(QLabel('출원일'))
            right_vbox = QVBoxLayout()
            right_vbox.addWidget(title_Label)
            right_vbox.addWidget(applicantName_Label)
            right_vbox.addWidget(applicationstatus_Label)
            right_vbox.addWidget(applicationnumber_Label)
            right_vbox.addWidget(applicationDate_Label)
            hbox = QHBoxLayout()
            hbox.addLayout(left_vbox)
            hbox.addLayout(middle_vbox)
            hbox.addLayout(right_vbox)

            self.groupBox.setLayout(hbox)

            # Web에서 Image 정보 로드, 웹에서 Load한 Image를 이용하여 QPixmap에 사진데이터를 Load하고, Label을 이용하여 화면에 표시
            urlString = item.select_one("drawing").text
            imageFromWeb = urllib.request.urlopen(urlString).read()
            qPixmapWebVar = QPixmap()
            qPixmapWebVar.loadFromData(imageFromWeb)
            img_Label.setPixmap(qPixmapWebVar)
            # 다른정보들
            indexno_Label.setText(item.select_one("indexno").text)
            title_Label.setText(item.select_one("title").text)
            applicantName_Label.setText(item.select_one("applicantName").text)
            applicationstatus_Label.setText(item.select_one("applicationstatus").text)
            applicationnumber_Label.setText(item.select_one("applicationnumber").text)
            applicationDate_Label.setText(item.select_one("applicationDate").text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    exit(app.exec())
applicationDate_Label