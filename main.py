from pathlib import Path
import argparse
import json
import toml


parser = argparse.ArgumentParser()
parser.add_argument("filepath")
args = parser.parse_args()


def main():
    path: Path = Path(args.filepath)
    data: dict = {}
    with open(path) as file:
        data = json.loads(file.read())

    if path.suffix == ".json":
        toml_path = Path(str(path).replace(".json", ".toml"))
        with open(toml_path, "w+") as file:
            toml.dump(data, file)
            return
    print("Unable to read file...")


if __name__ == "__main__":
    main()
