# prefect-email

## Welcome!

`prefect-email` is a collection of prebuilt Prefect tasks that can be used to quickly construct Prefect flows that interacts with email services..

## Getting Started

### Python setup

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `prefect-email` with `pip`:

```bash
pip install prefect-email
```

### Send an email using Gmail

```python
from prefect import flow
from prefect_email import EmailServerCredentials, email_send_message

@flow
def example_email_send_message_flow():
    email_server_credentials = EmailServerCredentials(
        username="your_email_address@gmail.com",
        password="MUST_be_an_app_password_here!",
    )
    subject = email_send_message(
        email_server_credentials=email_server_credentials,
        subject="Example Flow Notification using Gmail",
        msg="This proves email_send_message works!",
        email_to="someone_awesome@gmail.com",
    )
    return subject

example_email_send_message_flow()
```

Please note, many email services, like Gmail, require an [App Password](https://support.google.com/accounts/answer/185833) to successfully send emails. If you encounter an error similar to `smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted...`, it's likely you are not using an App Password.

## Resources

If you encounter and bugs while using `prefect-email`, feel free to open an issue in the [prefect-email](https://github.com/PrefectHQ/prefect-email) repository.

If you have any questions or issues while using `prefect-email`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

## Development

If you'd like to install a version of `prefect-email` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/PrefectHQ/prefect-email.git

cd prefect-email/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
