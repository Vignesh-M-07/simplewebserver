from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <title>Top Software Industries</title>
    <body>
        <table border="2" cellspacing="10" cellpadding="6">
            <caption>Top 5 Revenue Generating Software Companies</caption>
            <tr>
                <th>s.no</th>
                <th>companies</th>
                <th>Revenue</th>
            </tr>
            <tr>
                <th>1</th>
                <th>Google</th>
                <th>65 billion</th>
            </tr>
            <tr>
                <th>2</th>
                <th>oracle</th>
                <th>30 billion</th>
            </tr>
            <tr>
                <th>3</th>
                <th>IBM</th>
                <th>29.1 billion</th>
            </tr>
            <tr>
                <th>4</th>
                <th>SAP</th>
                <th>10 billion</th>
            </tr>
            <tr>
                <th>5</th>
                <th>symentec</th>
                <th>20 billion</th>
            </tr>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()        
