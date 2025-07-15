Turbo Intruder scripts

example for InjectEncodeB64:
POST /api/login HTTP/1.1
Host: target.com
Content-Type: application/json
Content-Length: ...

{
    "username": "§ENCODE_START§admin§PAYLOAD§123§ENCODE_END§",
    "password": "password"

}
