from data.dto.request.AccountRequest import AccountRequest
from data.dto.response.AccountResponse import AccountResponse
from data.model.Account import Account
from data.repository.AccountRepositoryInterface import AccountRepositoryInterface
from service.AccountServiceInterface import AccountServiceInterface


class AccountServiceInterfaceImpl(AccountServiceInterface):
    account_repo = AccountRepositoryInterface()

    def create_new_account(self, account_request: AccountRequest) -> AccountResponse:
        pass

    def find_account_by_account_id(self, id: int) -> Account:

        id_response = self.account_repo.find_account_by_id(id)
        if not id_response:
            raise ValueError("Invalid Id")
        else:
            return id_response

    def delete_account_by_account_id(self, id: int) -> str:
        pass

    def find_account_by_account_name(self, name: str) -> str:
        pass

    def delete_account_by_account_name(self, name: str) -> str:
        pass

    def edit_account_by_account_id(self, id: int) -> str:
        pass

    def edit_account_by_account_name(self, name: str) -> str:
        pass
