def set_query(task: str):
    special_chars = {ord('ä'):'ae', ord('ü'):'ue', ord('ö'):'oe', ord('ß'):'ss'}
    query = str(input("Gebe hier deine Frage ein: ")).translate(special_chars)
    return query