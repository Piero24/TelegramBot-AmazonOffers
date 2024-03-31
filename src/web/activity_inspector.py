# Copyright (C) by Pietrobon Andrea - All Rights Reserved
#
# This file is part of the project: TelegramBot-AmazonOffers
# It can only be distributed from Andrea Pietrobon's official Github profile
# The use of the project TelegramBot-AmazonOffers or of this file follow
# the rules indicated in the LICENSE file.
# The redistribution or sale of the files without the written consent 
# of the author is not authorized.
#
# Written by Pietrobon Andrea, Jan 2024
# Official website <https://pietrobonandrea.com>
# Github website <https://github.com/Piero24>

# Standard library modules
import logging
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

# Importing internal modules
from configs import settings
from utils.log_manager import setup_logger

# Setting up logger
setup_logger()
logger = logging.getLogger(__name__)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """Handles HTTP requests and serves files from the current directory.

    This class extends BaseHTTPRequestHandler and implements GET and HEAD 
    methods for serving files and handling HTTP requests.

    Methods:
        do_GET(self): Handles GET requests.
    """
    def do_GET(self) -> None:
        """Handles GET requests. Sets up the response status, header, 
            and sends HTML content with the response status.

        Args:
            self: The instance of the class handling the request.
        """
        # Set response status (200 OK)
        response_ok = 200
        
        # Check if the request is for CSS
        if self.path.endswith('.css'):
            content_type = 'text/css'
            # Construct the full path to the CSS file
            file_path = 'src/web/style.css'
        else:
            # For other requests, assume HTML
            content_type = 'text/html'
            file_path = 'src/web/index.html'
        
        try:
            with open(file_path, 'rb') as file:
                content = file.read()
        except FileNotFoundError:
            # If file not found, send a 404 response
            self.send_error(404, "File not found")
            return
        
        # Set response headers
        self.send_response(response_ok)
        self.send_header('Content-type', content_type)
        self.end_headers()
        
        # Converts the content to bytes and sends it as a response
        self.wfile.write(content)

def run_server() -> None:
    """Runs the web server. Starts the server on a specified IP 
        address and port. Prints server start-up messages.
    """
    logging.info('Start the server...')
    # Specifies the IP address and port on which the server will run
    server_address = ('', settings.PORT)
    # Create a web server instance
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    # Start the server
    logging.info(f'The server is running at localhost:{settings.PORT}.')
    httpd.serve_forever()

def run_server_thread() -> None:
    """Runs the web server in a separate thread. Creates a thread for 
        running the server and starts the thread.
    """
    # Create a thread for the server
    server_thread = threading.Thread(target=run_server)
    # Start the server thread
    server_thread.start()
