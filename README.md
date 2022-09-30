# prefect-email

<p align="center">
    <a href="https://pypi.python.org/pypi/prefect-email/" alt="PyPI version">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/prefect-email?color=0052FF&labelColor=090422"></a>
    <a href="https://github.com/PrefectHQ/prefect-email/" alt="Stars">
        <img src="https://img.shields.io/github/stars/PrefectHQ/prefect-email?color=0052FF&labelColor=090422" /></a>
    <a href="https://pepy.tech/badge/prefect-email/" alt="Downloads">
        <img src="https://img.shields.io/pypi/dm/prefect-email?color=0052FF&labelColor=090422" /></a>
    <a href="https://github.com/PrefectHQ/prefect-email/pulse" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/m/PrefectHQ/prefect-email?color=0052FF&labelColor=090422" /></a>
    <br>
    <a href="https://prefect-community.slack.com" alt="Slack">
        <img src="https://img.shields.io/badge/slack-join_community-red.svg?color=0052FF&labelColor=090422&logo=slack" /></a>
    <a href="https://discourse.prefect.io/" alt="Discourse">
        <img src="https://img.shields.io/badge/discourse-browse_forum-red.svg?color=0052FF&labelColor=090422&logo=discourse" /></a>
</p>
## Welcome!

`prefect-email` is a collection of prebuilt Prefect tasks that can be used to quickly construct Prefect flows that interacts with email services.

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

Then, register to [view the block](https://orion-docs.prefect.io/ui/blocks/) on Prefect Cloud:

```bash
prefect block register -m prefect_email
```

Note, to use the `load` method on Blocks, you must already have a block document [saved through code](https://orion-docs.prefect.io/concepts/blocks/#saving-blocks) or [saved through the UI](https://orion-docs.prefect.io/ui/blocks/).

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

If you encounter any bugs while using `prefect-email`, feel free to open an issue in the [prefect-email](https://github.com/PrefectHQ/prefect-email) repository.

If you have any questions or issues while using `prefect-email`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

Feel free to ⭐️ or watch [`prefect-email`](https://github.com/PrefectHQ/prefect-email) for updates too!

## Development

If you'd like to install a version of `prefect-email` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/PrefectHQ/prefect-email.git

cd prefect-email/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
