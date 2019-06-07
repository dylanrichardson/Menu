# Menu

Easily create command-line menus.


Install
-

    pip install Menu
    
**Note:** Use with Python 2 requires the [future](https://pypi.org/project/future/) package to be installed.

Create the Menu
-

The Menu constructor arguments are all optional. The arguments are options, title, message, prompt, and refresh. Options is a list of tuples consisting of a name and a handler. Refresh is a handler called before showing the menu.

	Menu() # empty menu, will close upon opening
    Menu(options=[("Option Name", optionHandler)]) # customize the options
    Menu(options=[("Option Name", optionHandler, {'key': val})]) # add kwargs to option handlers
	Menu(title="Menu title") # customize the title
	Menu(message="Message text") # customize the message, disabled by default
	Menu(prompt=">") # customize the user input prompt
	Menu(refresh=refreshHandler) # customize the refresh handler

Open the Menu
-

    menu = Menu()
    menu.open()

Close the Menu
-
from the instance after creating the menu

    menu = Menu()
    menu.close()

or use the static method before creating the menu

    Menu(options = [("Close", Menu.CLOSE)])

Edit the menu
-

    menu = Menu()
    menu.set_options([("new option name", newOptionHandler)])
    menu.set_title("new title")
    menu.set_message("new message")
    menu.set_prompt("new prompt")

Create a Submenu
-

	main = Menu(title = "Main Menu")
    sub = Menu(title = "Submenu")
    main.set_options([
        ("Open submenu", sub.open),
        ("Close main menu", main.close)
    ])
    sub.set_options([
        ("Return to main menu", sub.close)
    ])
    main.open()

Example
-

[example.py](test/example.py)


Development
-

Symlink package to immediately see changes locally
    
    $ pip install -e .

Build and publish to PyPI

    $ python setup.py register sdist upload
