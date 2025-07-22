# This turbo Intruder script is used to inject payloads into a POST request, then makes a get request to a seperate URL. Ideal for when the POST data is reflected in a different web page.
# Turbo Intruder script to send a payload-injected request (with %s placeholder),
# followed by a GET request to another page.

def queueRequests(target, wordlists):
    engine = RequestEngine(
        endpoint=target.endpoint,
        concurrentConnections=5,
        requestsPerConnection=100,
        pipeline=False
    )

    # Load payloads from external file
    with open('/path/to/wordlist.txt', 'r') as f:
        payloads = [line.strip() for line in f]

    # Use the base request you sent from Burp, which should contain `%s`
    base = target.baseRequest.decode()

    for payload in payloads:
        # Replace the %s placeholder in the original request with the payload
        attack_request = base.replace('%s', payload)

        # Send the original request with payload
        engine.queue(attack_request)

        # === Modify this path as needed — this is the follow-up GET request ===
        followup_get = """GET /results HTTP/1.1
Host: example.com

"""
        engine.queue(followup_get)

# Add responses to the results table if HTTP 200
def handleResponse(req, interesting):
    if req.status == 200:
        table.add(req)
