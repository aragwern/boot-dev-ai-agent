from functions.write_file import write_file


def test_write_file():
    print("Result for lorem.txt:")
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)
    print("Result for pkg/morelorem.txt:")
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)
    print("Result for /tmp/temp.txt:")
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)


if __name__ == "__main__":
    test_write_file()
