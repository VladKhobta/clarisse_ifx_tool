def add_to_shelf(app, path: str,  name: str = '', description: str = ''):
    shelf = app.get_shelf()
    shelf.add_item(0, 'custom', name, description, path, )


if __name__ == "__main__":
    clarisse_app = ix.application

    # adding script to the custom shelf
    script_path = r"D:\Projects\clarisse_ifx\scripts\script.py"
    add_to_shelf(clarisse_app, script_path, '...')
