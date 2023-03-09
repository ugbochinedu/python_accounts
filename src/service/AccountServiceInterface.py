from abc import ABC, abstractmethod

from data.dto.request.AccountRequest import AccountRequest
from data.dto.response.AccountResponse import AccountResponse
from data.model.Account import Account


class AccountServiceInterface(ABC):
    @abstractmethod
    def create_new_account(self, account_request: AccountRequest) -> AccountResponse:
        pass

    @abstractmethod
    def find_account_by_account_id(self, name: str) -> Account:
        pass

    @abstractmethod
    def delete_account_by_account_id(self, id: int) -> str:
        pass

    @abstractmethod
    def find_account_by_account_name(self, name: str) -> str:
        pass

    @abstractmethod
    def delete_account_by_account_name(self, name: str) -> str:
        pass

    @abstractmethod
    def edit_account_by_account_id(self, id: int) -> str:
        pass

    @abstractmethod
    def edit_account_by_account_name(self, name: str) -> str:
        pass
