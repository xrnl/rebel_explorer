"""functions and decorators that encapsulate common functionality reusable with multiple test cases"""
from contextlib import contextmanager
from functools import wraps

from flask import template_rendered


@contextmanager
def record_request_information(app):
    """reusable try/finally to obtain the rendered template and context of the request
    after making a request to app
    """
    recorded = []

    def record(sender, template, context, **extra):
        """signals that registers the template and context when a request is made"""
        recorded.append((template, context))

    template_rendered.connect(record, app)  # connect and register all signals
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)  # disconnect from signal listening


def client_get_request(url):
    """decorator which makes requests to url and returns the
    response, loaded template and context to the test case which it decorates"""

    def decorator(test_method):
        @wraps(test_method)
        def wrapper(self):
            with record_request_information(self.app) as recorded:
                response = self.client.get(url, follow_redirects=True)  # make request
                template, context = recorded[0]  # extract data recorded in previous request
                test_method(self, response, template.name, context)  # pass all data to the test function

        return wrapper

    return decorator
