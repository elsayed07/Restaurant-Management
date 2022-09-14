from project import service, taxes, assign_table


def main():
    test_service()
    test_taxes()
    test_assign_table()


def test_service():
    assert service(check=20, table="small") == 0
    assert service(check=20, table="regular")== 1
    assert service(check=20, table="large") == 2


def test_taxes():
    assert taxes(check=20) == 2
    assert taxes(check=100) == 10


def test_assign_table(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 2)
    persons_n = input("to assign the right table, how many persons are there: ")
    assert persons_n == 2
    assert assign_table() == "small"

    monkeypatch.setattr('builtins.input', lambda _: 4)
    persons_n = input("to assign the right table, how many persons are there: ")
    assert persons_n == 4
    assert assign_table() == "regular"

    monkeypatch.setattr('builtins.input', lambda _: 7)
    persons_n = input("to assign the right table, how many persons are there: ")
    assert persons_n == 7
    assert assign_table() == "large"


if __name__ == "__main__":
    main()