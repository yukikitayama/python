# REST

## Request

`?` in the request URI separates the resource identification from additional request parameters.

## Response

Consists of header and contents

`Content-Type` describes what the server response's contents format is.

## json-server

`json-server --watch FILE.json`

## requests

Needs server's address and the service port number. Default 80 if the port number is omitted.

`text` property stores the raw response's contents as string.

Response method `json()` can be used if the server response's header `Content-Type` contains `application/json`.

## CRUD

Create (POST), Read (GET), Update (PUT), Delete (DELETE)

