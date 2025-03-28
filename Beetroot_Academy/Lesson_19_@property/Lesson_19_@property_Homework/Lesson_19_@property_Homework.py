print(
    '''
Task 1
    '''
)

import re


class EmailValidator:
    def __init__(self, email: str):
        self.email = email
        self.validate(email)  # Передаем email явно

    @classmethod
    def validate(cls, email: str):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise ValueError(f"Invalid email address: {email}")


try:
    valid_email = EmailValidator("example@example.com")
    print("Email is valid!")
except ValueError as e:
    print(e)

try:
    invalid_email = EmailValidator("invalid-email")
except ValueError as e:
    print(e)

print(
    '''
Task 2
    '''
)


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    def add_worker(self, worker):
        if not isinstance(worker, Worker):
            raise TypeError("Only Worker instances can be added.")
        if worker not in self._workers:
            self._workers.append(worker)
            worker._boss = self

    @property
    def workers(self):
        return self._workers


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if not isinstance(new_boss, Boss):
            raise TypeError("boss must be an instance of Boss.")
        if self._boss:
            self._boss._workers.remove(self)
        self._boss = new_boss
        if self not in new_boss.workers:
            new_boss.add_worker(self)


boss1 = Boss(1, "Boss1", "Company1")
worker1 = Worker(1, "Worker1", "Company1", boss1)
worker2 = Worker(2, "Worker2", "Company1", boss1)

print(
    f"Workers under {boss1.name}: {[worker.name for worker in boss1.workers]}"
)
print(
    '''
Task 3
    '''
)

from functools import wraps


class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return int(result)

        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return str(result)

        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return bool(result)

        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return float(result)

        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25
assert do_something('True') is True
