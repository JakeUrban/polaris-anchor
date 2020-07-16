First, clone the repository:
::

    git clone git@github.com:JakeUrban/polaris-anchor.git
    cd polaris-anchor

Write the following to a ``.env`` file in the root directory:
::

    DJANGO_SECRET_KEY="secretkeykeysecret"
    DJANGO_DEBUG=True

    SIGNING_SEED=<your SEP-10 signing key here>

    # "Test SDF Network ; September 2015" or "Public Global Stellar Network ; September 2015"
    # Or a custom passphrase if you're using a private network.
    STELLAR_NETWORK_PASSPHRASE="Test SDF Network ; September 2015"

    HORIZON_URI="https://horizon-testnet.stellar.org/"
    SERVER_JWT_KEY=<your secret encoding string for SEP-10>
    HOST_URL="http://localhost:8000"
    LOCAL_MODE=True

Run ``docker-compose build``

Now you need to run the server container and create the ``Asset`` object you intend to anchor on testnet.
::

    docker-compose up server
    docker exec -it server python manage.py shell

Then, in python, import and create your ``Asset`` object.
::

    from polaris.models import Asset
    Asset.objects.create(
        code="", 
        issuer="", 
        distribution_seed="", 
        sep24_enabled=True
    )

Kill the server container: ``docker kill server``
Run every container: ``docker-compose up``

You should have a SEP-24 anchor server up on http://localhost:8000
