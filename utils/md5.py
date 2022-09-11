import hashlib


def get_digest(bytes):
    md5 = hashlib.md5()
    md5.update(bytes)
    digest = md5.hexdigest()
    return digest


def get_file_digest(filepath):
    block_size = 10 * 1024 * 1024
    with open(filepath, 'rb') as f:
        md5 = hashlib.md5()

        chunk = f.read(block_size)
        while len(chunk) > 0:
            md5.update(chunk)
            chunk = f.read(block_size)

        result = md5.hexdigest()

        return result

