from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict


class Result:
    def __init__(self, status_code: int, message: str = "", data: List[Dict] = None):
        """
        Result returned from low-level RestAdapter
        :param status_code: Standard HTTP Status code
        :param message: Human readable result
        :param data: Python List of Dicts
        """
        self.status_code = int(status_code)
        self.message = str(message)
        self.data = data if data else []


@dataclass
class Pagination:
    available_pages: int
    items_per_page: int
    page: int
    total_items: int


@dataclass
class Goals:
    steps: int
    sleep: int
    calories: int
    workout: int


class User:
    def __init__(
        self,
        id: str,
        name: str,
        email: str,
        birthday: str,
        gender: str,
        height: float,
        weight: float,
        goals: Dict,
    ):
        self.id = id
        self.name = name
        self.email = email
        self.birthday = datetime.strptime(birthday, "%Y-%m-%d").date()
        self.gender = gender
        self.height = height
        self.weight = weight
        self.goals = Goals(**goals)


class Users:
    def __init__(self, users: List[User], data_left: bool):
        self.users = users
        self.data_left = data_left

    def __iter__(self):
        for user in self.users:
            yield user