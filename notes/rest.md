# REST

## Request

`?` in the request URI separates the resource identification from additional request parameters.

## Response

Consists of header and contents

`Content-Type` describes what the server response's contents format is.

## Status code

`204` server successfully fulfilled the request, and no content in the response.

`404` indicates that the requested resource was not found on the server.

`503` (service unavailable) is used when the server is temporarily unable to handle the request.

## json-server

`json-server --watch FILE.json`

## requests

Needs server's address and the service port number. Default 80 if the port number is omitted.

`text` property stores the raw response's contents as string.

Response method `json()` can be used if the server response's header `Content-Type` contains `application/json`.

`requests.Session()` creates persistent session object to store and send authentication credentials in subsequent 
requests.

## CRUD

Create (POST), Read (GET), Update (PUT), Delete (DELETE)

## Socket

`socket.sendto(data, address)` allows you to send data to a given address. Data is bytes-like object. This method is 
typically used with UDP (User Datagram Protocol) sockets. Data is sent as individual packets without establishing a 
persistent connection.

`socket.accept()` is used by a server socket to accept requests from a client socket of another host.

`socket.bind(address)` binds a socket toa specific network address and port combination.

The below uses a UDP socket `SOCK_DGRAM` and `sendto()` method and send data over UDP.

```
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect(('localhost', 8080))
client_socket.sendto("Hello, server!", ('localhost', 8080))
client_socket.close()
```

The below sends data over a TCP socket connection `SOCK_STREAM` and `send()` method.

```
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))
client_socket.send("Hello, server!")
client_socket.close()
```

## TCP

`ConnectionRefusedError` is the exception type when the client code establishes a TCP connection to the server but
encounters an error during the connection process. A connection attempt is refused by the server.

## UDP

User Datagram Protocol

UDP uses a simple connectionless communication model. It doesn't establish a persistent connection between sever and 
receiver. Each datagram (packet) is sent independently and can take different paths through the network.

UDP doesn't involve handshaking dialogues for connection establishment or termination. UDP doesn't guarantee reliability,
ordering, or congestion control. UDP provides a lightweight, low-overhead communication mechanism without the overhead
of establishing and maintaining a connection.

UDP is often used for applications where **real-time** or **low-latency** communication is required.

## DNS

Use `dnslib` to perform domain name system resolution to resolve domain names into IP addresses, construct DNS packets,
parse DNS responses.
