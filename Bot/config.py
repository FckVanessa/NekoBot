class Config(object):
    LOGGER = True
    TOKEN = "1965069129:AAFO3Om7xiK_BoUHJluELv4vZNY2Xw6PYHQ"
    MONGO_URI = "mongodb+srv://vira:MafGans@12@cluster0.qzouh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
