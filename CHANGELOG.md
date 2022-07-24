# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Added

### Changed

- Updated tests to be compatible with core Prefect library (v2.0b9) and bumped required version - [#18](https://github.com/PrefectHQ/prefect_email/pull/18)

### Deprecated

### Removed

### Fixed

### Security

## 0.1.0

Released on March 8th, 2022.

### Changed

- Made `email_to` in `email_send_message` optional as long as one of `email_to`, `email_to_cc`, or `email_to_bcc` is specified - [#2](https://github.com/PrefectHQ/prefect-email/pull/2)

### Added

- `email_send_message` task - [#1](https://github.com/PrefectHQ/prefect-email/pull/1)
