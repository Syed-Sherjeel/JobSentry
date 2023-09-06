from locust import HttpUser, task, between


class AppUser(HttpUser):
    wait_time = between(2,5)

    @task
    def home_page(self):
        self.client.get("/")

    @task
    def register(self):
        self.client.get("/register/")

    @task
    def login_page(self):
        self.client.get("/login/")

