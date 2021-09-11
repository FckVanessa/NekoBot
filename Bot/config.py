class Config(object):
    LOGGER = True
    TOKEN = "1965069129:AAFO3Om7xiK_BoUHJluELv4vZNY2Xw6PYHQ"
    MONGO_URI = "mongodb+srv://username:<password>@cluster0.c11xf.mongodb.net/<dbname>?retryWrites=true&w=majority"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
