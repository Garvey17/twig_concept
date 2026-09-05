
to_be_excluded = [
    ".lock", "package-lock.json", "yarn.lock", "poetry.lock",
    ".min.js", ".min.css",
    "dist/", "build/", "node_modules/",
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico",
    ".pdf", ".zip"
]

def check_excluded_file(file_name: str) -> bool:
    for file_format in to_be_excluded:
        if file_name.startswith(file_format) or file_name.endswith(file_format):
            return True

    return False


