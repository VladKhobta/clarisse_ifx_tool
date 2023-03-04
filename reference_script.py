import os


def choose_file_via_browser(app: ix.api.ClarisseApp) -> str:
    start_path = r"D:"
    extension = 'Usd\t*.{usd}\n'
    return str(app.open_file(start_path, 'Choosing reference file', extension))


# importing asset with provided path function
def import_asset(app: ix.api.ClarisseApp, asset_path: str) -> bool:
    if os.path.isfile(asset_path):
        scene_context = app.get_current_context()
        asset_context = scene_context.add_context('assets')
        prop_context = asset_context.add_context('Prop')

        ix.cmds.CreateFileReference(str(prop_context), [asset_path, ])
    else:
        print('No such file')
        return False

    return True


if __name__ == '__main__':
    clarisse_app = ix.application

    file_path = choose_file_via_browser(clarisse_app)
    import_asset(clarisse_app, file_path)
