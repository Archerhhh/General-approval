import cx_Oracle
from framework import readConfig
from framework.logger import logger

localReadConfig = readConfig.ReadConfig()
logger = logger(logger="configMySql").getlog()

class Oracle:
    global host,pwd, port, tnsname
    host = localReadConfig.get_oracle("host")
    #username = localReadConfig.get_oracle("username")    #审批个性化，需要连接gd_base和gd_dbwizard，所以不固定用户名，便于切换数据库
    pwd = localReadConfig.get_oracle("password")
    port = localReadConfig.get_oracle("port")
    tnsname = localReadConfig.get_oracle("tnsname")   #实例名

    def __init__(self):
        # self.log = Log.get_log()
        # self.logger = self.log.get_logger()
        self.db = None
        self.cursor = None

    def connectDB(self,username):
        """
        connect to database
        :return:
        """
        try:
            # connect to DB
            self.db = cx_Oracle.connect(username, pwd, host+':'+port+'/'+tnsname)
            # create cursor
            self.cursor = self.db.cursor()
            logger.info("Connect Oracle successfully!")
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
    def executeSQL(self,username,sql):
        """
        execute sql
        :param sql:
        :return:
        """
        self.connectDB(username)
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

