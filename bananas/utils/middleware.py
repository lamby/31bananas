from django.middleware import transaction

class TransactionMiddleware(transaction.TransactionMiddleware):
    """
    Like Django's ``django.middleware.transaction.TransactionMiddleware`` but
    only activates if the following conditions are true:

        * HTTP request method is not GET or HEAD.
    """

    def process_request(self, request):
        if request.method in ('GET', 'HEAD'):
            return

        super(TransactionMiddleware, self).process_request(request)

    def process_exception(self, request, exception):
        if request.method in ('GET', 'HEAD'):
            return

        super(TransactionMiddleware, self).process_exception(request, exception)

    def process_response(self, request, response):
        if request.method in ('GET', 'HEAD'):
            return response

        super(TransactionMiddleware, self).process_response(request, response)

        return response
