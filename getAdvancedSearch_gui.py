import sys
from PyQt5.QtWidgets import *
import requests
from bs4 import BeautifulSoup
import getInfoFromApi


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.trademarkName_le = QLineEdit()
        self.trademarkName_le.setPlaceholderText('trademarkName 예>clip')
        # self.applicationDate_le = QLineEdit()
        # self.applicationDate_le.setPlaceholderText('applicationDate')
        self.similarityCode_le = QLineEdit()
        self.similarityCode_le.setPlaceholderText('similarityCode 예>G2601')

        self.btn = QPushButton('Search')
        self.btn.clicked.connect(self.mark_search)

        self.lbl = QLabel('')

        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)

        grid = QGridLayout()
        grid.addWidget(self.trademarkName_le, 0, 0, 1, 3)
        # grid.addWidget(self.applicationDate_le, 1, 0, 1, 3)
        grid.addWidget(self.similarityCode_le, 2, 0, 1, 3)
        grid.addWidget(self.btn, 2, 3, 1, 1)
        grid.addWidget(self.lbl, 3, 0, 1, 4)
        grid.addWidget(self.tb, 4, 0, 1, 4)

        self.setLayout(grid)

        self.setWindowTitle('Mark Search')
        self.setGeometry(100, 100, 700, 450)
        self.show()

    def mark_search(self):
        trademarkName_le = self.trademarkName_le.text()
        # applicationDate_le = self.applicationDate_le.text()
        similarityCode_le = self.similarityCode_le.text()

        self.lbl.setText('Search Results for "' + trademarkName_le + '"')
        self.tb.clear()

        query = {
            "trademarkName": trademarkName_le,
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
            "similarityCode": similarityCode_le,
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
        i = 0
        for item in items:
            applicationnumber = item.select_one("applicationnumber").text
            title = item.select_one("title").text

            self.tb.append(str(i) + '번: ')
            self.tb.append('상표명: ' + title)
            self.tb.append('출원번호: ' + applicationnumber)
            i+=1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())