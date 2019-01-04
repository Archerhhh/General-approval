import pymysql
from framework import readConfig
#from common.Log import MyLog as Log
from framework.logger import logger

localReadConfig = readConfig.ReadConfig()
logger = logger(logger="configMySql").getlog()

class MySql:
    global host, username, password, port, database, config
    host = localReadConfig.get_mysql("host")
    username = localReadConfig.get_mysql("username")
    password = localReadConfig.get_mysql("password")
    port = localReadConfig.get_mysql("port")
    database = localReadConfig.get_mysql("database")
    config = {
        'host': str(host),
        'user': username,
        'passwd': password,
        'port': int(port),
        'db': database
    }

    def __init__(self):
        # self.log = Log.get_log()
        # self.logger = self.log.get_logger()
        self.db = None
        self.cursor = None

    def connectDB(self):
        """
        connect to database
        :return:
        """
        try:
            # connect to DB
            self.db = pymysql.connect(**config)
            # create cursor
            self.cursor = self.db.cursor()
            logger.info("Connect MySql successfully!")
        except ConnectionError as ex:
            logger.error(str(ex))

    # def executeSQL(self, sql, params):
    #     """
    #     execute sql
    #     :param sql:
    #     :return:
    #     """
    #     self.connectDB()
    #     # executing sql
    #     self.cursor.execute(sql, params)
    #     # executing by committing to DB
    #     self.db.commit()
    #     return self.cursor
    def executeSQL(self,sql):
        """
        execute sql
        :param sql:
        :return:
        """
        self.connectDB()
        # executing sql
        self.cursor.execute(sql)
        # executing by committing to DB
        self.db.commit()
        logger.info("executeSQL successfully")
        return self.cursor

    def get_all(self, cursor):
        """
        get all result after execute sql
        :param cursor:
        :return:
        """
        value = cursor.fetchall()
        return value

    def get_one(self, cursor):
        """
        get one result after execute sql
        :param cursor:
        :return:
        """
        value = cursor.fetchone()
        return value

    def closeDB(self):
        """
        close database
        :return:
        """
        self.db.close()
        logger.info("Database closed!")



