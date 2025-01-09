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

> [!IMPORTANT]
> The flag [`-d` `--data`] is deprecated and fully out of support, has been renamed to [`-b` `--body`]


The usage name for Ayonix is `call`:
```bash
call "https://jsonplaceholder.typicode.com/posts" --method POST -H '{"Content-Type": "application/json"}' -b '{"title": "foo", "body": "bar", "userId": 1}'
```

The following table shows the available flags that Ayonix allows for:

# CLI Flags and Arguments

| **Flag/Argument**         | **Type**       | **Default**  | **Description**                                                                 |
|---------------------------|----------------|--------------|---------------------------------------------------------------------------------|
| `url`                     | `str`          | Required     | URL to send the request to.                                                    |
| `--method`                | `str`          | `GET`        | HTTP method to use (e.g., GET, POST, PUT, DELETE).                             |
| `-H`, `--header`          | `JSON string`  | None         | Headers to include in the request as a JSON string.                            |
| `-b`, `--body`            | `JSON string`  | None         | Body data to include in the request as a JSON string.                          |
| `--only-content`          | `flag`         | `False`      | Only print the content of the response.                                        |
| `--only-res-code`         | `flag`         | `False`      | Only print the response code.                                                  |
| `-m`, `--metrics`         | `flag`         | `False`      | Print metrics of the response (e.g., time, headers, cookies).                  |
| `-a`, `--average-response-time` | `int`   | None         | Calculate and print the average response time (number of requests specified).  |


