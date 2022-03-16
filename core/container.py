from dependency_injector import containers, providers

import core
from core.database import Database
from repository.account_repository import AccountRepository
from service.account_service import AccountService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=['api'])

    db = providers.Singleton(
        Database,
        db_url=f'{core.Config.DB_FULL_URL}'
    )

    # inject
    account_repository = providers.Factory(AccountRepository, session_factory=db.provided.session)

    account_service = providers.Factory(AccountService, account_repository=account_repository)