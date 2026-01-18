from functions.get_file_content import get_file_content


def test_get_file_content():
    print("-------- main.py --------------------")
    print(get_file_content("calculator", "main.py"))
    print("-------- pkg/calculator.py ----------")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("-------- /bin/cat -------------------")
    print(get_file_content("calculator", "/bin/cat"))
    print("-------- pkg/does_not_exist.py ------")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))
    print("-------- lorem.txt ------")
    print(get_file_content("calculator", "lorem.txt"))


if __name__ == "__main__":
    test_get_file_content()
