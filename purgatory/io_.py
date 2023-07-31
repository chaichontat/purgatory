from contextlib import contextmanager
from fcntl import fcntl
from pathlib import Path


@contextmanager
def lock(path: str):
    locked_file_descriptor = open(Path(path), "w+")
    fcntl.lockf(locked_file_descriptor, fcntl.LOCK_EX)
    yield locked_file_descriptor
    locked_file_descriptor.close()
