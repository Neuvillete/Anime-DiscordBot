def removetags(text):
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


def cutlength(text):
    if len(text) > 900:
        return text[:900] + "..."
    return text


def replacenone(text):
    if text is None:
        return 'N/A'
    return text

