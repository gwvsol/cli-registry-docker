import sys
from pathlib import Path
from dotenv import load_dotenv

env: str = '.env'

base_dir = Path(__file__).parent.parent
env_file = base_dir


if base_dir.as_posix() in sys.executable:
    env_file = base_dir/env

else:

    if __file__.find('tmp') != -1:
        base_dir = Path(sys.executable).parent

    if base_dir.as_posix().find('bin') != -1:
        base_dir = base_dir.parent.parent.parent

    env_file = base_dir/env


if env_file.is_file():
    load_dotenv(dotenv_path=env_file.as_posix())


if __name__ == "__main__":
    from registry.__main__ import main
    main()
