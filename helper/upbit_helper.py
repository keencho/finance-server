import uuid

import jwt
import requests

from core.config import Config
from core.path import UpbitPath
from exception.exception import FinanceCommonException

BASE_URL = UpbitPath.BASE_URL


def upbit_request(path: str):
    res = requests.get(BASE_URL + path, headers=_get_headers())

    if res.status_code != 200:
        raise FinanceCommonException('upbit 요청 실패 - ' + path)

    return res.json()


def _get_headers():
    payload = {
            'access_key': Config.UPBIT_ACCESS_KEY,
            'nonce': str(uuid.uuid4())
    }

    jwt_token = jwt.encode(payload, Config.UPBIT_SECRET_KEY)
    authorize_token = 'Bearer {}'.format(jwt_token)

    return {"Authorization": authorize_token}

################################################################


def get_market_code():
    """
    market          업비트에서 제공중인 시장 정보
    korean_name     거래 대상 암호화폐 한글명
    english_name    거래 대상 암호화폐 영문명
    """
    return upbit_request(UpbitPath.QUOTATION_MARKET_CODE)


def get_ticker(markets: list):
    """
    market	                종목 구분 코드	            String
    trade_date	            최근 거래 일자(UTC)           String
    trade_time	            최근 거래 시각(UTC)           String
    trade_date_kst	        최근 거래 일자(KST)           String
    trade_time_kst	        최근 거래 시각(KST)           String
    opening_price	        시가	                        Double
    high_price	            고가	                        Double
    low_price	            저가	                        Double
    trade_price	            종가	                        Double
    prev_closing_price	    전일 종가	                Double
    change	                EVEN : 보합
                            RISE : 상승
                            FALL : 하락	                String
    change_price	        변화액의 절대값	            Double
    change_rate	            변화율의 절대값	            Double
    signed_change_price	    부호가 있는 변화액	            Double
    signed_change_rate	    부호가 있는 변화율	            Double
    trade_volume	        가장 최근 거래량	            Double
    acc_trade_price	        누적 거래대금(UTC 0시 기준)	Double
    acc_trade_price_24h	    24시간 누적 거래대금	        Double
    acc_trade_volume	    누적 거래량(UTC 0시 기준)	    Double
    acc_trade_volume_24h	24시간 누적 거래량	        Double
    highest_52_week_price	52주 신고가	                Double
    highest_52_week_date	52주 신고가 달성일	        String
    lowest_52_week_price	52주 신저가	                Double
    lowest_52_week_date	    52주 신저가 달성일	        String
    timestamp	            타임스탬프	                Long
    """
    return upbit_request(UpbitPath.QUOTATION_TICKER + '?markets=' + ",".join(markets))


def get_orderbook(markets: list):
    """
    market	            마켓 코드	        String
    timestamp	        호가 생성 시각	    Long
    total_ask_size	    호가 매도 총 잔량	    Double
    total_bid_size	    호가 매수 총 잔량	    Double
    orderbook_units	    호가	                List of Objects
    ask_price	        매도호가	            Double
    bid_price	        매수호가	            Double
    ask_size	        매도 잔량	        Double
    bid_size	        매수 잔량	        Double
    """
    return upbit_request(UpbitPath.QUOTATION_ORDERBOOK + '?markets=' + ",".join(markets))