Turbo Intruder scripts

example for InjectEncodeB64:

POST /api/login HTTP/1.1 \n
Host: target.com \n
Content-Type: application/json \n
Content-Length: ... \n

{
    "username": "§ENCODE_START§admin§PAYLOAD§123§ENCODE_END§",
    "password": "password"

}
