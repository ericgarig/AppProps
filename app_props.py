import yaml


class AppProps:
    _instance = None
    _config = {}
    _config_filepath = None

    def __new__(cls, config_path: str = "", filepath: str = "configuration.yml"):
        if cls._instance is None:
            cls._instance = super(AppProps, cls).__new__(cls)
            cls._init_from_config_file(filepath)
        return cls._get_config(config_path)

    @classmethod
    def _init_from_config_file(cls, filepath: str):
        with open(filepath, "r") as stream:
            try:
                cls._config = yaml.safe_load(stream)
                cls._config_filepath = filepath
            except yaml.YAMLError as e:
                print(e)

    @classmethod
    def _get_config(cls, path: str, sub_config: dict = None) -> str:
        """Get value of dot-delimited config path."""
        if not path:
            return ""
        [path, remaining] = path.split(".", 1) if path.count(".") else [path, None]
        working_dict = sub_config if sub_config else cls._config
        sub_dict = working_dict.get(path)
        if sub_dict is None:
            raise KeyError(
                f"unable to find '{path}' configuration property in '{cls._config_filepath}'."
            )
        if remaining:
            return cls._get_config(remaining, sub_dict)
        return sub_dict
