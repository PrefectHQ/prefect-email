"""This is an example flows module"""
from prefect import flow

from prefect_email.tasks import (
    goodbye_prefect_email,
    hello_prefect_email,
)


@flow
def hello_and_goodbye():
    """
    Sample flow that says hello and goodbye!
    """
    print(hello_prefect_email)
    print(goodbye_prefect_email)
