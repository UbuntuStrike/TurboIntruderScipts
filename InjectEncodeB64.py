from base64 import b64encode

def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False
                           )

    for word in wordlists['default']:
        # Insert the payload
        modified = target.req.replace(b'§PAYLOAD§', word.encode())

        # Encode the region between §ENCODE_START§ and §ENCODE_END§
        encoded = encode_selected_region(modified)

        engine.queue(encoded)

def encode_selected_region(request):
    start_tag = b'§ENCODE_START§'
    end_tag = b'§ENCODE_END§'

    start = request.find(start_tag)
    end = request.find(end_tag)

    if start == -1 or end == -1 or end <= start:
        return request  # Tags not found or invalid, return unmodified

    pre = request[:start]
    to_encode = request[start + len(start_tag):end]
    post = request[end + len(end_tag):]

    encoded_part = b64encode(to_encode)
    return pre + encoded_part + post

def handleResponse(req, interesting):
    if b"something_interesting" in req.response:
        tabl
e.add(req)
