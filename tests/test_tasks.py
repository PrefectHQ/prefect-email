from prefect import flow

from prefect_email.tasks import (
    goodbye_prefect_email,
    hello_prefect_email,
)


def test_hello_prefect_email():
    @flow
    def test_flow():
        return hello_prefect_email()

    flow_state = test_flow()
    task_state = flow_state.result()
    assert task_state.result() == "Hello, prefect-email!"


def goodbye_hello_prefect_email():
    @flow
    def test_flow():
        return goodbye_prefect_email()

    flow_state = test_flow()
    task_state = flow_state.result()
    assert task_state.result() == "Goodbye, prefect-email!"
