"""A Python Pulumi program"""

import os
import pulumi
from pulumi_authentik import (
    Provider as AuthentikProvider,
    Application,
    get_user,
)


cfg = pulumi.Config()


authentik = AuthentikProvider(
    "authentik",
    url="http://localhost:9000",
    insecure=True,
    token=os.environ["AUTHENTIK_TOKEN"],
)
app = Application(
    "app",
    opts=pulumi.ResourceOptions(provider=authentik),
    name="app",
    slug="app",
)  # TODO: setup app

admin_user = get_user(
    "admin_user",
    username="admin",
    opts=pulumi.InvokeOptions(provider=authentik),
)
# assign the user to the app

# TODO: setup roles
