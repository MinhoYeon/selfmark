import sys
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import *
from PyQt5 import uic
import kiprisPlus
import xml_test
from PyQt5.QtGui import *


form_class = uic.loadUiType("getAdvancedSearch_v3.ui")[0]
form_class2 = uic.loadUiType("asignproductsearchinfo.ui")[0]
form_class3 = uic.loadUiType("one_mark.ui")[0]


class OpenApplicationnumber(QWindow, form_class3):
    def __init__(self, parent=None):
        super(OpenApplicationnumber, self).__init__(parent)
        self.setupUi(self)

        # xml = xml_test.xml
        # soup = BeautifulSoup(xml, 'html.parser')
        # items = soup.select("item")
        # for item in items[:1]:
        #     # Web에서 Image 정보 로드, 웹에서 Load한 Image를 이용하여 QPixmap에 사진데이터를 Load하고, Label을 이용하여 화면에 표시
        #     urlString = item.select_one("drawing").text
        #     imageFromWeb = urllib.request.urlopen(urlString).read()
        #     qPixmapWebVar = QPixmap()
        #     qPixmapWebVar.loadFromData(imageFromWeb)
        #     self.lb_img.setPixmap(qPixmapWebVar)
        #
        #     # 다른정보들
        #     self.lb_applicationstatus.setText(item.select_one("applicationstatus").text)
        #     self.lb_indexno.setText(item.select_one("indexno").text)
        #     self.lb_title.setText(item.select_one("title").text)
        #     self.lb_applicantName.setText(item.select_one("applicantName").text)
        #     self.lb_applicationnumber.setText(item.select_one("applicationnumber").text)
        #     self.lb_applicationDate.setText(item.select_one("applicationDate").text)
        #     self.lb_classificationCode.setText(item.select_one("classificationCode").text)

class AsignProductSearchInfo(QWindow, form_class2):
    def __init__(self, parent=None):
        super(AsignProductSearchInfo, self).__init__(parent)
        self.setupUi(self)

        self.le_asignProduct.returnPressed.connect(self.goods_search)
        self.btn_search.clicked.connect(self.goods_search)


    def goods_search(self):
        searchWord = self.le_asignProduct.text()
        query = {"searchWord": searchWord}
        api = kiprisPlus.api_trademarkAsignProductSearchInfo
        service_key = kiprisPlus.service_key
        params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding="UTF-8", errors=None)
        url = api + "?" + params + "&accessKey=" + service_key
        request = urllib.request.urlopen(url)
        xml = request.read()
        soup = BeautifulSoup(xml, 'html.parser')

        # {지정상품 : 유사군코드}_ 지정상품-유사군코드 dict으로 만들고,
        # {유사군코드 : {지정상품1, 지정상품2}}_유사군코드별-지정상품들의 dict 만들기
        good_code_dict = {}
        for k in soup.select("trademarkAsignProductSearchInfo"):
            good_code_dict[k.select_one("name").text] = k.select_one("simm").text
        code_goods_dict = {}
        for k, v in good_code_dict.items():
            code_goods_dict.setdefault(v, set()).add(k)
        # print(code_goods_dict)
        lb_simm = self.lb_simm
        tb_goods = self.tb_goods
        tb_goods.clear()
        # cb_simm = self.cb_simm


        for key in list(code_goods_dict.keys())[:1]:
            lb_simm.setText(key)
            tb_goods.append(str(code_goods_dict[key]))


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #위젯 연결
        self.btn_search.clicked.connect(self.mark_search)
        self.btn_asignProduct.clicked.connect(self.trademark_asignProduct_searchInfo)
        self.asignProduct = self.le_asignProduct.text()
        self.btn_applicationnumber.clicked.connect(self.open_applicationnumber)

    # 새로운 창으로 한개 상표 상세 보기 창 생성
    def open_applicationnumber(self):
        self.newWindow1 = OpenApplicationnumber(self)
        self.newWindow1.show()

    # 고시명칭 검색
    def trademark_asignProduct_searchInfo(self):
        self.newWindow = AsignProductSearchInfo(self)
        self.newWindow.show()

    # 상표 상세 검색
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
        # le_left_registerDate = self.le_left_registerDate.text()
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
        #     "registerDate": le_left_registerDate + "~" + le_right_registerDate,
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

        xml = xml_test.xml
        soup = BeautifulSoup(xml, 'html.parser')
        items = soup.select("item")
        for item in items[:1]:

            # Web에서 Image 정보 로드, 웹에서 Load한 Image를 이용하여 QPixmap에 사진데이터를 Load하고, Label을 이용하여 화면에 표시
            urlString = item.select_one("drawing").text
            imageFromWeb = urllib.request.urlopen(urlString).read()
            qPixmapWebVar = QPixmap()
            qPixmapWebVar.loadFromData(imageFromWeb)
            self.lb_img.setPixmap(qPixmapWebVar)

            # 다른정보들
            self.lb_applicationstatus.setText(item.select_one("applicationstatus").text)
            self.lb_indexno.setText(item.select_one("indexno").text)
            self.lb_title.setText(item.select_one("title").text)
            self.lb_applicantName.setText(item.select_one("applicantName").text)
            self.btn_applicationnumber.setText(item.select_one("applicationnumber").text)
            self.lb_applicationDate.setText(item.select_one("applicationDate").text)
            self.lb_classificationCode.setText(item.select_one("classificationCode").text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    exit(app.exec())
