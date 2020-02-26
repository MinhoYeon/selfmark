import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import getInfoFromApi

form_class = uic.loadUiType("gui_ui_getAdvancedSearch.ui")[0]

class MyWindow(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #위젯 연결
        self.btn_search.clicked.connect(self.mark_search)

    #위젯에 연결된 함수
    def mark_search(self):
        le_trademarkName = self.le_trademarkName.text()
        # applicationDate_le = self.applicationDate_le.text()
        le_similarityCode = self.le_similarityCode.text()

        self.textBrowser_searched.clear()

        query = {
            "trademarkName": le_trademarkName,
            "classification": "",
            "asignProduct": "",
            "applicationNumber": "",
            "registerNumber": "",
            "publicationNumber": "",
            "registrationPublicNumber": "",
            "internationalRegisterNumber": "",
            "priorityNumber": "",
            # "applicationDate": applicationDate_le,
            "registerDate": "",
            "publicationDate": "",
            "registrationPublicDate": "",
            "priorityDate": "",
            "internationalRegisterDate": "",
            "applicantName": "",
            "agentName": "",
            "viennaCode": "",
            "regPrivilegeName": "",
            "freeSearch": "",
            "similarityCode": le_similarityCode,
            "application": "true",
            "registration": "true",
            "refused": "true",
            "expiration": "true",
            "withdrawal": "true",
            "publication": "true",
            "cancel": "true",
            "abandonment": "true",
            "trademark": "true",
            "serviceMark": "true",
            "trademarkServiceMark": "true",
            "businessEmblem": "true",
            "collectiveMark": "true",
            "internationalMark": "true",
            "character": "true",
            "figure": "true",
            "compositionCharacter": "true",
            "figureComposition": "true",
            "numOfRows": "20",
            "pageNo": "1"
        }
        soup = getInfoFromApi.getAdvancedSearch(query)
        items = soup.select("item")
        i = 1
        for item in items:
            applicationnumber = item.select_one("applicationnumber").text
            title = item.select_one("title").text
            self.textBrowser_searched.append(str(i) + '번: ')
            self.textBrowser_searched.append('상표명: ' + title)
            self.textBrowser_searched.append('출원번호: ' + applicationnumber)
            i+=1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec()
