# unisport-command-line
Manage your Unisport reservations with Python

# Requirements

    sudo apt-get install python-mechanize
    sudo apt-get install jq
    
You also need a Helsinki University account.

# Setup

Create a username/password file:

    echo '[unisport]' > $HOME/.auth.unisport
    echo 'username = mylogin' >> $HOME/.auth.unisport
    echo 'password = mypass' >> $HOME/.auth.unisport

Create a cookie jar file:

    echo '#LWP-Cookies-2.0' >  $HOME/.cookies.unisport

# Usage

Read available events, e.g. futsal (no authentication needed):

    ./get-events-json.sh 826539 | jq

Make sure your credentials work:

    python get-omattiedot-json.py

Make a reservation:

    python make-reservation.py 206607525

Cancel a reservation:

    python make-reservation.py 207094658

