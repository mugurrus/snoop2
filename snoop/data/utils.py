def run_once(func):
    not_run = object()
    rv = not_run

    def wrapper():
        nonlocal rv
        if rv is not_run:
            rv = func()
        return rv

    return wrapper


def read_exactly(f, size):
    buffer = b''
    while len(buffer) < size:
        chunk = f.read(size - len(buffer))
        if not chunk:
            break
        buffer += chunk
    return buffer
