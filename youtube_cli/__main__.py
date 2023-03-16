#!/usr/bin/env python

import os

from pyyoutube.models import Playlist
from pyyoutube import Api


api = Api(client_id=os.environ["ID"], client_secret=os.environ["SECRET"])
print(api.get_authorization_url())
response = input("response:")
api.generate_access_token(authorization_response=response)

# channel_by_mine = api.get_channel_info(mine=True)
# print(channel_by_mine)
# channel_id = channel_by_mine.items[0].id
#
# playlists_by_channel = api.get_playlists(channel_id=channel_id)
# print(playlists_by_channel.items)


playlists_by_mine = api.get_playlists(mine=True)
playlist : Playlist
for playlist in playlists_by_mine.items:
    print(playlist.to_json())
