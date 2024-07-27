def getbyid(type, id):
    type = type.upper()
    if type == 'ANIME' and type != 'MANGA':
        variables = {
            'type': type,
            'id': id
        }
        return variables

