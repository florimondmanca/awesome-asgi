# awesome-asgi

[![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

> A curated list of awesome ASGI servers, frameworks, apps, libraries, and other resources.

To contribute to this list, please read the [contribution guidelines](CONTRIBUTING.md).

**Contents**

- [Applications](#applications)
- [Application frameworks](#application-frameworks)
- [Libraries](#libraries)
- [Middleware](#middleware)
- [Publications](#publications)
- [Servers](#servers)

## Applications

_Applications that expose the ASGI interface._

## Application frameworks

_Frameworks for building ASGI web applications._

- [Bocadillo](https://bocadilloproject.github.io) - Fast, scalable and real-time capable web APIs for everyone. Powered by Starlette. Supports HTTP (incl. SSE) and WebSockets.
- [Channels](https://channels.readthedocs.io/en/latest/) - Asynchronous support for Django, and the original driving force behind the ASGI project. Supports HTTP and WebSockets with Django integration, and any protocol with ASGI-native code.
- [FastAPI](https://github.com/tiangolo/fastapi) - A modern, high-performance web framework for building APIs with Python 3.6+ based on standard Python type hints. Powered by Starlette and Pydantic. Supports HTTP and WebSockets.
- [Quart](https://github.com/pgjones/quart) - A Python ASGI web microframework whose API is a superset of the Flask API. Supports HTTP (incl. SSE and HTTP/2 server push) and WebSockets.
- [Responder](https://python-responder.org/en/latest/) - A familiar HTTP Service Framework for Python, powered by Starlette. (ASGI 2.0 only, ed.)
- [Starlette](https://www.starlette.io/) - Starlette is a lightweight ASGI framework/toolkit, which is ideal for building high performance asyncio services. Supports HTTP and WebSockets.

## Libraries

_Libraries for use in ASGI apps._

## Middleware

_General-purpose middleware to wrap around ASGI apps._

## Publications

_Articles, talks and other contents about ASGI._

## Servers

_ASGI web servers._

- [Daphne](http://github.com/django/daphne) - An HTTP, HTTP2 and WebSocket protocol server for ASGI, developed to power Django Channels.
- [Hypercorn](https://pgjones.gitlab.io/hypercorn/index.html) - An ASGI server based on the sans-io hyper, h11, h2, and wsproto libraries. Supports HTTP/1, HTTP/2, WebSockets, ASGI 2.0 and ASGI 3.0. Compatible with asyncio, uvloop and trio worker types.
- [Uvicorn](https://www.uvicorn.org/) - A fast ASGI server based on uvloop and httptools. Supports HTTP/1 and WebSockets.
