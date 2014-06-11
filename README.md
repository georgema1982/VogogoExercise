VogogoExercise
==============

As part of Vogogo development exercise, implement the code for a checkout system that handles pricing  schemes such as “apples cost 50 cents each; three apples cost $1.30”.


The Goal
========

Write a console program that takes as input an unordered list of singular items from a shopping cart and “checks them out”, printing  an itemized receipt and a total price.

The receipt will follow Superstore's sytle, ie. in the case of "Buy n of them, and they’ll cost you y cents.", the item will be displayed as ``n/$y``. For example, "3 of them cost $4.97" will be displayed as ``3/$4.97``


Requirements
============

Please make sure that Python 2.7 has been installed. Virtualenv is recommended.

Installation
============

In any local directory, enter the following commands:

	$ git clone https://github.com/georgema1982/VogogoExercise.git

	$ cd VogogoExercise

	$ pip install -r requirements.txt

	$ python manage.py syncdb

	$ python manage.py migrate

Optionally, you can run the unit tests inside the repository folder with the following command:

    $ python manage.py test


Usage
=====

There are two parts in this program. One part is the Admin part which is a web application where you can add items and their pricing rules. The other part is the console that takes as input an unordered list of singular items from a shopping cart and “checks them out”, printing  an itemized receipt and a total price.


Admin
-----

To start the Admin, run the following command in the repository folder:

	$ python manage.py runserver

Then go to `http://localhost:8000/admin/ <http://localhost:8000/admin/>`__ and login with the credential you created during installation.

After login, go to Checkout > Items to add/edit/delete items and their pricing rules.

> Please note that each item must have an active base price, which is the price for an individual item.


Console Program
---------------

After items and the pricing rules are added, run the following command in the repository folder:
	$ python manage.py do_checkout code1 [code2 code3 ...]

> Codes should correspond to the item codes defined in the Admin. Nonexistent codes will cause the console program to fail. Codes should be separated by one space.