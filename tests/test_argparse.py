import argparse
import shlex


def test_repeated_arguments_with_append():
    parser = argparse.ArgumentParser()
    parser.add_argument("--arg", action="append")

    command = shlex.split("--arg 1 --arg 2 --arg 3")
    options = parser.parse_args(command)

    assert options.arg == ["1", "2", "3"]


def test_repeated_arguments_with_extend():
    parser = argparse.ArgumentParser()
    parser.add_argument("--arg", action="extend")

    command = shlex.split("--arg 1 --arg 2 --arg 3")
    options = parser.parse_args(command)

    assert options.arg == ["1", "2", "3"]


def test_repeated_arguments_with_multiple_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--arg", action="extend", nargs="+")

    command = shlex.split("--arg 1 --arg 2 3")
    options = parser.parse_args(command)

    assert options.arg == ["1", "2", "3"]


def test_repeated_arguments_with_extend_and_list_type():
    parser = argparse.ArgumentParser()
    parser.add_argument("--arg", action="extend", type=list)

    command = shlex.split("--arg 1 --arg 2 --arg 3")
    options = parser.parse_args(command)

    assert options.arg == ["1", "2", "3"]


def test_repeated_arguments_with_append_and_list_type():
    parser = argparse.ArgumentParser()
    parser.add_argument("--arg", action="append", type=list)

    command = shlex.split("--arg 1 --arg 2 --arg 3")
    options = parser.parse_args(command)

    assert options.arg == [["1"], ["2"], ["3"]]
