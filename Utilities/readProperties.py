import configparser

config=configparser.RawConfigParser()
config.read("C:\\Users\\prata\\PycharmProjects\\pythonProject\\Automation_Excercise_Project\\Configurations\\config.ini")

#Reading properties from config.ini
class Readconfig:
    @staticmethod
    def getURL():
        URL=config.get('CommonInfo','baseURL')
        return URL
    @staticmethod
    def getEmail():
        email=config.get('CommonInfo','email')
        return email
    @staticmethod
    def getpassword():
        password=config.get('CommonInfo','Password')
        return password
    @staticmethod
    def xlfilename():
        file=config.get('CommonInfo','file')
        return file


