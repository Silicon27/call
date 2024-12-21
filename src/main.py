import argparse
import requests
import json
import time

COLOR_BLUE = '\033[94m'
COLOR_GREEN = '\033[92m'
COLOR_YELLOW = '\033[93m'
COLOR_RESET = '\033[0m'
COLOR_ORANGE = '\033[33m'
COLOR_RED = '\033[31m'
COLOR_LIGHT_BLUE = '\033[36m'
COLOR_PURPLE = '\033[35m'
COLOR_PINK = '\033[95m'
COLOR_WHITE = '\033[97m'
COLOR_GRAY = '\033[90m'
COLOR_MAGENTA = '\033[95m'
COLOR_CYAN = '\033[96m'
COLOR_LIGHT_GREEN = '\033[92m'
COLOR_LIGHT_YELLOW = '\033[93m'
COLOR_LIGHT_RED = '\033[91m'
COLOR_LIGHT_PURPLE = '\033[95m'
UNDERLINE = '\033[4m'

def call_api(url: str, method: str, headers: dict, data: dict, only_content: bool, show_metrics: bool, average_response_time: int) -> None:
    
    if average_response_time:
        response_times = []
        for _ in range(average_response_time):
            start = time.time()
            response = requests.request(method, url, headers=headers, json=data)
            end = time.time()
            response_times.append(end - start)
        
        print(f"{COLOR_BLUE}Average response time: {COLOR_RESET}{COLOR_GREEN}{sum(response_times) / len(response_times):.2f}s{COLOR_RESET}")
        return
    
    if not only_content:
        print(f"{COLOR_YELLOW}[Calling API at {url}]{COLOR_RESET}")
    try:
        start = time.time()
        response = requests.request(method, url, headers=headers, json=data)
        end = time.time()
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"{COLOR_RED}Error: {e}{COLOR_RESET}")
        return
    
    if only_content:
        print(response.text)
    else:
        print(f"{COLOR_BLUE}Response status code: {COLOR_RESET}{COLOR_GREEN}{response.status_code}{COLOR_RESET}")
        print(f"{COLOR_BLUE}Response content: {COLOR_RESET}{response.text}")
        
    if show_metrics:
        print(f"{COLOR_BLUE}Response time: {COLOR_RESET}{COLOR_GREEN}{end - start:.2f}s{COLOR_RESET}")
        print(f"{COLOR_BLUE}Response headers: {COLOR_RESET}{response.headers}")
        print(f"{COLOR_BLUE}Response cookies: {COLOR_RESET}{response.cookies}")
        

def main() -> None:
    parser = argparse.ArgumentParser(description="CLI program for API testing")
    parser.add_argument("url", type=str, help="URL to send request to")
    parser.add_argument("--method", type=str, default="GET", help=f"HTTP method to use [DEFAULT: {COLOR_CYAN}GET{COLOR_RESET}]")
    parser.add_argument("-H", "--header", type=json.loads, help="Headers to include in request as a JSON string")
    parser.add_argument("-d", "--data", type=json.loads, help="Data to include in request as a JSON string")
    
    parser.add_argument("--only-content", action="store_true", help="Only print the content of the response")
    parser.add_argument("-m", "--metrics", action="store_true", help="Print metrics of the response")
    
    parser.add_argument("-a", "--average-response-time", type=int, nargs="?", help="Print the average response time of the API")
    
    args = parser.parse_args()
    
    headers = args.header if args.header else {}
    data = args.data if args.data else {}
    
    call_api(args.url, args.method, headers, data, args.only_content, args.metrics, args.average_response_time if args.average_response_time else 0)

if __name__ == "__main__":
    main()