from dynaconf import Dynaconf


def get_settings():
    settings = Dynaconf(
        settings_files=["settings.toml", ".secrets.toml"],
        environments=True,
    )
    settings.setenv(settings.env)
    return settings
