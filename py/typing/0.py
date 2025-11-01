from typing import Annotated, Any, Literal


class Settings:
    envs = Literal['dev', 'prod']

    config = Annotated[str, "uuid"]


def get_any(anyone: Any) -> Any:
    if isinstance(anyone, str):
        return "str"
    elif isinstance(anyone, int):
        return "int"
    elif isinstance(anyone, tuple):
        return "tuple"
    elif isinstance(anyone, list):
        return "lis"
    return None


def main() -> None:
    settings = Settings()

    gt = get_any("hello")

    print(settings.config, gt)


if __name__ == '__main__':
    main()

