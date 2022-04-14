from random import random
from locust import HttpUser, between, task


class User(HttpUser):
    wait_time = between(0.1, 0.5)

    @task(4)
    def heavy_load(self):
        self.client.get("")
        self.client.get("cats")

    # /other

    @task(1)
    def page_other(self):
        self.client.get("other")
        number = int(random() * 1000)
        self.client.get(f"/other?page={number}", name="/other")

    # /exp

    @task(2)
    def page_exp(self):
        number = int(random() * 1000)
        self.client.get(f"/exp?value={number}", name="/exp")
