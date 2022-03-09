from dependency_injector import containers, providers

from core.config import Config
from core.database import Database
from repository.account_repository import AccountRepository
from service.account_service import AccountService
from service.jwt_service import JwtService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=['api'])

    db = providers.Singleton(
        Database,
        db_url=f'{Config.DB_FULL_URL}'
    )

    # inject
    account_repository = providers.Factory(AccountRepository, session_factory=db.provided.session)

    jwt_service = providers.Factory(JwtService)

    account_service = providers.Factory(
        AccountService,
        account_repository=account_repository,
        jwt_service=jwt_service
    )