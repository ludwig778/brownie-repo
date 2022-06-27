from pydantic import BaseSettings, Field


class AppSettings(BaseSettings):
    private_key: str
    etherscan_token: str
    infura_project_id: str = Field(env="WEB3_INFURA_PROJECT_ID")


def get_settings():
    return AppSettings()