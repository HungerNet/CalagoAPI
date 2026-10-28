# Internal Calagopus PublicAPI (unauthenticated panel information)
class PublicAPI:
    def __init__(self, client):
        self.client = client

    def settings(self):
        return self.client.get('/api/settings')

    def languages(self):
        return self.client.get('/api/languages')['languages']

    def announcements(self):
        return self.client.get('/api/announcements')['announcements']
