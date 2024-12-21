# Ayonix

A CLI program for API testing.

## Features

- Send HTTP requests to specified URLs
- Supports GET, POST, PUT, DELETE, and other HTTP methods
- Include headers and data in requests
- Measure and display response time
- Calculate average response time over multiple requests
- Display response status code, headers, and content

## Installation

You can install the package using `pip`:
```bash
pip install ayonix
```

## Usage

The usage name for Ayonix is `call`:
```bash
call "https://jsonplaceholder.typicode.com/posts" --method POST -H '{"Content-Type": "application/json"}' -d '{"title": "foo", "body": "bar", "userId": 1}'
```
