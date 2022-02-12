import hospital_db
from module import user_management  as um
from module.user_management.add_user import add_user


def test_user_management():
    a = add_user("patient", 1, "Jason", 16)
    assert(a==0)


if __name__ == '__main__':
    test_user_management()