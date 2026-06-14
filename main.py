# This is a sample Python script.
from sqlalchemy.testing import db
from sqlalchemy.testing.config import db_url

from service.candidate_selector import CandidateSelector

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#CandidateSelector.get_candidate_requests(db,31.768300,35.213700,2002,4.5,100000000)
from database import SessionLocal
from service.candidate_selector import CandidateSelector

db = SessionLocal()

selector = CandidateSelector(db)

result = selector.get_candidate_requests(
    31.768300,
    35.213700,
    2002,
    4.5,
    100000000
)

print(result)

db.close()