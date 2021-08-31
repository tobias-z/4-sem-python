import argparse

FILE_NAME = "output.csv"


def print_file_content(file_name):
    with open(file_name) as file:
        for line in file:
            print(line.rstrip())


def write_list_to_file(output_file: str, *lines: str):
    with open(output_file, "w") as file:
        for idx, line in enumerate(lines):
            line_to_use = line
            if not line.endswith("\n") and lines[idx] is not lines[-1]:
                line_to_use = line + "\n"
            file.write(line_to_use)


def read_csv(file_name):
    with open(file_name) as file:
        result = []
        for line in file:
            result.append(line)
        return result


def deturmine_cli_action(args):
    if args.file is None:
        return print_file_content(args.path)

    rows = read_csv(args.path)
    write_list_to_file(args.file, *rows)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A system to read and write to a file")
    parser.add_argument("path", help="The path to your file")
    parser.add_argument("--file", help="The file you want to write to")

    args = parser.parse_args()
    deturmine_cli_action(args)
