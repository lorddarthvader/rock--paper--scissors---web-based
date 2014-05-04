#!/usr/bin/python

import cgi, random
print "Content-type:text/html\n\n"

print """
      <html>
          <title>Rock, Paper, Scissors</title>
          <style>
          #container
          {
            width: 350px;
            border: 3px solid #CCC;
            box-shadow: 0 10px 15px #CCC;
            margin: 50px auto;
            text-align : center;
            padding:10px;
          }
          </style>
          <body>
          <div id=container>
              <form action="" method=POST>
                  <select multiple=multiple name=q>
                  <option> Rock </option>
                  <option> Paper </option>
                  <option> Scissors </option>
                  </select><br><br>
	          <input type=submit name=submit value=Play!>
              </form>
          </body>
      </html>
      """

defeat = {'rock' : 'scissors', 'scissors' : 'paper', 'paper' : 'rock'}
storage = cgi.FieldStorage()
user = storage.getvalue('q').lower()
random.seed()
cpu = random.choice(defeat.keys())
if user != None:
    print "<b>cpu</b> : <i>%s</i> | <b>user</b> : <i>%s</i><br><br>" % (cpu.capitalize(), user.capitalize()) 
    print "<b>"
    if cpu == user:
        print "Draw!"
    elif cpu == defeat[user]:
        print "User wins!"
    else:
        print "Cpu wins!"
    print "</b></div>"
