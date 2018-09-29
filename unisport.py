#!/usr/bin/python

import mechanize
import cookielib
import ConfigParser
import sys
from os.path import expanduser

def init():
    global homedir
    homedir = expanduser("~")

    global configFilePath, cookieFilePath

    configFilePath = homedir + '/.auth.unisport'
    config = ConfigParser.ConfigParser()
    config.read(configFilePath)

    global hy_username, hy_password
    hy_username = config.get("unisport","username")
    hy_password = config.get("unisport","password")

    cookieFilePath = homedir + '/.cookies.unisport'

    # browser
    global br
    br = mechanize.Browser()

    # Cookie Jar
    global cj
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    cj.load(cookieFilePath, ignore_discard=True, ignore_expires=True)

    # Browser options
    br.set_handle_equiv(True)
    # br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    # Want debugging messages?
    #br.set_debug_http(True)
    #br.set_debug_redirects(True)
    #br.set_debug_responses(True)

    # User-Agent
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def hy_login():
    # test if session is on
    try:
        r = br.open('https://unisport.fi/yol/web/fi/crud/read/user.json?id=authenticated')
    except mechanize.HTTPError, response:
        # if not:
        sys.stderr.write("Probably a 401 error, so have to login. Maybe a cookie went bad.\n")

        # login then
        r = br.open('https://unisport.fi/Shibboleth.sso/HYLogin?target=https%3A%2F%2Funisport.fi%2Fyol%2Fweb%2Ffi%2FshibbolethLogin.do%3Fsite%3DCLIENT%26authenticationType%3DSHIBBOLETH%26target%3Dhttps%253A%252F%252Funisport.fi%252F%253Fpage%253Dliikumeilla%252362826539%2526login')
        br.select_form(nr=0)
        br.form['j_username']=hy_username
        br.form['j_password']=hy_password
        br.submit()

        # non-JS browser, we have to click a button
        br.select_form(nr=0)
        br.submit()

        # save cookies
        cj.save(cookieFilePath, ignore_discard=True, ignore_expires=True)
