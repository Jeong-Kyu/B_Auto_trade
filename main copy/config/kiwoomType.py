class RealType(object):
    SENDTYPE={
        '거래구분':{
            '지정가':'00',
            '시장가':'03',
            '조건부지정가':'05',
            '최유리지정가':'06',
            '최우선지정가':'07',
            '지정가IOC':'10',
            '시장가IOC':'13',
            '최유리IOC':'16',
            '지정가FOK':'20',
            '시장가FOK':'23',
            '최유리FOK':'26',
            '장전시간외종가':'61',
            '시간외단일가매매':'62',
            '장후시간외종가':'81'
        }
    }

    REALTYPE={
        '주식호가잔량':{
            '호가시간':21
        },
        '주식체결':{
            '체결시간':20,
            '현재가':10,
            '전일대비':11,
            '등락율':12,
            '(최우선)매도호가':27,
            '(최우선)매수호가':28,
            '거래량':15,
            '누적거래량':13,
            '누적거래대금':14,
            '시가':16,
            '고가':17,
            '저가':18,
            '전일대비기호':25,
            '전일거래량대비':26,
            '거래대금증감':29,
            '전일거래량대비':30,
            '거래회전율':31,
            '거래비용':32,
            '체결강도':228,
            '시가총액(억)':311,
            '장구분':290,
            'KO접근도':691,
            '상한가발생시간':567,
            '하한가발생시간':568
        },

        '장시작시간':{
            '장운영구분':215,
            '시간':20,
            '장시작예상잔여시간':214
        },

        '주문체결':{
            '계좌번호':9201,
            '주문번호':9203,
            '관리자사번':9205,
            '종목코드':9001,
            '주문업무분류':912,
            '주문상태':913,
            '종목명':302,
            '주문수량':900,
            '주문가격':901,
            '미체결수량':902,
            '체결누계금액':903,
            '원주문번호':904,
            '주문구분':905,
            '매매구분':906,
            '매도수구분':907,
            '주문/체결시간':908,
            '체결번호':909,
            '체결가':910,
            '체결량':911,
            '현재가':10,
            '(최우선)매도호가':27,
            '(최우선)매수호가':28,
            '단위체결가':914,
            '단위체결량':915,
            '당일매매수수료':938,
            '당일매매세금':939,
            '거부사유':919,
            '화면번호':920,
            '터미널번호':921,
            '신용구분(실시간 체결용)':922,
            '대출일(실시간 체결용':923
        },

        '매도수구분':{
            '1':'매도',
            '2':'매수'
        },

        '잔고':{
            '계좌번호':9201,
            '종목코드':9001,
            '종목명':302,
            '현재가':10,
            '보유수량':930,
            '매입단가':931,
            '총매입가':932,
            '주문가능수량':933,
            '당일순매수량':945,
            '매도매수구분':946,
            '당일총매도손익':950,
            '예수금':951,
            '(최우선)매도호가':27,
            '(최우선)매수호가':28,
            '기준가':307,
            '손익율':8019
        },
        '선물시세':{
            '체결시간':20,
            '현재가':10,
            '전일대비':11,
            '등락율':12,
            '(최우선)매도호가':27,
            '(최우선)매수호가':28,
            '거래량':15,
            '누적거래량':13,
            '누적거래대금':14,
            '시가':16,
            '고가':17,
            '저가':18,
            '미결제약정':195,
            '이론가':182,
            '이론베이시스':184,
            '시장베이시스':183,
            '괴리율':186,
            '미결제약정전일대비':181,
            '괴리도':185,
            '전일대비기호':25,
            'KOSPI200':197,
            '전일거래량대비(계약,주)':26,
            '시초미결제약정수량':246,
            '최고미결제약정수량':247,
            '최저미결제약정수량':248,
            '전일거래량대비(비율)':30,
            '미결제증감':196,
            '실시간상한가':1365,
            '실시간하한가':1366,
            '협의대량누적체결수량':1367,
            '상한가':305,
            '하한가':306
        },
        '주식시세':{
            '현재가':10,
            '전일대비':11,
            '등락율':12,
            '(최우선)매도호가':27,
            '(최우선)매수호가':28,
            '누적거래량':13,
            '누적거래대금':14,
            '시가':16,
            '고가':17,
            '저가':18,
            '전일거래량대비(계약,주)':26,
            '거래대금증감':29,
            '전일거래량대비(비율)':30,
            '거래회전율':31,
            '거래비용':32,
            '시가총액(억)':311,
            '상한가발생시간':567,
            '하한가발생시간':568
        },
        
        '업종지수':{
            '체결시간':20,
            '현재가':10,
            '전일대비':11,
            '등락율':12,
            '거래량(+는 매수체결, -는 매도체결)':15,
            '누적거래량':13,
            '누적거래대금':14,
            '시가':16,
            '고가':17,
            '저가':18,
            '전일대비기호':25,
            '전일거래량대비(계약,주)':26
        },
        '옵션시세':{
            '체결시간':20,
            '현재가':10,
            '전일대비':11,
            '등락율':12,
            '(최우선)매도호가':27,
            '(최우선)매수호가':28,
            '거래량':15,
            '누적거래량':13,
            '누적거래대금':14,
            '시가':16,
            '고가':17,
            '저가':18,
            '미결제약정':195,
            '이론가':182,
            '괴리율':186,
            '델타':190,
            '감마':191,
            '세타':193,
            '베가':192,
            '로':194,
            '미결제약정전일대비':181,
            '전일대비기호':25,
            '전일거래량대비(계약,주)':26,
            '호가순잔량':137,
            '내재가치':187,
            'KOSPI200':197,
            '시초미결제약정수량':246,
            '최고미결제약정수량':247,
            '최저미결제약정수량':248,
            '선물최근월물지수':219,
            '미결제증감':196,
            '시간가치':188,
            '내재변동성(I.V.)':189,
            '전일거래량대비(비율)':30,
            '기준가대비시가등락율':391,
	        '기준가대비고가등락율':392,
	        '기준가대비저가등락율':393,
            '실시간상한가':1365,
            '실시간하한가':1366,
            '협의대량누적체결수량':1367,
            '상한가':305,
            '하한가':306
        },

        '옵션호가잔량':{
            '호가시간':21,
            '(최우선)매도호가':27,
            '(최우선)매수호가':28,
            '매도호가1':41,
            '매도호가수량1':61,
            '매도호가직전대비1':81,
            '매도호가건수1':101,
            '매수호가1':51,
            '매수호가수량1':71,
            '매수호가직전대비1':91,
            '매수호가건수1':111,
            '매도호가2':42,
            '매도호가수량2':62,
            '매도호가직전대비2':82,
            '매도호가건수2':102,
            '매수호가2':52,
            '매수호가수량2':72,
            '매수호가직전대비2':92,
            '매수호가건수2':112,
            '매도호가3':43,
            '매도호가수량3':63,
            '매도호가직전대비3':83,
            '매도호가건수3':103,
            '매수호가3':53,
            '매수호가수량3':73,
            '매수호가직전대비3':93,
            '매수호가건수3':113,
            '매도호가4':44,
            '매도호가수량4':64,
            '매도호가직전대비4':84,
            '매도호가건수4':104,
            '매수호가4':54,
            '매수호가수량4':74,
            '매수호가직전대비4':94,
            '매수호가건수4':114,
            '매도호가5':45,
            '매도호가수량5':65,
            '매도호가직전대비5':85,
            '매도호가건수5':105,
            '매수호가5':55,
            '매수호가수량5':75,
            '매수호가직전대비5':95,
            '매수호가건수5':115,
            '매도호가총잔량':121,
            '매도호가총잔량직전대비':122,
            '매도호가총건수':123,
            '매수호가총잔량':125,
            '매수호가총잔량직전대비':126,
            '매수호가총건수':127,
            '호가순잔량':137,
            '순매수잔량':128,
            '누적거래량':13,
            '예상체결가':23,
            '예상체결가전일종가대비기호':238,
            '예상체결가전일종가대비':200,
            '예상체결가전일종가대비등락율':201,
            '예상체결가(예상체결 시간동안에만 유효한 값)':291,
            '예상체결가전일대비기호':293,
            '예상체결가전일대비':294,
            '예상체결가전일대비등락율':295
        }
    }