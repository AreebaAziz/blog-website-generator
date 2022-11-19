index_page = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Notes</title>
</head>
<body>
    <h1>{page_title}</h1>
    <ul>
    	{notes_list}
    </ul>
</body>
</html>
"""

subdir_item = "<li><a href=\"{title}/index.html\">{title}/</a></li>"
file_item = "<li><a href=\"{title}\">{title}</a></li>"

note_page = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Notes - {title}</title>
</head>
<body>
    {body}
</body>
</html>
"""