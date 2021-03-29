import pytest
import IO
import os

class stuff:
    def __init__(self, inv_name, v_name):
        self.inv_name = inv_name
        self.v_name = v_name
        self.f_dir = "{}/".format(os.getcwd())

    def make_valid_file(self):
        with open("{}{}".format(self.f_dir, self.v_name), mode='a'):
            pass






@pytest.fixture
def f_dir():
    print("Fixture f_dir")
    s = stuff("testfile_invalid.txt", "testfile.txt")
    return s.f_dir


@pytest.fixture
def invalid_file_name():
    print("Fixture invalid_file_name")
    s = stuff("testfile_invalid.txt", "testfile.txt")
    return s.inv_name

@pytest.fixture
def valid_file_name():
    print("Fixture valid_file_name")
    s = stuff("testfile_valid.txt", "testfile.txt")
    s.make_valid_file()
    return s.v_name



def test_read_df_invalid(f_dir, invalid_file_name):
    print("Test invalid file name")
    with pytest.raises(RuntimeError):
        IO.read_df(f_dir, invalid_file_name)


def test_read_df_valid(f_dir, valid_file_name):
    print("Test valid file name")
    with pytest.raises(RuntimeError):
        IO.read_df(f_dir, valid_file_name)

@pytest.fixture
def cleanup(valid_file_name):
    print("cleaning the valid filename")
    p = "{}/{}".format(os.getcwd(), valid_file_name)
    print(p)
    os.remove(p)
    return p


def test_assert_delete(cleanup):
    print(cleanup)
    assert not os.path.exists(cleanup)
