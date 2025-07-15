from base64 import b64encode

def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False)

    # 📝 Load wordlist from file
    wordlist_path = '/full/path/to/your/wordlist.txt'
    with open(wordlist_path, 'r') as f:
        payloads = [line.strip() for line in f if line.strip()]

    for word in payloads:
        # Replace placeholder with word
        modified = target.req.replace(b'§PAYLOAD§', word.encode())

        # Base64 encode region
        modified = encode_selected_region(modified)

        # Update content-length if POST body changed
        modified = update_content_length(modified)

        # Optional debug output:
        print(modified.decode(errors='ignore'))

        # Queue modified request
        engine.queue(modified)

def encode_selected_region(request):
    start_tag = b'§ENCODE_START§'
    end_tag = b'§ENCODE_END§'

    start = request.find(start_tag)
    end = request.find(end_tag)

    if start == -1 or end == -1 or end <= start:
        return request  # Tags not found

    # Extract and encode the region
    pre = request[:start]
    to_encode = request[start + len(start_tag):end]
    post = request[end + len(end_tag):]

    encoded = b64encode(to_encode)
    return pre + encoded + post

def update_content_length(request):
    parts = request.split(b'\r\n\r\n', 1)
    if len(parts) != 2:
        return request  # Not a valid HTTP request

    headers, body = parts
    new_length = str(len(body)).encode()

    lines = headers.split(b'\r\n')
    for i, line in enumerate(lines):
        if line.lower().startswith(b'content-length:'):
            lines[i] = b'Content-Length: ' + new_length
            break
    else:
        lines.append(b'Content-Length: ' + new_length)

    return b'\r\n'.join(lines) + b'\r\n\r\n' + body

def handleResponse(req, interesting):
    if b'success' in req.response:
     
table.add(req)
