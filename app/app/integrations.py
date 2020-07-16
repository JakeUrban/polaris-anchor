from .forms import AmountForm
from polaris.models import Asset
from polaris.integrations import (
    DepositIntegration,
    WithdrawalIntegration,
    RailsIntegration
)


class MyDepositIntegration(DepositIntegration):
    def content_for_transaction(self, transaction, post_data=None, amount=None):
        if transaction.amount_in:
            return
        elif post_data:
            form = AmountForm(transaction, post_data)
        else:
            form = AmountForm(transaction, initial={"amount": amount})
        return {
            "form": form,
            "guidance": "Enter the amount you would like to deposit",
            "title": "Test Anchor",
            "icon_label": "Test SRT Anchor"
        }


class MyWithdrawalIntegration(WithdrawalIntegration):
    def content_for_transaction(self, transaction, post_data=None, amount=None):
        if transaction.amount_in:
            return
        elif post_data:
            form = AmountForm(transaction, post_data)
        else:
            form = AmountForm(transaction, initial={"amount": amount})
        return {
            "form": form,
            "guidance": "Enter the amount you would like to deposit",
            "title": "Test Anchor",
            "icon_label": "Test SRT Anchor"
        }


class MyRailsIntegration(RailsIntegration):
    def poll_outgoing_transactions(self, transactions):
        return list(transactions)

    def poll_pending_deposits(self, pending_deposits):
        print("returning all pending transactions")
        return list(pending_deposits)

    def execute_outgoing_transaction(self, transaction):
        transaction.amount_fee = 0
        transaction.status = transaction.STATUS.pending_external
        transaction.save()


def toml():
    return {
        "DOCUMENTATION": {
            "ORG_NAME": "Stellar Development Foundation",
            "ORG_URL": "https://stellar.org",
            "ORG_DESCRIPTION": "SEP 24 reference server.",
            "ORG_KEYBASE": "stellar.public",
            "ORG_TWITTER": "StellarOrg",
            "ORG_GITHUB": "stellar",
        },
        "CURRENCIES": [
            {
                "code": asset.code.upper(),
                "issuer": asset.issuer,
                "status": "test",
                "is_asset_anchored": False,
                "anchor_asset_type": "other",
                "desc": "A fake anchored asset to use with this example anchor server.",
            }
            for asset in Asset.objects.all()
        ],
        "PRINCIPALS": [
            {
                "name": "Jacob Urban",
                "email": "jake@stellar.org",
                "keybase": "jakeurban",
                "github": "https://www.github.com/JakeUrban",
            }
        ],
    }
