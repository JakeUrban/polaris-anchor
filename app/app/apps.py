from django.apps import AppConfig


class MyAppConfig(AppConfig):
    name = "app"

    def ready(self):
        from .integrations import (
            MyDepositIntegration,
            MyWithdrawalIntegration,
            MyRailsIntegration,
            toml
        )
        from polaris.integrations import register_integrations

        register_integrations(
            deposit=MyDepositIntegration(),
            withdrawal=MyWithdrawalIntegration(),
            rails=MyRailsIntegration(),
            toml_func=toml
        )
