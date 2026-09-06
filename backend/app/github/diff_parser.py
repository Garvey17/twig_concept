import unidiff
from pydantic import BaseModel
from typing import Literal


class HunkLine(BaseModel):
    line_number: int
    content: str
    type: Literal["addition", "context"]


class FileChange(BaseModel):
    filename: str
    hunks: list[HunkLine]

to_be_excluded = [
    ".lock", "package-lock.json", "yarn.lock", "poetry.lock",
    ".min.js", ".min.css",
    "dist/", "build/", "node_modules/",
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico",
    ".pdf", ".zip"
]

def check_excluded_file(file_name: str) -> bool:
    for pattern in to_be_excluded:
        if pattern.endswith("/"):
            if pattern in file_name:
                return True
        elif file_name.endswith(pattern):
            return True
    return False

def diff_parser(raw_diff: str) -> list[FileChange]:
    patched_files = unidiff.PatchSet(raw_diff)

    changed_files = []

    for patch_file in patched_files:
        if patch_file.is_binary_file or check_excluded_file(patch_file.path):
            continue
        hunks = []
        for hunk in patch_file:
            for line in hunk:
                if line.is_added:
                    line_no = line.target_line_no

                    hunks.append(HunkLine(
                        line_number=line_no,
                        content=line.value.rstrip("\n"),
                        type="addition"
                    ))
                elif line.is_context:
                    line_no = line.target_line_no

                    hunks.append(HunkLine(
                        line_number=line_no,
                        content=line.value.rstrip("\n"),
                        type= "context"
                    ))
        if not hunks:
            continue            
        changed_files.append(FileChange(
            filename=patch_file.path,
            hunks=hunks
        ))
    return changed_files