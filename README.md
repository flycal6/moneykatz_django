# moneykatz_django
***Do not upload local_settings.py to your production server***

A Django / Python webapp for uploading / serving files, plus a handful of pages of personal whatever. 

It has a login required to view/upload files, and a server side cookie to count visits and keep people logged in.  The user gets
a csrf token to hopefully prevent forgery.  Currently, the cookie expires after two weeks.

Planned additions:<br />
  &nbsp; &nbsp; allow users to upload profile images and edit their profiles<br />
  &nbsp; &nbsp; drag and drop files in addition to the file picker

This is code for my personal website @ www.moneykatz.com
