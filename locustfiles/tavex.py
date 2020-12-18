import random
import json
from locust import HttpUser,SequentialTaskSet, User, TaskSet, task, between

class Frontpage(TaskSet):
    @task
    def pages(self):
        self.client.get("/")

class Price(TaskSet):
    @task
    def pages(self):
        self.client.get("/valuuta-hinnakiri-tallinn")

class WebUsers(HttpUser):
    email = "NOT_FOUND"
    password = "NOT_FOUND"
    name = "NOT_FOUND"
    headers = {'content-type': 'application/json'}
    wait_time = between(1, 1)
    weight = 1
    tasks = { Frontpage:3, Price:1}
