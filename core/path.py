class ContextPath:
    CONTEXT_PATH = '/finance'


class UpbitPath:
    BASE_URL = 'https://api.upbit.com'

    # 자산
    # 1. 전체 계좌 조회 (GET)
    ACCOUNT_INQUIRY = '/v1/accounts'

    # 주문
    # 1. 주문 가능 정보 (GET)
    ORDERS_AVAILABLE = '/v1/orders/chance'
    # 2. 개별 주문 조회 (GET)
    ORDER = '/v1/order'
    # 3. 주문 리스트 조회 (GET)
    ORDERS = '/v1/orders'
    # 4. 주문 취소 접수 (DELETE)
    ORDER_DELETE = '/v1/order'
    # 5. 주문하기 (POST)
    ORDERS_REQUEST = '/v1/orders'


