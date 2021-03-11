import random
import json
from locust import HttpUser,SequentialTaskSet, User, TaskSet, task, between


class Heavypdf(TaskSet):
    @task
    def pages(self):
        self.client.get("/api/v3/templates/24839/output?name=LoadTesting&format=pdf&output=base64&data=https://pdfapi-test-data-bucket.s3.amazonaws.com/large_invoice_test.json&key=e2b73c33ebc402fcaa05205de569a43c&secret=e45c2b47cdff177ab5a4a46910fcee1e&workspace=info@actualreports.com")

class Frontpage(TaskSet):
    @task
    def pages(self):
        self.client.get("/")

class Price(TaskSet):
    @task
    def pages(self):
        self.client.get("/pricing")

class Invoice(TaskSet):
    @task
    def pages(self):
        self.client.get("/api/v3/templates/24386/output?name=LoadTesting&format=pdf&output=base64&data=https://pdfgeneratorapi.com/example-documents/34873/json&key=61e5f04ca1794253ed17e6bb986c1702&secret=68db1902ad1bb26d34b3f597488b9b28&workspace=demo.example@actualreports.com")

class InvoiceWithMerge(TaskSet):
    @task
    def pages(self):
        self.client.post("/api/v3/templates/output?name=load-test&format=pdf&output=base64&workspace=info@actualreports.com&key=e2b73c33ebc402fcaa05205de569a43c&secret=e45c2b47cdff177ab5a4a46910fcee1e", json=[{'template':24847,'data':'https://pdfapi-test-data-bucket.s3.amazonaws.com/shopify.json'},{'template':24848,'data':'https://pdfapi-test-data-bucket.s3.amazonaws.com/shopify.json'}])

class WebUsers(HttpUser):
    email = "NOT_FOUND"
    password = "NOT_FOUND"
    name = "NOT_FOUND"
    headers = {'content-type': 'application/json'}
    wait_time = between(1, 1)
    weight = 1
    tasks = {Heavypdf:1, Frontpage:1, Price:1, Invoice:3, InvoiceWithMerge:0}
