# Email Verifier

A simple Python script that checks whether an email address follows a basic valid format.

## What it does

This project does not verify whether an email actually exists. It only performs a basic format check such as:

- containing exactly one `@`
- containing a `.` in the domain portion
- not starting with `@`
- not ending with `.`

## Run it

```bash
python emailverifier.py
```

## Example

```text
Please enter your language (Supported Languages: English, Portuguese) >>> english
Please enter your email address >>> name@example.com
Email is Valid
```
