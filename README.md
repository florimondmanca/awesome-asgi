# awesome-asgi

[![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)
[![Versioning](https://img.shields.io/badge/calver-YY.M.MICRO-22bfda.svg)](https://calver.org)

> A curated list of awesome ASGI servers, frameworks, apps, libraries, and other resources.

This list should help you keep yourself up to date with the most awesome ASGI projects and resources. Watch releases on this repo to be notified about new entries. If you find anything missing, please [contribute](CONTRIBUTING.md). ❣️

[ASGI] is a standard interface positioned as a spiritual successor to WSGI. It enables communication and interoperability across the whole Python async web stack: servers, applications, middleware, and individual components.

Born in 2016 to power the Django Channels project, ASGI and its ecosystem have been expanding ever since, boosted by the arrival of projects such as Starlette and Uvicorn in 2018.

[asgi]: https://asgi.readthedocs.io

**Contents**

- [Applications](#applications)
- [Application frameworks](#application-frameworks)
- [Libraries](#libraries)
- [Middleware](#middleware)
- [Publications](#publications)
- [Servers](#servers)

## Applications

_Apps and projects that make use of the ASGI interface._

- [Datasette](https://github.com/simonw/datasette/) - A tool for exploring and publishing data, including ASGI-compatible components and plugins.

## Application frameworks

_Frameworks for building ASGI web applications._

- [Bocadillo](https://bocadilloproject.github.io) - Fast, scalable and real-time capable web APIs for everyone. Powered by Starlette. Supports HTTP (incl. SSE) and WebSockets.
- [Channels](https://channels.readthedocs.io/en/latest/) - Asynchronous support for Django, and the original driving force behind the ASGI project. Supports HTTP and WebSockets with Django integration, and any protocol with ASGI-native code.
- [FastAPI](https://github.com/tiangolo/fastapi) - A modern, high-performance web framework for building APIs with Python 3.6+ based on standard Python type hints. Powered by Starlette and Pydantic. Supports HTTP and WebSockets.
- [Quart](https://github.com/pgjones/quart) - A Python ASGI web microframework whose API is a superset of the Flask API. Supports HTTP (incl. SSE and HTTP/2 server push) and WebSockets.
- [Responder](https://python-responder.org/en/latest/) - A familiar HTTP Service Framework for Python, powered by Starlette. (ASGI 2.0 only, ed.)
- [Sanic](https://sanicframework.org/) - Sanic is a Python 3.6+ web server and web framework that's written to go fast. It allows the usage of the async/await syntax added in Python 3.5, which makes your code non-blocking and speedy. Supports HTTP and WebSockets.
- [Starlette](https://www.starlette.io/) - Starlette is a lightweight ASGI framework/toolkit, which is ideal for building high performance asyncio services. Supports HTTP and WebSockets.

## Libraries

_Libraries for use in ASGI apps._

- [Ariadne](https://github.com/mirumee/ariadne) - A Python library for implementing GraphQL servers.
- [asgiref](https://github.com/django/asgiref) - ASGI reference implementation, including function wrappers, server base classes and a WSGI-to-ASGI adapter.
- [Bonnette](https://github.com/erm/bonnette) - ASGI adapter for Azure Functions.
- [HTTPX](https://www.encode.io/httpx) - Next generation HTTP client, including async support and ability to call ASGI apps directly.
- [Mangum](https://github.com/erm/mangum) - AWS Lambda & API Gateway support for ASGI.
- [tartiflette-asgi](https://github.com/tartiflette/tartiflette-asgi) - ASGI support for the Tartiflette GraphQL engine.

## Middleware

_General-purpose middleware to wrap around ASGI apps._

- [datasette-auth-github](https://github.com/simonw/datasette-auth-github) - GitHub OAuth authentication for ASGI apps. Supports restricting to specific users or member of specific teams or organizations.
- [ProxyHeadersMiddleware](https://github.com/encode/uvicorn/blob/master/uvicorn/middleware/proxy_headers.py) - Use `X-Forwarded-Proto` and `X-Forwarded-For` headers set by a known and trusted proxy to make `client` and `scheme` reference the connecting client (shipped with Uvicorn).
- [Sentry ASGI](https://docs.sentry.io/platforms/python/asgi/) - Sentry integration for ASGI frameworks (part of `sentry-sdk`).
- [Starlette middleware](https://www.starlette.io/middleware) - Middleware for CORS, HTTPS redirection, GZip compression, and more (shipped with Starlette).
- [timing-asgi](https://github.com/steinnes/timing-asgi) - ASGI middleware to record and emit timing metrics.

## Publications

_Articles, talks and other contents about ASGI._

<!-- Please use anti-chronological order of publication. If date of publication is unknown, place at the bottom. -->

Articles:

- 2019-03-20 - [ASGI 3.0](https://www.aeracode.org/2019/03/20/asgi-30/), Andrew Godwin.
- 2018-06-22 - [Writing an ASGI web framework](https://yoongkang.com/blog/writing-an-asgi-web-framework/), Yoong Kang Lim.
- 2018-06-17 - [Embracing ASGI with Quart; Introducing Hypercorn](https://medium.com/@pgjones/embracing-asgi-with-quart-introducing-hypercorn-652cb6b269f5), Philip Jones.
- _Undated_ - [Hello ASGI](https://www.encode.io/articles/hello-asgi/), Tom Christie.
- _Undated_ - [Working with ASGI and HTTP](https://www.encode.io/articles/asgi-http/), Tom Christie.

Talks:

- 2019-06-15 - [An introduction to ASGI, Asynchronous Server Gateway Interface](https://www.youtube.com/watch?v=t3gCK9QqXWU), P G Jones, PyLondinium 2019.
- 2019-04-12 - [Sketching out A Django redesign](https://www.youtube.com/watch?v=u8GSFEg5lnU), Tom Christie, DjangoCon Europe.
- 2018-05 - [Taking Django Async](https://www.youtube.com/watch?v=-7taKQnndfo), Andrew Godwin, PyCon.

## Servers

_Web servers for ASGI applications._

- [Daphne](http://github.com/django/daphne) - An HTTP, HTTP2 and WebSocket protocol server for ASGI, developed to power Django Channels.
- [Hypercorn](https://pgjones.gitlab.io/hypercorn/index.html) - An ASGI server based on the sans-io hyper, h11, h2, and wsproto libraries. Supports HTTP/1, HTTP/2, WebSockets, ASGI 2.0 and ASGI 3.0. Compatible with asyncio, uvloop and trio worker types.
- [Uvicorn](https://www.uvicorn.org/) - A fast ASGI server based on uvloop and httptools. Supports HTTP/1 and WebSockets.
