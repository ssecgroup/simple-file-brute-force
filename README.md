# simple file brute force
 Python Code - URL Endpoint Testing
This Python code allows you to test multiple URL endpoints by providing a list of URLs and corresponding endpoints. It performs HTTP requests to each URL by replacing the {SS} placeholder in the endpoint with the content from the file list. The response details, including the HTTP status code, port, and URL, are saved to a file.

Features
Supports testing multiple URL endpoints with different file contents
Customizable endpoint placeholder ({SS}) for file content substitution
Saves response details to a file for further analysis
Requirements
Python 3.x
Requests library (install via pip install requests)
Usage
Clone the repository or download the Python code file.
Install the required dependencies by running pip install requests.
Update the urls.txt file with your desired list of URLs.
Run the code using the command: python url_endpoint_test.py --url <URL_ENDPOINT> --f <FILE_PATH>.
Replace <URL_ENDPOINT> with the endpoint URL you want to test.
Replace <FILE_PATH> with the path to your file containing the content to substitute in the endpoint.
The response details will be saved to the response_details.txt file.
Feel free to customize the code according to your specific requirements and adapt it to your projects.

License
This project is licensed under the MIT License.

Happy testing and coding! If you have any questions or suggestions, feel free to reach out.