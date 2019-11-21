#!/usr/bin/env python3

from pyaml import yaml
import os
from mastodon import Mastodon


with open("fedi.login", "r") as f:
    login = yaml.load(f.read(), Loader=yaml.FullLoader)

if not os.path.exists(".oauth.secret"):
    Mastodon.create_app(
        "yuibot", api_base_url=login["instance"], to_file=".oauth.secret"
    )
if not os.path.exists(".user.secret"):
    mastodon = Mastodon(client_id=".oauth.secret", api_base_url=login["instance"])
    mastodon.log_in(login["username"], login["password"], to_file=".user.secret")

mastodon = Mastodon(access_token=".user.secret", api_base_url=login["instance"])

if __name__ == "__main__":
    with open("cloud.png", "rb") as f:
        res = mastodon.media_post(f, "image/png")
        mastodon.status_post("@floatingghost", media_ids=[res["id"]], visibility="direct")
