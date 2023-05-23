import argparse
import requests

def make_request(url, file):
    # Read the contents of the file
    with open(file, 'r') as f:
        file_content = f.read()

    # Replace {SS} in the URL with the file content
    modified_url = url.replace('{SS}', file_content)

    # Make the HTTP request
    response = requests.get(modified_url)

    # Save response details to a file
    with open('response_details.txt', 'a') as f:
        f.write(f"URL: {modified_url}\n")
        f.write(f"Response Code: {response.status_code}\n")
        f.write(f"Port: {response.url}\n")
        f.write("\n")

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Make HTTP requests with file content')
parser.add_argument('--url', type=str, help='URL with {SS} placeholder')
parser.add_argument('--file', type=str, help='File containing text to replace {SS}')
args = parser.parse_args()

# Check if URL and file arguments are provided
if args.url and args.file:
    make_request(args.url, args.file)
else:
    print('Please provide both --url and --file arguments.')
