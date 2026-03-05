r = requests.get(tarball_url, stream=True)

    # The response body is not downloaded until you access r.content
    print(r.content)
    # This will download the response body from the server
    # and return it as a bytes object

    # If you want to save it to a file, do this:
    with open('data.tar.gz', 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)

    # Or save it directly to a file in one line:
    with requests.get(tarball_url, stream=True) as r:
        with open('data.tar.gz', 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)

.. warning:: This means the response body is not downloaded until you access
   the :attr:`Response.content <requests.Response.content>` attribute. This can
   result in memory issues if you're trying to download large files.

.. _timeout:

Timeouts
--------

You can tell Requests to stop waiting for a response after a given number of
seconds with the ``timeout`` parameter. Nearly all production code should use
this parameter in nearly all requests. Failure to do so can cause your program
to hang indefinitely::

    >>> requests.get('https://github.com/', timeout=0.001)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    requests.exceptions.Timeout: HTTPConnectionPool(host='github.com', port=80): Request timed out. (timeout=0.001)

.. admonition:: Note

    ``timeout`` is not a time limit on the entire response download;
    rather, an exception is raised if the server has not issued a
    response for ``timeout`` seconds (more precisely, if no bytes have been
    received on the underlying socket for ``timeout`` seconds). If no timeout is specified explicitly, requests do
    not time out.

.. _proxies:

Proxies
-------

You can use proxies to send requests through an intermediate server. A proxy can
be used to hide your real IP address, or to route requests through a specific
network.

