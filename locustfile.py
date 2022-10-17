from locust import HttpUser, task

class WikiAPI(HttpUser):
    @task
    def wikiSearch(self):
        self.client.get("/")
        # self.client.get("/world")