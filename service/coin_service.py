import telegram
from sqlalchemy import create_engine, orm

from core.config import Config
from model.account import Account
from util.telegram_util import telegram_send


engine = create_engine(Config.DB_FULL_URL)
session_factory = orm.scoped_session(
    orm.sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)


def init():
    with session_factory() as session:
        account = session.query(Account).filter(Account.login_id == '1').first()
        if account is None:
            return
        token = account.telegram_token
        chat_id = account.telegram_chat_id

        telegram_send(token, chat_id, 'Hello telegram world!')


if __name__ == '__main__':
    init()