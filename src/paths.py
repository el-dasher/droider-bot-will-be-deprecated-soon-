# SE VOCÊ FOR RODAR O PROJETO LOCALMENTE ATRIBUA O VALOR DE "debug" PARA "True"

from pathlib import Path

debug = False # debug = True SE VOCÊ FOR RODAR O PROJETO LOCALMENTE!!!

if debug:
    print("O BOT ESTÁ RODANDO LOCALMENTE")
    
    COGS_PATH = Path('./lib/cogs')

    WEIRD_TAGS_RESPONSE_PATH = Path("./lib/db/data/json/weird_tags_response.json")
    LUCKY_PATH = Path("./lib/db/data/json/lucky_responses.json")
    MONTHS_PATH = Path("./lib/db/data/json/months.json")
else:
    print('O BOT ESTÁ RODANDO EM "PRODUÇÃO')
    
    COGS_PATH = Path('./src/lib/cogs')

    WEIRD_TAGS_RESPONSE_PATH = Path(".src/lib/db/data/json/weird_tags_response.json")
    LUCKY_PATH = Path("./src/lib/db/data/json/lucky_responses.json")
    MONTHS_PATH = Path("./src/lib/db/data/json/months.json")