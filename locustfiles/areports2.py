import random
import json
from locust import HttpUser,SequentialTaskSet, User, TaskSet, task, between

class Test(TaskSet):
    @task
    def pages(self):
        self.client.get("/api/v3/templates/24884/output?output=base64&key=e2b73c33ebc402fcaa05205de569a43c&secret=e45c2b47cdff177ab5a4a46910fcee1e&workspace=info@actualreports.com&data=https://pdfapi-test-data-bucket.s3.amazonaws.com/shopify.json")

class WebUsers(HttpUser):
    email = "NOT_FOUND"
    password = "NOT_FOUND"
    name = "NOT_FOUND"
    headers = {'content-type': 'application/json'}
    wait_time = between(0.1, 1)
    weight = 1
    tasks = { Test:1 }
