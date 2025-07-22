#This turbo Intruder script is used to inject payloads into a POST request, then makes a get request to a seperate URL. Ideal for when the POST data is reflected in a different web page.
def queueRequests(target,wordlist)
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False)

    for word in wordlists['Passwords']:
        post_req = """POST /submit HTTP/1.1
Host: example.com
Content-Type: application/json
Content-Length: {length}

{"input": "%s"}""" % word

        get_req = "GET /results HTTP/1.1\nHost: example.com\n\n"

        # Send POST and then GET
        engine.queue(post_req)
        engine.queue(get_req)

def handleResponse(req, interesting):
    if "reflected_input" in req.response:
        table.add(req)