Proxies are specified using a dictionary, where the key is the scheme (``http`` or
``https``) and the value is the proxy URL. The proxy URL must contain a scheme
(``http://`` or ``https://``) as well.

For example, to send a request through an HTTP proxy::

    proxies = {
        'http': 'http://10.10.1.10:3128',
        'https': 'http://10.10.1.10:1080',
    }

    r = requests.get('https://github.com', proxies=proxies)

Note: The scheme for a proxy URL is now required in Requests 2.x.

.. warning:: When using proxies, you must ensure that your proxy supports
   both HTTP and HTTPS. If your proxy doesn't support HTTPS, then you'll get
   an error when trying to use it for HTTPS requests.

.. _cookies:

Cookies
-------

Requests can be used to send cookies to the server and receive cookies from
the server. This allows you to maintain state across multiple requests.

For example, to send a cookie to the server::

    r = requests.get('https://httpbin.org/cookies', cookies={'mycookie': 'value'})

To receive cookies from the server::

    r = requests.get('https://httpbin.org/cookies')
    print(r.cookies['mycookie'])

.. warning:: If you're using a Session object, cookies will be persisted across
   requests. If you're using a regular request object, cookies will only be
   sent with that request.

.. _auth:

Authentication
--------------

Requests supports several forms of authentication, including basic auth,
digest auth, and OAuth 1. You can find more information in the
:ref:`authentication <authentication>` section.

.. _headers:

Custom Headers
--------------

If you'd like to add HTTP headers to a request, simply pass in a ``dict`` to the
``headers`` parameter.

For example, we didn't specify our user-agent in the previous example::

    >>> url = 'https://api.github.com/some/endpoint'
    >>> headers = {'user-agent': 'my-app/0.0.1'}

    >>> r = requests.get(url, headers=headers)

Note: Custom headers are given less precedence than more specific sources of information. For instance:

* Authorization headers set with `headers=` will be overridden if credentials
  are specified in ``.netrc``, which in turn will be overridden by the  ``auth=``
  parameter. Requests will search for the netrc file at `~/.netrc`, `~/_netrc`,
  or at the path specified by the `NETRC` environment variable.
  Check details in :ref:`netrc authentication <authentication>`.
* Authorization headers will be removed if you get redirected off-host.
* Proxy-Authorization headers will be overridden by proxy credentials provided in the URL.
* Content-Length headers will be overridden when we can determine the length of the content.

Furthermore, Requests does not change its behavior at all based on which custom headers are specified. The headers are simply passed on into the final request.

Note: All header values must be a ``string``, bytestring, or unicode. While permitted, it's advised to avoid passing unicode header values.

.. _redirects:

Redirection and History
-----------------------

By default Requests will perform location redirection for all verbs except
HEAD.

We can use the ``history`` property of the Response object to track redirection.

The :attr:`Response.history <requests.Response.history>` list contains the
:class:`Response <requests.Response>` objects that were created in order to
complete the request. The list is sorted from the oldest to the most recent
response.

For example, GitHub redirects all HTTP requests to HTTPS::

    >>> r = requests.get('http://github.com/')

    >>> r.url
    'https://github.com/'

    >>> r.status_code
    200

    >>> r.history
    [<Response [301]>]

If you're using GET, OPTIONS, POST, PUT, PATCH or DELETE, you can disable
redirection handling with the ``allow_redirects`` parameter::

    >>> r = requests.get('http://github.com/', allow_redirects=False)

    >>> r.status_code
    301

    >>> r.history
    []

If you're using HEAD, you can enable redirection as well::

    >>> r = requests.head('http://github.com/', allow_redirects=True)

    >>> r.url
    'https://github.com/'

    >>> r.history
    [<Response [301]>]

.. _mismatched-urls:

Mismatched URLs
---------------

If you have a URL that doesn't match the expected pattern, Requests will raise
an exception. This is to prevent requests from being made to the wrong URL.

For example, if you have a URL that ends with a trailing slash, Requests will
raise an exception if you try to access it without a trailing slash::

    >>> requests.get('https://github.com/')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "requests/api.py", line 75, in get
        raise ValueError('URL must end with a slash if it contains a trailing slash')
    ValueError: URL must end with a slash if it contains a trailing slash

.. _certs:

Certificates
------------

Requests can be used to send and receive certificates from a server. This is
useful for setting up secure communication between two systems.

To send a certificate to the server, you can use the ``cert`` parameter::

    r = requests.get('https://kennethreitz.org', cert=('/path/client.cert', '/path/client.key'))

To receive a certificate from the server, you can use the ``verify`` parameter::

    r = requests.get('https://kennethreitz.org', verify='/path/to/certfile')

.. _custom-hooks:

Custom Hooks
------------

Requests supports custom hooks for various events in the request lifecycle.
These hooks can be used to modify the request or response object at various
points in the request lifecycle.

For example, you can use a hook to modify the headers of a request::

    def modify_headers(request, *args, **kwargs):
        request.headers['X-My-Header'] = 'value'
        return request

    r = requests.get('https://httpbin.org/headers', hooks={'request': modify_headers})

You can also use a hook to modify the response object::

    def modify_response(response, *args, **kwargs):
        response.headers['X-My-Header'] = 'value'
        return response

    r = requests.get('https://httpbin.org/headers', hooks={'response': modify_response})

You can also use a hook to modify the request or response object at various
points in the request lifecycle.

For example, you can use a hook to modify the headers of a request::

    def modify_headers(request, *args, **kwargs):
        request.headers['X-My-Header'] = 'value'
        return request

    r = requests.get('https://httpbin.org/headers', hooks={'request': modify_headers})

You can also use a hook to modify the response object::

    def modify_response(response, *args, **kwargs):
        response.headers['X-My-Header'] = 'value'
        return response

    r = requests.get('https://httpbin.org/headers', hooks={'response': modify_response})

You can also use a hook to modify the request or response object at various
points in the request lifecycle.

For example, you can use a hook to modify the headers of a request::

    def modify_headers(request, *args, **kwargs):
        request.headers['X-My-Header'] = 'value'
        return request

    r = requests.get('https://httpbin.org/headers', hooks={'request': modify_headers})

You can also use a hook to modify the response object::

    def modify_response(response, *args, **kwargs):
        response.headers['X-My-Header'] = 'value'
        return response

    r = requests.get('https://httpbin.org/headers', hooks={'response': modify_response})

You can also use a hook to modify the request or response object at various
points in the request lifecycle.

For example, you can use a hook to modify the headers of a request::

    def modify_headers(request, *args, **kwargs):
        request.headers['X-My-Header'] = 'value'
        return request

    r = requests.get('https://httpbin.org/headers', hooks={'request': modify_headers})

You can also use a hook to modify the response object::

    def modify_response(response, *args, **kwargs):
        response.headers['X-My-Header'] = 'value'
        return response

    r = requests.get('https://httpbin.org/headers', hooks={'response': modify_response})

You can also use a hook to modify the request or response object at various
points in the request lifecycle.

For example, you can use a hook to modify the headers of a request::

    def modify_headers(request, *args, **kwargs):
        request.headers['X-My-Header'] = 'value'
        return request

    r = requests.get('https://httpbin.org/headers', hooks={'request': modify_headers})

You can also use a hook to modify the response object::

    def modify_response(response, *args, **kwargs):
        response.headers['X-My-Header'] = 'value'
        return response

    r = requests.get('https://httpbin.org/headers', hooks={'response': modify_response})

You can also use a hook to modify the request or response object at various
points in the request lifecycle.

For example, you can use a hook to modify the headers of a request::

    def modify_headers(request, *args, **kwargs):
        request.headers['X-My-Header'] = 'value'
        return request

    r = requests.get('https://httpbin.org/headers', hooks={'request': modify_headers})

You can also use a hook to modify the response object::

    def modify_response(response, *args, **kwargs):
        response.headers['X-My-Header'] = 'value'
        return response

    r = requests.get('https://httpbin.org/headers', hooks={'response': modify_response})

You can also use a hook to modify the request or response object at various
points in the request lifecycle.

For example, you can use a hook to modify the headers of a request::

    def modify_headers(request, *args, **kwargs):
        request.headers['X-My-Header'] = 'value'
        return request

    r = requests.get('https://httpbin.org/headers', hooks={'request': modify_headers})

You can also use a hook to modify the response object::

    def modify_response(response, *args, **kwargs):
        response.headers['X-My-Header'] = 'value'
        return response

    r = requests.get('https://httpbin.org/headers', hooks={'response': modify_response})

You can also use a hook to modify the request or response object at various
points in the request lifecycle.

For example, you can use a hook to modify the headers of a request::

    def modify_headers(request, *args, **kwargs):
        request.headers['X-My-Header'] = 'value'
        return request

    r = requests.get('https://httpbin.org/headers', hooks={'request': modify_headers})

You can also use a hook to modify the response object::

    def modify_response(response, *args, **kwargs):
        response.headers['X-My-Header'] = 'value'
        return response

    r = requests.get('https://httpbin.org/headers', hooks={'response': modify_response})

You can also use a hook to modify the request or response object at various
points in the request lifecycle.

For example, you can use a hook to modify the headers of a request::

    def modify_headers(request, *args, **kwargs):
        request.headers['X-My-Header'] = 'value'
        return request

    r = requests.get('https://httpbin.org/headers', hooks={'request': modify_headers})

You can also use a hook to modify the response object::

    def modify_response(response, *args, **kwargs):
        response.headers['X-My-Header'] = 'value'
        return response

    r = requests.get('https://httpbin.org/headers', hooks={'response': modify_response})

You can also use a hook to modify the request or response object at various
points in the request lifecycle.

For example, you can use a hook to modify the headers of a request::

    def modify_headers(request, *args, **kwargs):
        request.headers['X-My-Header'] = 'value'
        return request

    r = requests.get('https://httpbin.org/headers', hooks={'request': modify_headers})

You can also use a hook to modify the response object::

    def modify_response(response, *args, **kwargs):
        response.headers['X-My-Header'] = 'value'
        return response

    r = requests.get('https://httpbin.org/headers', hooks={'response': modify_response})

You can also use a hook to modify the request or response object at various
points in the request lifecycle.

For example, you can use a hook to modify the headers of a request::

    def modify_headers(request, *args, **kwargs):
        request.headers['X-My-Header'] = 'value'
        return request

    r = requests.get('https://httpbin.org/headers', hooks={'request': modify_headers})

You can also use a hook to modify the response object::

    def modify_response(response, *args, **kwargs):
        response.headers['X-My-Header'] = 'value'
        return response

    r = requests.get('https://httpbin.org/headers', hooks={'response': modify_response})

You can also use a hook to modify the request or response object at various
points in the request lifecycle.

For example, you can use a hook to modify the headers of a request::

    def modify_headers(request, *args, **kwargs):
        request.headers['X-My-Header'] = 'value'
        return request

    r = requests.get('https://httpbin.org/headers', hooks={'request': modify_headers})

You can also use a hook to modify the response object::

    def modify_response(response, *args, **kwargs):
        response.headers['X-My-Header'] = 'value'
        return response

    r = requests.get('https://httpbin.org/headers', hooks={'response': modify_response})

You can also use a hook to modify the request or response object at various
points in the request lifecycle.

For example, you can use a hook to modify the headers of a request::

    def modify_headers(request, *args, **kwargs):
        request.headers['X-My-Header'] = 'value'
        return request

    r = requests.get('https://httpbin.org/headers', hooks={'request': modify_headers})

You can also use a hook to modify the response object::

    def modify_response(response, *args, **kwargs):
        response.headers['X-My-Header'] = 'value'
        return response

    r = requests.get('https://httpbin.org/headers', hooks={'response': modify_response})

You can also use a hook to modify the request or response object at various
points in the request lifecycle.

For example, you can use a hook to modify the headers of a request::

    def modify_headers(request, *args, **kwargs):
        request.headers['X-My-Header'] = 'value'
        return request

    r = requests.get('https://httpbin.org/headers', hooks={'request': modify_headers})

You can also use a hook to modify the response object::

    def modify_response(response, *args, **kwargs):
        response.headers['X-My-Header'] = 'value'
        return response

    r = requests.get('https://httpbin.org/headers', hooks={'response': modify_response})

You can also use a hook to modify the request or response object at various
points in the request lifecycle.

For example, you can use a hook to modify the headers of a request::

    def modify_headers(request, *args, **kwargs):
        request.headers['X-My-Header'] = 'value'
        return request

    r = requests.get('https://httpbin.org/headers', hooks={'request': modify_headers})

You can also use a hook to modify the response object::

    def modify_response(response, *args, **kwargs):
        response.headers['X-My-Header'] = 'value'
        return response

    r = requests.get('https://httpbin.org/headers', hooks={'response': modify_response})

You can also use a hook to modify the request or response object at various
points in the request lifecycle.

For example, you can use a hook to modify the headers of a request::

    def modify_headers(request, *args, **kwargs):
        request.headers['X-My-Header'] = 'value'
        return request

    r = requests.get('https://httpbin.org/headers', hooks={'request': modify_headers})

You can also use a hook to modify the response object::

    def modify_response(response, *args, **kwargs):
        response.headers['X-My-Header'] = 'value'
        return response

    r = requests.get('https://httpbin.org/headers', hooks={'response': modify_response})

You can also use a hook to modify the request or response object at various
points in the request lifecycle.

For example, you can use a hook to modify the headers of a request::

    def modify_headers(request, *args, **kwargs):
        request.headers['X-My-Header'] = 'value'
        return request

    r = requests.get('https://httpbin.org/headers', hooks={'request': modify_headers})

You can also use a hook to modify the response object::

    def modify_response(response, *args, **kwargs):
        response.headers['X-My-Header'] = 'value'
        return response

    r = requests.get('https://httpbin.org/headers', hooks={'response': modify_response})

You can also use a hook to modify the request or response object at various
points in the request lifecycle.

For example, you can use a hook to modify the headers of a request::

    def modify_headers(request, *args, **kwargs):
        request.headers['X-My-Header'] = 'value'
        return request

    r = requests.get('https://httpbin.org/headers', hooks={'request': modify_headers})

You can also use a hook to modify the response object::

    def modify_response(response, *args, **kwargs):
        response.headers['X-My-Header'] = 'value'
        return response

    r = requests.get('https://httpbin.org/headers', hooks={'response': modify_response})

You can also use a hook to modify the request or response object at various
points in the request lifecycle.

For example, you can use a hook to modify the headers of a request::

    def modify_headers(request, *args, **kwargs):
        request.headers['X-My-Header'] = 'value'
        return request

    r = requests.get('https://httpbin.org/headers', hooks={'request': modify_headers})

You can also use a hook to modify the response object::

    def modify_response(response, *args, **kwargs):
        response.headers['X-My-Header'] = 'value'
        return response

    r = requests.get('https://httpbin.org/headers', hooks={'response': modify_response})

You can also use a hook to modify the request or response object at various
points in the request lifecycle.

For example, you can use a hook to modify the headers of a request::

    def modify_headers(request, *args, **kwargs):
        request.headers['X-My-Header'] = 'value'
        return request

    r = requests.get('https://httpbin.org/headers', hooks={'request': modify_headers})

You can also use a hook to modify the response object::

    def modify_response(response, *args, **kwargs):
        response.headers['X-My-Header'] = 'value'
        return response

    r = requests.get('https://httpbin.org/headers', hooks={'response': modify_response})

You can also use a hook to modify the request or response object at various
points in the request lifecycle.

For example, you can use a hook to modify the headers of a request::

    def modify_headers(request, *args, **kwargs):
        request.headers['X-My-Header'] = 'value'
        return request

    r = requests.get('https://httpbin.org/headers', hooks={'request': modify_headers})

You can also use a hook to modify the response object::

    def modify_response(response, *args, **kwargs):
        response.headers['X-My-Header'] = 'value'
        return response

    r = requests.get('https://httpbin.org/headers', hooks={'response': modify_response})

You can also use a hook to modify the request or response object at various
points in the request lifecycle.

For example, you can use a hook to modify the headers of a request::

    def modify_headers(request, *args, **kwargs):
        request.headers['X-My-Header'] = 'value'
        return request

    r = requests.get('https://httpbin.org/headers', hooks={'