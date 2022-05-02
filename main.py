import pandas as pd
import soundcloud


client = soundcloud.Client(
    client_id=YOUR_CLIENT_ID,
    client_secret=YOUR_CLIENT_SECRET,
    username='jane@example.com',
    password='janespassword'
)

track = client.post('/tracks', track={
    'title': 'This is a sample track',
    'sharing': 'private',
    'asset_data': open('mytrack.mp4', 'rb')
})

if __name__ == '__main__':
    pass
