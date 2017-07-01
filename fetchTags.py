from instagram.client import InstagramAPI

access_token = "231701122.cf769c1.4410605eb51244228f82428280c6bffe"
client_secret = "a0ac0cc51a7744a59831f46eb3ea574c"

api = InstagramAPI(access_token=access_token, client_secret=client_secret)
result, url = api.tag_recent_media(tag_name='hotdog')
media = api.media_popular(count=10)