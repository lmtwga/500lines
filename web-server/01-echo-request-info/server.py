import BaseHTTPServer

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    '''Respond to HTTP requests with info about the request.'''

    # Template for page to send back.
    Page = '''\
<html>
<body>
<h1>Nitinat/Python V1.0 Page</h1>
<table>
<tr>  <td>Date and time</td>  <td>%(date_time)s</td>   </tr>
<tr>  <td>Client host</td>    <td>%(client_host)s</td> </tr>
<tr>  <td>Client port</td>    <td>%(client_port)s</td> </tr>
<tr>  <td>Command</td>        <td>%(command)s</td>     </tr>
<tr>  <td>Path</td>           <td>%(path)s</td>        </tr>
</body>
</html>
'''

    # Handle a request by constructing an HTML page that echoes the
    # request back to the caller.
    def do_GET(self):
        page = self.create_page()
        self.send_page(page)

    # Create an information page to send.
    def create_page(self):
        values = {
            'date_time'   : self.date_time_string(),
            'client_host' : self.client_address[0],
            'client_port' : self.client_address[1],
            'command'     : self.command,
            'path'        : self.path
        }
        page = self.Page % values
        return page

    # Send the created page.
    def send_page(self, page):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(page)

#----------------------------------------------------------------------

if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
