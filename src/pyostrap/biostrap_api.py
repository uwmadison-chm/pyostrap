import logging

from models import Pagination, User, Users
from rest_adapter import RestAdapter


class BiostrapApi:
    def __init__(
        self,
        api_key: str,
        hostname: str = "api-beta.biostrap.com",
        ver: str = "v1",
        ssl_verify: bool = True,
        logger: logging.Logger = None,
    ):
        self._rest_adapter = RestAdapter(api_key, hostname, ver, ssl_verify, logger)

    def get_users(self, page: int, items_per_page: int) -> Users:
        ep_params = {"page": page, "items_per_page": items_per_page}
        result = self._rest_adapter.get(
            endpoint="organizations/users", ep_params=ep_params
        )
        pagination = Pagination(**result.data["pagination"])
        user_list = [User(**raw_user) for raw_user in result.data["users"]]
        return Users(user_list, pagination.page < pagination.available_pages)
