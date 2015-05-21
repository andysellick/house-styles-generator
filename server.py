import http.server
import socketserver
import logging
import cgi
import os
import shutil
from config import *

PORT = 8000
OUTPUT = os.path.dirname(os.path.realpath(__file__)) + '/output/' #set the output directory

corefiles = ''
extrafiles = ''
optionfiles = ''

#first empty the outputs folder
def cleanOutput():
    for the_file in os.listdir(OUTPUT):
        file_path = os.path.join(OUTPUT, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path,ignore_errors=True)
        except (Exception, e):
            print(e)

responsive = 0 #option to select responsive styles if available

#create all the checkbox options
for x in range(len(files)):
    if files[x]['type'] == 'core':
        corefiles += '<div class="field"><label><input type="checkbox" name="lessfile-' + files[x]['id'] + '" checked="checked"/>' + files[x]['name'] + '</label></div>'
    if files[x]['type'] == 'extra':
        extrafiles += '<div class="field"><label><input type="checkbox" name="lessfile-' + files[x]['id'] + '"/>' + files[x]['name'] + '</label></div>'
    if files[x]['type'] == 'optional':
        optionfiles += '<div class="field"><label><input type="checkbox" name="lessfile-' + files[x]['id'] + '"/>' + files[x]['name'] + '</label></div>'
    if 'responsive' in files[x]:
        responsive = 1

# high level structure based on https://snipt.net/raw/f8ef141069c3e7ac7e0134c6b58c25bf/?nice
class ServerHandler(http.server.SimpleHTTPRequestHandler):

    #display the initial form
    def do_GET(self):
        if self.path == '/': #override the response for the root
            cleanOutput()
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()

            f = open('www/index.html', 'r')
            html = f.read()
            html = html.replace("<!-- COREFILES -->",corefiles)
            html = html.replace("<!-- EXTRAFILES -->",extrafiles)
            html = html.replace("<!-- OPTIONFILES -->",optionfiles)
            if responsive:
                html = html.replace("<!-- RESPONSIVE -->",'<label><input type="checkbox" name="responsive-styles"/>Include responsive styles where available</label>')
            self.wfile.write(bytes(html, 'UTF-8'))
        else: #need to include this so paths other than '/' work e.g. stylesheets
            #logging.warning(self.path)
            http.server.SimpleHTTPRequestHandler.do_GET(self)

    #handle the form once submitted
    def do_POST(self):
        #set up new dir structure
        if not os.path.exists(OUTPUT + dircss):
            os.makedirs(OUTPUT + dircss)
        if not os.path.exists(OUTPUT + dirless):
            os.makedirs(OUTPUT + dirless)
        if not os.path.exists(OUTPUT + dirjs):
            os.makedirs(OUTPUT + dirjs)

        #handle data
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })

        lessfilecontents = ''
        responsivelessfilecontents = ''
        includeresponsive = 0

        for key in form.keys():
            if 'responsive-styles' in str(key):
                includeresponsive = 1

        for key in form.keys():
            #logging.warning(key)
            #logging.warning(form[key].value)

            #process all the less file checkboxes
            if 'lessfile-' in str(key):
                for x in range(len(files)):
                    thiskey = str(key).replace('lessfile-','')
                    if files[x]['id'] == thiskey:
                        #logging.warning('found: ' + files[x]['name'])
                        shutil.copy2(sourcedir + dirless + files[x]['less'], OUTPUT + dirless + files[x]['less'])
                        lessfilecontents += '@import "' + files[x]['less'] + '";\n' #add this less file to the main less file
                        if includeresponsive and 'responsive' in files[x]:
                            shutil.copy2(sourcedir + dirless + files[x]['responsive'], OUTPUT + dirless + files[x]['responsive'])
                            responsivelessfilecontents += '@import "' + files[x]['responsive'] + '";\n'



        if len(lessfilecontents):
            #write the main less file
            f = open(OUTPUT + dirless + lessfile,'w')
            f.write(lessfilecontents)

        if includeresponsive:
            #write the responsive less file
            r = open(OUTPUT + dirless + responsivelessfile,'w')
            r.write(responsivelessfilecontents)


        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        f = open('www/success.html', 'r')
        html = f.read()
        self.wfile.write(bytes(html, 'UTF-8'))
        #http.server.SimpleHTTPRequestHandler.do_GET(self)


#Handler = http.server.SimpleHTTPRequestHandler
Handler = ServerHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()

