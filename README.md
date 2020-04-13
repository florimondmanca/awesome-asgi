# awesome-asgi

[![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)
[![Versioning](https://img.shields.io/badge/calver-YY.M.MICRO-22bfda.svg)](https://calver.org)

> A curated list of awesome ASGI servers, frameworks, apps, libraries, and other resources.

This list should help you keep yourself up to date with the most awesome ASGI projects and resources. You can **watch releases** on this repo to be notified about new entries. If you find anything missing, please [contribute](CONTRIBUTING.md). ❣️

[ASGI] is a standard interface positioned as a spiritual successor to WSGI. It enables communication and interoperability across the whole Python async web stack: servers, applications, middleware, and individual components.

Born in 2016 to power the Django Channels project, ASGI and its ecosystem have been expanding ever since, boosted by the arrival of projects such as Starlette and Uvicorn in 2018.

[asgi]: https://asgi.readthedocs.io

**Contents**

- [Application frameworks](#application-frameworks)
- [Authentication](#authentication)
- [End-user applications](#end-user-applications)
- [GraphQL](#graphql)
- [Monitoring](#monitoring)
- [Proxies](#proxies)
- [Real-time web](#real-time-web)
- [Resources](#resources)
  - [Reference](#reference)
  - [Talks](#publications)
  - [Tutorials](#tutorials)
- [Security](#security)
- [Serialization](#serialization)
- [Serverless](#serverless)
- [Servers](#servers)
- [Testing](#testing)

## Application frameworks

_Frameworks for building ASGI web applications._

- [Channels](https://channels.readthedocs.io/en/latest/) - Asynchronous support for Django, and the original driving force behind the ASGI project. Supports HTTP and WebSockets with Django integration, and any protocol with ASGI-native code.
- [FastAPI](https://github.com/tiangolo/fastapi) - A modern, high-performance web framework for building APIs with Python 3.6+ based on standard Python type hints. Powered by Starlette and Pydantic. Supports HTTP and WebSockets.
- [Quart](https://github.com/pgjones/quart) - A Python ASGI web microframework whose API is a superset of the Flask API. Supports HTTP (incl. SSE and HTTP/2 server push) and WebSockets.
- [Responder](https://responder.readthedocs.io/en/latest/) - A familiar HTTP Service Framework for Python, powered by Starlette.
- [Sanic](https://sanicframework.org/) - Sanic is a Python 3.6+ web server and web framework that's written to go fast. It allows the usage of the async/await syntax added in Python 3.5, which makes your code non-blocking and speedy. Supports HTTP and WebSockets.
- [Starlette](https://www.starlette.io/) - Starlette is a lightweight ASGI framework/toolkit, which is ideal for building high performance asyncio services. Supports HTTP and WebSockets.

## Authentication

_Packages for adding authentication and managing users in ASGI web applications._

- [datasette-auth-github](https://github.com/simonw/datasette-auth-github) - GitHub OAuth authentication for ASGI apps. Supports restricting to specific users or member of specific teams or organizations.

## End-user applications

_Real-world applications that run on ASGI._

- [Datasette](https://github.com/simonw/datasette/) - A tool for exploring and publishing data, including ASGI-compatible components and plugins.

## GraphQL

_Packages for building GraphQL APIs via ASGI._

- [Ariadne](https://github.com/mirumee/ariadne) - A Python library for implementing GraphQL servers.
- [tartiflette-asgi](https://github.com/tartiflette/tartiflette-asgi) - ASGI support for the Tartiflette GraphQL engine.

## Monitoring

_Packages for monitoring ASGI web applications._

- [Scout APM Starlette](https://docs.scoutapm.com/#starlette) - Scout APM integration with Starlette and Starlette-based frameworks. (Shipped with `scout-apm`.)
- [Sentry ASGI](https://docs.sentry.io/platforms/python/asgi/) - Sentry integration for ASGI frameworks. (Shipped with `sentry-sdk`.)
- [timing-asgi](https://github.com/steinnes/timing-asgi) - ASGI middleware to record and emit timing metrics.

## Proxies

_Packages for use when running ASGI web applications behind proxies._

- [ProxyHeadersMiddleware](https://github.com/encode/uvicorn/blob/master/uvicorn/middleware/proxy_headers.py) - Use `X-Forwarded-Proto` and `X-Forwarded-For` headers set by a known and trusted proxy to make `client` and `scheme` reference the connecting client (shipped with Uvicorn).

## Real-time web

_Packages for use when building real-time-capable ASGI web applications._

- [python-socketio](https://python-socketio.readthedocs.io) - WebSocket clients and servers using Socket.IO. Includes an ASGI application wrapper.

## Resources

_Content about ASGI itself: concepts, history, usage, etc._

### Publications

_Articles, blog posts and other publications about ASGI._

- 2019-08-11 - [Introduction to ASGI: Emergence of an Async Python Web Ecosystem](https://florimond.dev/blog/articles/2019/08/introduction-to-asgi-async-python-web/) - Florimond Manca.
- 2019-03-20 - [ASGI 3.0](https://www.aeracode.org/2019/03/20/asgi-30/), Andrew Godwin.
- 2018-06-17 - [Embracing ASGI with Quart; Introducing Hypercorn](https://medium.com/@pgjones/embracing-asgi-with-quart-introducing-hypercorn-652cb6b269f5), Philip Jones.
- _Undated_ - [Hello ASGI](https://www.encode.io/articles/hello-asgi), Tom Christie.

### Reference

_Reference documentation and implementation for ASGI._

- [ASGI Documentation](https://asgi.readthedocs.io) - Documentation site for the ASGI specification.
- [asgiref](https://github.com/django/asgiref) - ASGI reference implementation, including function wrappers, server base classes and a WSGI-to-ASGI adapter.

### Talks

_Talks about ASGI._

- 2019-06-15 - [An introduction to ASGI, Asynchronous Server Gateway Interface](https://www.youtube.com/watch?v=t3gCK9QqXWU), P G Jones, PyLondinium 2019.
- 2019-04-12 - [Sketching out A Django redesign](https://www.youtube.com/watch?v=u8GSFEg5lnU), Tom Christie, DjangoCon Europe.
- 2018-07-27 - [Quart; an ASGI alternative to Flask](https://www.youtube.com/watch?v=t8-Y7Kivuu0), P G Jones, EuroPython 2018.
- 2018-05 - [Taking Django Async](https://www.youtube.com/watch?v=-7taKQnndfo), Andrew Godwin, PyCon.
- 2017-11 - [Future Pythonic Web: ASGI & Daphne](https://www.youtube.com/watch?v=6xEKPsKBbD0), Dmitry Nazarov, PiterPy.

### Tutorials

_Tutorials about working with ASGI applications and components._

- 2019-08-26 - [Quick and dirty mock service with Starlette](https://www.mattlayman.com/blog/2019/starlette-mock-service/), Matt Layman.
- 2018-06-22 - [Writing an ASGI web framework](https://yoongkang.com/blog/writing-an-asgi-web-framework/), Yoong Kang Lim.
- _Undated_ - [Working with ASGI and HTTP](https://www.encode.io/articles/asgi-http), Tom Christie.

## Security

_Packages and components for managing the security of ASGI web applications._

- [CORSMiddleware](https://www.starlette.io/middleware/#corsmiddleware) - Allow cross-origin requests from browsers. (Shipped with Starlette.)
- [HTTPSRedirectMiddleware](https://www.starlette.io/middleware/#httpsredirectmiddleware) - Redirect HTTP/WS traffic to HTTPS/WSS. (Shipped with Starlette.)
- [TrustedHostMiddleware](https://www.starlette.io/middleware/#trustedhostmiddleware) - Guard against host header attacks by validating the `Host` header of requests. (Shipped with Starlette.)

## Serialization

_Packages and components for converting the format of data in and out of ASGI web applications._

- [GZipMiddleware](https://www.starlette.io/middleware/#gzipmiddleware) - Response content compression using GZip. (Shipped with Starlette.)
- [msgpack-asgi](https://github.com/florimondmanca/msgpack-asgi) - Drop-in MessagePack support for ASGI apps and frameworks.

## Serverless

_Packages for building serverless web applications with ASGI._

- [Mangum](https://github.com/erm/mangum) - AWS Lambda & API Gateway support for ASGI.

## Servers

_Web servers for ASGI applications._

- [Daphne](http://github.com/django/daphne) - An HTTP, HTTP2 and WebSocket protocol server for ASGI, developed to power Django Channels.
- [Hypercorn](https://pgjones.gitlab.io/hypercorn/index.html) - An ASGI server based on the sans-io hyper, h11, h2, and wsproto libraries. Supports HTTP/1, HTTP/2, WebSockets, ASGI 2.0 and ASGI 3.0. Compatible with asyncio, uvloop and trio worker types.
- [Uvicorn](https://www.uvicorn.org/) - A fast ASGI server based on uvloop and httptools. Supports HTTP/1 and WebSockets.

## Testing

_Packages for testing ASGI applications._

- [async-asgi-testclient](https://github.com/vinissimus/async-asgi-testclient) - A framework-agnostic library for testing ASGI web applications.
- [HTTPX](https://www.encode.io/httpx) - Next generation HTTP client, including async support and ability to call ASGI apps directly.
