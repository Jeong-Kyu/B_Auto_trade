import os
import sys
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
from config.errorCode import *
from config.kiwoomType import *
import logging
import time

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        self.realType = RealType()

        print('kiwoom 클래스 입니다.')
        ## 변수 ##
        self.screen_start_stop_real = '1000'
        self.screen_my_info = '2000'
        self.screen_price_info = '3000'
        self.screen_pivot_info = '5000'
        self.account_select = 1
        self.use_money_percent = 0.1

        self.dict=[]
        self.line_dict = {}
        self.not_account_stock_dict={}
        self.jango_dict = {}

        ##시작##
        self.get_ocx_instance()
        self.event_slots()
        self.real_event_slots()

        self.signal_login_commConnect()
        self.get_account_info()

        self.detail_account_info()
        self.having_check_info()

        self.dynamicCall('SetRealReg(QString, QString, QString, QString)', self.screen_start_stop_real, '', self.realType.REALTYPE['장시작시간']['장운영구분'], '0')

        for code in self.dict:
            # self.having_pivot_info(code=code)
            # self.line_dict[code].update({"1차저항":self.sub[0],"2차저항":self.sub[1],"1차지지":self.sub[2],"2차지지":self.sub[3]})
            self.line_dict[code].update({"1차":0,"2차":0,"3차":0,"4차":0})
            # print(self.line_dict)
            screen_num = 4000
            fids = self.realType.REALTYPE['주식호가잔량']['호가시간']
            self.dynamicCall('SetRealReg(QString, QString, QString, QString)', screen_num, code, fids, '1')
            print('실시간 등록 코드: %s, 스크린번호: %s, fid번호: %s' % (code,screen_num,20))
    
    def get_ocx_instance(self):
        self.setControl('KHOPENAPI.KHOpenAPICtrl.1') 

    def event_slots(self):
        self.OnEventConnect.connect(self.login_slot)
        self.OnReceiveTrData.connect(self.trdata_slot)
        self.OnReceiveMsg.connect(self.msg_slot)

    def real_event_slots(self):
        self.OnReceiveRealData.connect(self.realdata_slot)
        self.OnReceiveChejanData.connect(self.chejan_slot)

    def signal_login_commConnect(self):
        self.dynamicCall("CommConnect()")
        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()

    def msg_slot(self, sScrNo, sRQName, sTrCode, sMsg):
        print(sScrNo, sRQName, sTrCode, sMsg)
    def login_slot(self, errCode):
        print(errors(errCode))
        self.login_event_loop.exit()

    def trdata_slot(self, sScrNo, sRQName, sTrCode, sRecordName, sPrevNext):
                         # 스크린번호, 설정이름, 요청id, 사용안함, 다음페이지
        if sRQName == '예수금상세현황요청':
            deposit = self.dynamicCall('GetCommData(String, String, int, String)', sTrCode, sRQName, 0, '주문가능금액')
            print('예수금 : %s' % int(deposit))
            self.use_money = int(deposit) * self.use_money_percent
            # self.use_money = self.use_money / 4
            ok_deposit = self.dynamicCall('GetCommData(String, String, int, String)', sTrCode, sRQName, 0, '출금가능금액')
            print('출금가능금액 : %s' % int(ok_deposit))

            self.detail_account_info_event_loop.exit()

        if sRQName == '계좌평가현황요청':
            h = self.dynamicCall('GetCommData(String, String, int, String)', sTrCode, sRQName, 0, '출력건수')
            for i in range(int(h)):
                h_code = self.dynamicCall('GetCommData(String, String, int, String)', sTrCode, sRQName, i, '종목코드')
                h_name = self.dynamicCall('GetCommData(String, String, int, String)', sTrCode, sRQName, i, '종목명')
                h_count = self.dynamicCall('GetCommData(String, String, int, String)', sTrCode, sRQName, i, '보유수량')
                self.dict.append(h_code.strip()[1:])
                self.line_dict.update({h_code.strip()[1:]:{}})
            print(self.dict)
            self.real_price_check_event_loop.exit()

        if sRQName == '주식일주월시분요청':
            self.sub = []
            h_price = int(self.dynamicCall('GetCommData(String, String, int, String)', sTrCode, sRQName, 1, '고가'))
            l_price = int(self.dynamicCall('GetCommData(String, String, int, String)', sTrCode, sRQName, 1, '저가'))
            e_price = int(self.dynamicCall('GetCommData(String, String, int, String)', sTrCode, sRQName, 1, '종가'))
            # pivot = (h_price+l_price+e_price)/3
            # one_d = (pivot*2)-l_price
            # two_d = pivot-l_price
            # one_a = (pivot*2)-h_price
            # two_a = pivot-h_price+l_price
            # self.sub.append(one_d)
            # self.sub.append(two_d)
            # self.sub.append(one_a)
            # self.sub.append(two_a)
            self.sub = [h_price,l_price,e_price]
            self.Pivot_event_loop.exit()

    def get_account_info(self):
        account_list = self.dynamicCall('GetLogininfo(String)','ACCNO')
        self.account_num = account_list.split(';')[self.account_select]
        print('전체 계좌번호 %s' %account_list)
        print('나의 보유 계좌번호 %s' %self.account_num)

    def detail_account_info(self):
        print('예수금 요청')
        self.dynamicCall('SetInputValue(String, String)','계좌번호', self.account_num)
        self.dynamicCall('SetInputValue(String, String)','비밀번호', '0000')
        self.dynamicCall('SetInputValue(String, String)','비밀번호입력매체구분', '00')
        # self.dynamicCall('SetInputValue(String, String)','조회구분', '2')    
        self.dynamicCall('CommRqData(String, String, int, String)', '예수금상세현황요청', 'opw00001', '0', self.screen_my_info)
        self.detail_account_info_event_loop = QEventLoop()
        self.detail_account_info_event_loop.exec_()

    def having_check_info(self):
        print('보유종목')
        self.dynamicCall('SetInputValue(String, String)','계좌번호', self.account_num)
        self.dynamicCall('SetInputValue(String, String)','비밀번호', '0000')
        self.dynamicCall('SetInputValue(String, String)','상장폐지조회구분', '0')
        self.dynamicCall('SetInputValue(String, String)','비밀번호입력매체구분', '00')
        self.dynamicCall('CommRqData(String, String, int, String)','계좌평가현황요청',"opw00004","0",self.screen_price_info)
        self.real_price_check_event_loop = QEventLoop()
        self.real_price_check_event_loop.exec_()

    def having_pivot_info(self, code):
        print('Pivot작업')
        self.dynamicCall('SetInputValue(String, String)','종목코드', code)
        self.dynamicCall('CommRqData(String, String, int, String)','주식일주월시분요청',"opt10005","0",self.screen_pivot_info)
        self.Pivot_event_loop = QEventLoop()
        self.Pivot_event_loop.exec_()

    def realdata_slot(self, sCode, sRealType, sRealData):
        
        if sRealType == '장시작시간':
            fid = self.realType.REALTYPE[sRealType]['장운영구분']
            value = self.dynamicCall('GetCommRealData(QString, int)', sCode, fid)

            if value == '0':
                print('장 시작 전')
            elif value == '3':
                print('장 시작')
            elif value == '2':
                print('장 종료, 동시호가로 넘어감')
                for sCode in self.jango_dict.keys():
                    bs = self.jango_dict[sCode]['주문가능수량']
                    gr = self.dynamicCall('SendOrderFO(QString, QString, QString, QString, int, int, QString, int, int, QString)',['당일종료매도', '0101', self.account_num, sCode, 1, 1, '3', bs, 0, ""])
                    print('당일종료매도',self.portfolio_stock_dict)     
                    self.jango_dict[sCode]['주문가능수량'] = 0

            elif value == '4':
                print('3시30분 장 종료')

        elif sRealType == '주식체결':
            self.now_price = float(self.dynamicCall("GetCommRealData(QString, int)", sCode, self.realType.REALTYPE[sRealType]['현재가']))
            self.low_price = float(self.dynamicCall("GetCommRealData(QString, int)", sCode, self.realType.REALTYPE[sRealType]['현재가']))

            print(self.now_price)
            # d1 = self.line_dict[sCode]['1차저항']
            # d2 = self.line_dict[sCode]['2차저항']
            # a1 = self.line_dict[sCode]['1차지지']
            # a2 = self.line_dict[sCode]['2차지지']
            # if self.now_price > d1:
            #     print('1차저항 위',self.now_price,d1)
            # elif d1 > self.now_price > a1:
            #     print('1차저항 1차지지 사이',d1,self.now_price,a1)
            # elif a1 > self.now_price > a2:
            #     print('1차지지 2차지지 사이',a1,self.now_price,a2)
            # elif a2 > self.now_price > d2:
            #     print('1차지지 2차저항 사이',a2,self.now_price,d2)
            # elif d2 > self.now_price:
            #     print('2차저항 아래',d2,self.now_price)

    def chejan_slot(self,sGubun,nItemCnt,sFIdList):
        if int(sGubun) == 0:
            sCode = self.dynamicCall('GetChejanData(int)', self.realType.REALTYPE['주문체결']['종목코드'])[1:]
            order_number = self.dynamicCall('GetChejanData(int)', self.realType.REALTYPE['주문체결']['주문번호'])
            order_status = self.dynamicCall('GetChejanData(int)', self.realType.REALTYPE['주문체결']['주문상태'])
            order_quan = self.dynamicCall('GetChejanData(int)', self.realType.REALTYPE['주문체결']['주문수량'])
            order_quan = int(order_quan)
            not_chegual_quan = self.dynamicCall('GetChejanData(int)', self.realType.REALTYPE['주문체결']['미체결수량'])
            not_chegual_quan = int(not_chegual_quan)
            chegual_quantity = self.dynamicCall('GetChejanData(int)', self.realType.REALTYPE['주문체결']['체결량'])
            if chegual_quantity == '':
                chegual_quantity = 0
            else:
                chegual_quantity = int(chegual_quantity)

            if sCode not in self.not_account_stock_dict.keys():
                self.not_account_stock_dict.update({sCode:{}})
            self.not_account_stock_dict[sCode].update({'주문번호':order_number})
            self.not_account_stock_dict[sCode].update({'주문상태':order_status})
            self.not_account_stock_dict[sCode].update({'주문수량':order_quan})
            self.not_account_stock_dict[sCode].update({'미체결수량':not_chegual_quan})
            if order_quan == chegual_quantity:
                del self.not_account_stock_dict[sCode]

        elif int(sGubun) == 1:
            account_num = self.dynamicCall('GetChejanData(int)', self.realType.REALTYPE['잔고']['계좌번호'])
            sCode = self.dynamicCall('GetChejanData(int)', self.realType.REALTYPE['잔고']['종목코드'])[1:]
            stock_name = self.dynamicCall('GetChejanData(int)', self.realType.REALTYPE['잔고']['종목명'])
            stock_name = stock_name.strip()
            current_price = self.dynamicCall('GetChejanData(int)', self.realType.REALTYPE['잔고']['현재가'])
            current_price = float(current_price)
            stock_quan = self.dynamicCall('GetChejanData(int)', self.realType.REALTYPE['잔고']['보유수량'])
            stock_quan = int(stock_quan)
            like_quan = self.dynamicCall('GetChejanData(int)', self.realType.REALTYPE['잔고']['주문가능수량'])
            like_quan = int(like_quan)
            buy_price = self.dynamicCall('GetChejanData(int)', self.realType.REALTYPE['잔고']['손익율'])
            buy_price = float(buy_price)
            total_buy_price = self.dynamicCall('GetChejanData(int)', self.realType.REALTYPE['잔고']['총매입가'])
            total_buy_price = float(total_buy_price)
            buy_p_price = self.dynamicCall('GetChejanData(int)', self.realType.REALTYPE['잔고']['매입단가'])
            buy_p_price = float(buy_p_price)

            if sCode not in self.jango_dict.keys():
                self.jango_dict.update({sCode:{}})
            self.jango_dict[sCode].update({'현재가':current_price})
            self.jango_dict[sCode].update({'종목코드':sCode})
            self.jango_dict[sCode].update({'종목명':stock_name})
            self.jango_dict[sCode].update({'보유수량':stock_quan})
            self.jango_dict[sCode].update({'주문가능수량':like_quan})
            self.jango_dict[sCode].update({'손익율':buy_price})
            self.jango_dict[sCode].update({'총매입가':total_buy_price})
            self.jango_dict[sCode].update({'매입단가':buy_p_price})
            print(self.not_account_stock_dict)
            print(self.jango_dict)

            if sCode not in self.dict:
                self.dict.append(sCode)
                self.line_dict.update({sCode:{}})            
                self.line_dict[sCode].update({"1차저항":self.sub[0],"2차저항":self.sub[1],"1차지지":self.sub[2],"2차지지":self.sub[3]})
                screen_num = 4000
                fids = self.realType.REALTYPE['옵션호가잔량']['호가시간']
                self.dynamicCall('SetRealReg(QString, QString, QString, QString)', screen_num, sCode, fids, '1')
                print('실시간 등록 코드: %s, 스크린번호: %s, fid번호: %s' % (sCode,screen_num,20))
            if like_quan == 0:
                del self.jango_dict[sCode]
                del self.line_dict[sCode]
                del self.dict[sCode]

