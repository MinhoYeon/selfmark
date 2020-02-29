import sys
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import *
from PyQt5 import uic
import kiprisPlus as kp
from PyQt5.QtGui import *
import xml_advancedSerach, xml_appNum, xml_goods

form_class3 = uic.loadUiType("one_mark.ui")[0]
form_class2 = uic.loadUiType("asignproductsearchinfo.ui")[0]
form_class = uic.loadUiType("getAdvancedSearch_v4.ui")[0]

class ApplicationNumberSearchInfo(QMainWindow, QDialog, form_class3):
    def __init__(self, parent=None):
        super(ApplicationNumberSearchInfo, self).__init__(parent)
        self.setupUi(self)

        print(advSearchWin.appNum)

        # query = {"applicationNumber" : advSearchWin.appNum}
        # self.soup = kp.search_accessKey(query, kp.api_applicationNumberSearchInfo)

        self.soup = BeautifulSoup(xml_appNum.xml, 'html.parser')

        # 상표작은이미지
        self.urlString = self.soup.select_one("thumbnailpath").text
        self.imageFromWeb = urllib.request.urlopen(self.urlString).read()
        self.qPixmapWebVar = QPixmap()
        self.qPixmapWebVar.loadFromData(self.imageFromWeb)
        self.lb_img.setPixmap(self.qPixmapWebVar)
        # 상태, 인덱스, 상표명, 출원인, 출원번호, 출원일, 분류
        self.lb_applicationstatus.setText(self.soup.select_one("applicationstatus").text)
        self.lb_title.setText(self.soup.select_one("title").text)
        self.lb_applicantName.setText(self.soup.select_one("applicantname").text)
        self.lb_applicationnumber.setText(self.soup.select_one("applicationnumber").text)
        self.lb_applicationDate.setText(self.soup.select_one("applicationdate").text)
        self.lb_classificationCode.setText(self.soup.select_one("GoodClassificationCode").text)
        # 공고번호, 공고일, 등록번호, 등록일
        self.lb_PublicNumber.setText(self.soup.select_one("publicnumber").text)
        self.lb_PublicDate.setText(self.soup.select_one("publicdate").text)
        self.lb_RegistrationNumber.setText(self.soup.select_one("registrationnumber").text)
        self.lb_RegistrationDate.setText(self.soup.select_one("registrationdate").text)
        # 상품분류, 비엔나코드
        self.lb_GoodClassificationCode.setText(self.soup.select_one("goodclassificationcode").text)
        self.lb_ViennaCode.setText(self.soup.select_one("viennacode").text)


        # 지정상품
        # query = {"applicationNumber" : ""}
        # self.soup = kp.search_accessKey(query, kp.api_trademarkDesignationGoodstInfo)
        self.soup = BeautifulSoup(xml_goods.xml, 'html.parser')
        self.goods = self.soup.select("trademarkDesignationGoodstInfo")
        for self.good in self.goods[:1]:
            self.lb_DesignationGoodsSerialNumber.setText(self.good.select_one("DesignationGoodsSerialNumber").text)
            self.lb_DesignationGoodsClassificationInformationCode.setText(self.good.select_one("DesignationGoodsClassificationInformationCode").text.split("(")[0])
            self.lb_SimilargroupCode.setText(self.good.select_one("SimilargroupCode").text)
            self.lb_DesignationGoodsHangeulName.setText(self.good.select_one("DesignationGoodsHangeulName").text)


class AsignProductSearchInfo(QMainWindow, QDialog, form_class2):
    def __init__(self, parent=None):
        super(AsignProductSearchInfo, self).__init__(parent)
        self.setupUi(self)

        self.le_asignProduct.setText(advSearchWin.asignProduct)

    def trademark_asignProduct_searchInfo(self):
        self.searchWord = self.le_asignProduct.text()
        query = {"searchWord": self.searchWord}
        self.soup = kp.search_accessKey(query, kp.api_trademarkAsignProductSearchInfo)
        # {지정상품 : 유사군코드}만들고, {유사군코드 : {지정상품1, 지정상품2}}만듬.
        good_code_dict = {}
        for k in self.soup.select("trademarkAsignProductSearchInfo"):
            good_code_dict[k.select_one("name").text] = k.select_one("simm").text
        code_goods_dict = {}
        for k, v in good_code_dict.items():
            code_goods_dict.setdefault(v, set()).add(k)
        lb_simm = self.lb_simm
        tb_goods = self.tb_goods
        tb_goods.clear()
        # cb_simm = self.cb_simm #체크박스 선택하고 저장하면 반영하는 코드 구현
        for key in list(code_goods_dict.keys())[:1]:
            lb_simm.setText(key)
            tb_goods.append(str(code_goods_dict[key]))

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.asignProduct = None
        self.appNum = None
    # 새로운 창으로 한개 상표 상세 보기 창 생성
    def applicationnumber_search_info(self):
        self.appNumWin = ApplicationNumberSearchInfo(self)
        self.appNumWin.show()
    # 고시명칭 검색
    def trademark_asignProduct_searchInfo(self):
        self.asignProductWin = AsignProductSearchInfo(self)
        self.asignProduct = self.btn_applicationnumber.text()
        self.asignProductWin.show()
    # 상표 상세 검색
    def advanced_search(self):
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
        # soup = kp.search_serviceKey(query, kp.api_getAdvancedSearch)
        self.soup = BeautifulSoup(xml_advancedSerach.xml, 'html.parser')
        self.items = self.soup.select("item")
        for self.item in self.items[:1]:
            # Web에서 Image 정보 로드, 웹에서 Load한 Image를 이용하여 QPixmap에 사진데이터를 Load하고, Label을 이용하여 화면에 표시
            self.urlString = self.item.select_one("drawing").text
            self.imageFromWeb = urllib.request.urlopen(self.urlString).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(self.imageFromWeb)
            self.lb_img.setPixmap(self.qPixmapWebVar)
            # 다른정보들
            self.lb_applicationstatus.setText(self.item.select_one("applicationstatus").text)
            self.lb_indexno.setText(self.item.select_one("indexno").text)
            self.lb_title.setText(self.item.select_one("title").text)
            self.lb_applicantName.setText(self.item.select_one("applicantName").text)
            self.btn_applicationnumber.setText(self.item.select_one("applicationnumber").text)
            self.lb_applicationDate.setText(self.item.select_one("applicationDate").text)
            self.lb_classificationCode.setText(self.item.select_one("classificationCode").text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    advSearchWin = MyWindow()
    advSearchWin.show()
    app.exec()
