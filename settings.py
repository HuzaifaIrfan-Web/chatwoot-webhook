


from pydantic import Field

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    CHATWOOT_URL: str = Field(default="http://chatwoot.home", alias="CHATWOOT_URL")

    CHATWOOT_API_TOKEN: str = Field(default="7KC6MKk1Xpywux7nJimcHB5K", alias="CHATWOOT_API_TOKEN")
    CHATWOOT_WEBSITE_TOKEN: str = Field(default="SyfNF8ANTbfEdirBLG3Z3qvj", alias="CHATWOOT_WEBSITE_TOKEN")
    KAFKA_URL: str = Field(default="kafka:9092", alias="KAFKA_URL")

    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding = "utf-8",
        populate_by_name=True 
    )



settings = Settings()
