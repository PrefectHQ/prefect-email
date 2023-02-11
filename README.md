# prefect-email

<p align="center">
    <!--- Insert a cover image here -->
    <!--- <br> -->
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

Visit the full docs [here](https://PrefectHQ.github.io/prefect-email) to see additional examples and the API reference.

`prefect-email` is a collection of prebuilt Prefect integrations that can be used to interact with email services.

## Getting Started

### Integrate with Prefect flows

Simplify your email communications and ensure task completion with the `prefect-email` library.

This powerful tool makes sending emails effortless, giving you peace of mind that your tasks are being completed as expected.

```python
from prefect import flow
from prefect_email import EmailServerCredentials, email_send_message

@flow
def example_email_send_message_flow():
    email_server_credentials = EmailServerCredentials.load("BLOCK-NAME-PLACEHOLDER")
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

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Saving credentials to block

Note, to use the `load` method on Blocks, you must already have a block document [saved through code](https://orion-docs.prefect.io/concepts/blocks/#saving-blocks) or [saved through the UI](https://orion-docs.prefect.io/ui/blocks/).

Below is a walkthrough on saving block documents through code.

3. Click "+ Create new secret key".
4. Copy the generated API key.
5. Create a short script, replacing the placeholders (or do so in the UI).

```python
from prefect_email import EmailServerCredentials

credentials = EmailServerCredentials(
    username="EMAIL-ADDRESS-PLACEHOLDER",
    password="PASSWORD-PLACEHOLDER",  # must be an app password
)
credentials.save("BLOCK-NAME-PLACEHOLDER")
```

Congrats! You can now easily load the saved block, which holds your credentials:

```python
from prefect_email import EmailServerCredentials

EmailServerCredentials.load("BLOCK_NAME_PLACEHOLDER")
```

!!! info "Registering blocks"

    Register blocks in this module to
    [view and edit them](https://orion-docs.prefect.io/ui/blocks/)
    on Prefect Cloud:

    ```bash
    prefect block register -m prefect_email
    ```

A list of available blocks in `prefect-email` and their setup instructions can be found [here](https://PrefectHQ.github.io/prefect-email/blocks_catalog).

### Feedback

If you encounter any bugs while using `prefect-email`, feel free to open an issue in the [prefect-email](https://github.com/PrefectHQ/prefect-email) repository.

If you have any questions or issues while using `prefect-email`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).
 
Feel free to star or watch [`prefect-email`](https://github.com/PrefectHQ/prefect-email) for updates too!

### Contributing
If you'd like to help contribute to fix an issue or add a feature to `prefect-email`, please [propose changes through a pull request from a fork of the repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork).

Here are the steps:

1. [Fork the repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository)
2. [Clone the forked repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository)
3. Install the repository and its dependencies:
```
pip install -e ".[dev]"
```
4. Make desired changes
5. Add tests
6. Insert an entry to [CHANGELOG.md](https://github.com/PrefectHQ/prefect-email/blob/main/CHANGELOG.md)
7. Install `pre-commit` to perform quality checks prior to commit:
```
pre-commit install
```
8. `git commit`, `git push`, and create a pull request
