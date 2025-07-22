# This turbo Intruder script is used to inject payloads into a POST request, then makes a get request to a seperate URL. Ideal for when the POST data is reflected in a different web page.
# Turbo Intruder script: Send POST requests with payloads from a file,
# then follow each with a GET request, and log all 200 OK responses.

def queueRequests(target, wordlists):
    # Create the request engine to manage concurrent connections
    engine = RequestEngine(
        endpoint=target.endpoint,
        concurrentConnections=5,
        requestsPerConnection=100,
        pipeline=False
    )

    # Load payloads from an external wordlist file
    with open('/path/to/wordlist.txt', 'r') as f:
        payloads = [line.strip() for line in f]

    for payload in payloads:
        # === UPDATE: Replace "/submit" with your actual POST endpoint ===
        post_req = """POST /submit HTTP/1.1
Host: example.com
Content-Type: application/json
Content-Length: {length}

{{"input": "{}"}}""".format(payload)

        # === UPDATE: Replace "/results" with your actual GET endpoint ===
        get_req = """GET /results HTTP/1.1
Host: example.com

"""

        # Queue both the POST and GET requests for each payload
        engine.queue(post_req)
        engine.queue(get_req)

# Add any response to the results table if it returns HTTP 200
def handleResponse(req, interesting):
    # Check if the response has a 200 OK status code
    if req.status == 200:
        table.
        add(req)
