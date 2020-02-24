import sys
from PyQt5.QtWidgets import *
import getInfoFromApi
from PyQt5 import uic
form_class1 = uic.loadUiType("gui_ui_getAdvancedSearch.ui")[0]
form_class2 = uic.loadUiType("gui_getGoodsList.ui")[0]


class NewMyApp(QMainWindow, form_class2):
    def __init__(self, parent=None):
        super(NewMyApp, self).__init__(parent)
        self.setupUi(self)

        #위젯 연결
        self.le_asignProduct.returnPressed.connect(self.get_goods_list)
        self.btn_search.clicked.connect(self.get_goods_list)

    #위젯에 연결된 함수
    def get_goods_list(self):
        le_asignProduct = self.le_asignProduct.text()

        self.tb_code_goods.clear()

        # {지정상품 : 유사군코드}_ 지정상품-유사군코드 dict 만들기
        def goods_code_dict(soup):
            list = soup.select("trademarkdesignationgoodstinfo")
            good_code_dict = {}
            for k in list:
                good_code_dict[k.select_one("designationgoodshangeulname").text] = k.select_one("similargroupcode").text
            return good_code_dict
        # {유사군코드 : {지정상품1, 지정상품2}}_유사군코드별-지정상품들의 dict 만들기
        def code_goods_dict(dict):
            code_goods_dict = {}
            for k, v in dict.items():
                code_goods_dict.setdefault(v, set()).add(k)
            return code_goods_dict
        # 출원번호의 리스트를 뽑아서 리턴
        def get_appNum(soup):
            return soup.select("applicationnumber")

        # 상품명에 대한 쿼리 및 api를 통해서 정로를 받음
        query = {
            "asignProduct": le_asignProduct,
            "applicationDate": "20191201~20200223",
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

        # 출원번호를 모아서, 지정상품 정보를 api를 통해서 받고, 지정상품:유사군코드 딕셔너리 생성
        appNums = get_appNum(soup)
        code_Goods_Dict = {}
        code_goods_output = {}
        for appNum in appNums:
            # 출원번호의 지정상품 정보
            soup = getInfoFromApi.trademarkDesignationGoodstInfo({"applicationNumber": appNum.text})
            goods_code_for_one_appNum = goods_code_dict(soup)
            code_goods_output.update(goods_code_for_one_appNum)

        # 유사군코드별 상품들로 바꿔줌
        code_Goods_Dict = code_goods_dict(code_goods_output)
        for k in code_Goods_Dict:
            self.tb_code_goods.append(str(k))
            self.tb_code_goods.append(str(code_Goods_Dict[k]))



class MyApp(QMainWindow, form_class1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #위젯 연결
        self.btn_search.clicked.connect(self.mark_search)
        self.but_seachr_goods.clicked.connect(self.button_clicked)

    # 버튼이 클릭될 때 새로운 창 생성
    def button_clicked(self):
        self.newMyApp = NewMyApp(self)
        self.newMyApp.show()

    #위젯에 연결된 함수
    def mark_search(self):
        le_trademarkName = self.le_trademarkName.text()
        # applicationDate_le = self.applicationDate_le.text()
        le_similarityCode = self.le_similarityCode.text()

        self.lbl_text.setText('Search Results for "' + le_trademarkName + '"')
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

app = QApplication(sys.argv)
ex = MyApp()
ex.show()
app.exec_()


