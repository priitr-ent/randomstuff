from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    def on_start(self):
        self.client.headers = {'SFSESSID': 'bpunmg3rp6t9ktqpp8jt4iblqq'}

    @task
    def hello_world(self):
        self.client.get("/")
