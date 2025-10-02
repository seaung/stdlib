import os
from typing import Any


def get_system_name() -> str:
    return os.name


def get_platform() -> Any:
    os_info = os.uname()
    print(os_info.version)
    return ""


def main() -> None:
    print(get_system_name())
    print(get_platform())


if __name__ == "__main__":
    main()
