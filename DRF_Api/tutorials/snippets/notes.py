"""

Requests and Responses
-> Requests objects
   Rest framework introduces a Request object that extends the regular
   HttpReqest, and provides more flexible request parsing. The core functionality
   of the Request object is the request.data attribute, which is similar to request.POST,
   but more useful for working with WebAPIs

   request.POST # only handles form data. only works for 'POST' methods.
   request.data # Handles arbitrary data. Works for 'POST', 'PUT' and 'PATCH' methods.


-> Response objects
   Rest framework also introduces a Response object, which is a type of
   TemplateResponse that takes unrendered content and uses content negotiation to
   determine the correct content type to return to the client

-> Status codes
   REST framework provides more explicit identifiers for each status code

-> Wrapping API views
   REST framewor provides two wrappers you can use to write API views
   1.) @api_view decorator for working with function based views
   2.) APIView class for working with class-based views

   These wrappers provide a few bits of functionality such as making sure you recieve `Request`
   instances in your view, and adding context to Response objects so that content
   negotiation can be performed
   They also provide behavior such as returning `405 Method Not Allowed` responses when appropriate
   and handling any `ParseError` exceptions that occur when accessing `request.data` with malformed input

   
"""