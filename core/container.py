from dependency_injector import containers, providers

from api import coin, account
from core.config import Config
from core.database import Database
from repository.account_repository import AccountRepository


class Container(containers.DeclarativeContainer):
    # wiring_config = containers.WiringConfiguration(packages=['api'])

    db = providers.Singleton(
        Database,
        db_url=f'{Config.DB_FULL_URL}'
    )

    # inject
    account_repository = providers.Factory(AccountRepository, session_factory=db.provided.session)