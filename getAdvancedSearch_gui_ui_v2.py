import sys
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import *
from PyQt5 import uic
import getInfoFromApi
import kiprisPlus
import xml_advancedSerach
from PyQt5.QtGui import *


form_class = uic.loadUiType("getAdvancedSearch_v3.ui")[0]

class MyWindow(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #위젯 연결
        self.btn_search.clicked.connect(self.mark_search)



    def mark_search(self):
        # le_trademarkName = self.le_trademarkName.text()
        # le_asignProduct = self.le_asignProduct.text()
        # le_applicantName = self.le_applicantName.text()
        # le_classification = self.le_classification.text()
        # le_similarityCode = self.le_similarityCode.text()
        # le_viennaCode = self.le_viennaCode.text()
        # le_regPrivilegeName = self.le_regPrivilegeName.text()
        # le_agentName = self.le_agentName.text()
        # le_applicationNumber = self.le_applicationNumber.text()
        # le_registerNumber = self.le_registerNumber.text()
        # le_left_applicationDate = self.le_left_applicationDate.text()
        # le_right_applicationDate = self.le_right_applicationDate.text()
        # le_lefr_registerDate = self.le_lefr_registerDate.text()
        # le_right_registerDate = self.le_right_registerDate.text()
        # le_freeSearch = self.le_freeSearch.text()
        #
        # query = {
        #     "trademarkName": le_trademarkName,
        #     "classification": le_classification,
        #     "asignProduct": le_asignProduct,
        #     "applicationNumber": le_applicationNumber,
        #     "registerNumber": le_registerNumber,
        #     "publicationNumber": "",
        #     "registrationPublicNumber": "",
        #     "internationalRegisterNumber": "",
        #     "priorityNumber": "",
        #     "applicationDate": le_left_applicationDate + "~" + le_right_applicationDate,
        #     "registerDate": le_lefr_registerDate + "~" + le_right_registerDate,
        #     "publicationDate": "",
        #     "registrationPublicDate": "",
        #     "priorityDate": "",
        #     "internationalRegisterDate": "",
        #     "applicantName": le_applicantName,
        #     "agentName": le_agentName,
        #     "viennaCode": le_viennaCode,
        #     "regPrivilegeName": le_regPrivilegeName,
        #     "freeSearch": le_freeSearch,
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
        #
        # params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding="UTF-8", errors=None)
        # url = api + "?" + params + "&ServiceKey=" + service_key
        # request = urllib.request.urlopen(url)
        # xml = request.read()

        xml = xml_advancedSerach.xml
        soup = BeautifulSoup(xml, 'html.parser')
        items = soup.select("item")
        for item in items[:2]:

            #mark layout
            lb_img = QLabel("")
            lb_indexno = QLabel("")
            lb_title = QLabel("")
            lb_applicantName = QLabel("")
            lb_applicationstatus = QLabel("")
            lb_applicationnumber = QLabel("")
            lb_applicationDate = QLabel("")

            left_vbox = QVBoxLayout()
            left_vbox.addWidget(lb_img)
            middle_vbox = QVBoxLayout()
            middle_vbox.addWidget(lb_indexno)
            middle_vbox.addWidget(QLabel('출원인'))
            middle_vbox.addWidget(QLabel('상태'))
            middle_vbox.addWidget(QLabel('출원번호'))
            middle_vbox.addWidget(QLabel('출원일'))
            right_vbox = QVBoxLayout()
            right_vbox.addWidget(lb_title)
            right_vbox.addWidget(lb_applicantName)
            right_vbox.addWidget(lb_applicationstatus)
            right_vbox.addWidget(lb_applicationnumber)
            right_vbox.addWidget(lb_applicationDate)
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
            lb_img.setPixmap(qPixmapWebVar)
            # 다른정보들
            lb_indexno.setText(item.select_one("indexno").text)
            lb_title.setText(item.select_one("title").text)
            lb_applicantName.setText(item.select_one("applicantName").text)
            lb_applicationstatus.setText(item.select_one("applicationstatus").text)
            lb_applicationnumber.setText(item.select_one("applicationnumber").text)
            lb_applicationDate.setText(item.select_one("applicationDate").text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    exit(app.exec())
applicationDate_Label