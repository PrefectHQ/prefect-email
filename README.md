# prefect-email

## Welcome!

prefect-email is a collection of prebuilt Prefect tasks that can be used to quickly construct Prefect flows.

## Getting Started

### Python setup

Requires an installation of Python 3.7+

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `prefect-email` with `pip`

```bash
pip install prefect-email
```

### Write and run a flow

```python
from prefect import flow
from prefect_email.tasks import (
    goodbye_prefect_email,
    hello_prefect_email,
)


@flow
def example_flow():
    hello_prefect_email
    goodbye_prefect_email

example_flow()
```

## Resources

If you encounter and bugs while using `prefect-email`, feel free to open an issue in the [prefect-email](https://github.com/PrefectHQ/prefect-email) repository.

If you have any questions or issues while using `prefect-email`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack)

## Development

If you'd like to install a version of `prefect-email` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/PrefectHQ/prefect-email.git

cd prefect-email/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
