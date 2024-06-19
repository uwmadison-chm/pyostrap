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
class JobStatus:
    job_id: str
    job_type: str
    latest_status: str
    status_updated_at_ts: int

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

@dataclass
class DeviceInfo:
    last_data_uploaded_at_ts: int
    last_updated_at_tz_offset_mins: int
    type: str
    battery_percentage: int = 0
    last_battery_info_updated_at_ts: int = 0

@dataclass
class ActivityScore:
    avg: int
    goal: int
    processing: bool
    value: int

@dataclass
class RecoveryScore:
    avg: int
    message: str
    processing: bool
    stage: str
    value: int

@dataclass
class SleepScore:
    avg: int
    duration_secs: int
    goal: int
    processing: bool
    value: int

class Scores:
    def __init__(self, activity: Dict, recovery: Dict, sleep: Dict):
        self.activity_score = ActivityScore(**activity)
        self.recovery_score = RecoveryScore(**recovery)
        self.sleep_score = SleepScore(**sleep)
