import os


def write_data(file_type: str, data: dict) -> None:
    """
    Writes vars into config file for unit tests
    """

    filename = "/.env.json" if file_type == "json" else "/.env"
    separator = ":" if file_type == "json" else "="

    with open(os.getcwd() + filename, "w") as file:
        if filename == "/.env.json":
            file.write("{")

        for k, v in data.items():
            file.write(f"{k}{separator}{v}\n")

        if filename == "/.env.json":
            file.write("}")
