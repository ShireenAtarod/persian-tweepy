from instagram.client import InstagramAPI

access_token = "231701122.cf769c1.4410605eb51244228f82428280c6bffe"
client_id = "2099951852.1677ed0.6fdea38690f040a7a75decaa4869eb8a"
client_secret = "a0ac0cc51a7744a59831f46eb3ea574c"

api = InstagramAPI(access_token=access_token, client_secret=client_secret)

recent_media, next_ = api.tag_recent_media(count=20, tag_name='hotdog')
# recent_media, next_ = api.user_recent_media()
# photos = []
# for media in recent_media:
#     photos.append('<img src="%s"/>' % media.images['thumbnail'].url)