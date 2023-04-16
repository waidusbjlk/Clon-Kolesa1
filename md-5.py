def hash_md5_func(text):
    import hashlib
    textUtf8 = text.encode("utf-8")
    hash_object = hashlib.md5(textUtf8)
    hash_text = hash_object.hexdigest()
    return hash_text
hash_result = hash_md5_func("қалаубекзат")
print(hash_result)