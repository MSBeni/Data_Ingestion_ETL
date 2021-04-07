import json
import facebook

secrets = json.loads(open('../../../facebook_app_credential.json', 'r').read())


def main():
    token = {secrets['auth']['access_token']}
    graph = facebook.GraphAPI(token)
    fields = ['id', 'name', 'about', 'emails', 'likes', 'posts']
    fields = ','.join(fields)
    page = graph.get_object("Bituniex", fields=fields)

    print(json.dumps(page, indent=4))

if __name__ == "__main__":
    main()