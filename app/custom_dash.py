from dash import Dash

class CustomDash(Dash):
    def interpolate_index(self, **kwargs):
        return '''
<!DOCTYPE html>
<html>
    <head>
        {metas}
        <title>{title}</title>

        <link rel="icon" href="assets/favicon/favicon.ico" sizes="any">
        <link rel="icon" type="image/svg+xml" href="assets/favicon/favicon.svg">
        <link rel="icon" type="image/png" sizes="96x96" href="assets/favicon/favicon-96x96.png">

        <link rel="apple-touch-icon" href="assets/favicon/apple-touch-icon.png">
        <link rel="manifest" href="assets/favicon/site.webmanifest">

        {css}
    </head>
    <body>
        {app_entry}
        <footer>
            {config}
            {scripts}
            {renderer}
        </footer>
    </body>
</html>
        '''.format(**kwargs)