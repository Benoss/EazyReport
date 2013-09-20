
try:
    import MySQLdb as MysqlDriver
except ImportError:
    import libs.pymysql as MysqlDriver


try:
    import psycopg2 as PgDriver
except ImportError:
    pass


class DBManagerException(Exception):
    pass


class Stores():
    @classmethod
    def instance(cls, *args, **kwgs):
        if not hasattr(cls, "_instance"):
            cls._instance = cls(*args, **kwgs)
        return cls._instance

    _stores = {}
    def get_store_names(self):
        return [name for name in self._stores.keys()]

    def get_store(self, name):
        '@rtype: DBStore'
        return self._stores[name]
    
    def remove_store(self, name):
        del self._stores[name]
    
    def add_store(self, name, driver_type, host, user='', passwd='', db=None, port=None):
        if self._stores.has_key(name):
            raise DBManagerException("Store %s already exist"%(name))
        else:
            self._stores[name] = DBStore(name, {'driver_type':driver_type, 'host':host, 'user':user, 'passwd':passwd, 'port':port, 'db':db})
    
    



def dict_to_update(field_dict, table_name, where_clause = None):
    return_values = []
    return_string = "UPDATE "+table_name+" SET "

    update_strings = []
    #print field_dict
    for key, value in field_dict.iteritems():
        update_strings.append(key+"=%s")
        return_values.append(value)
    
    return_string = return_string + ",".join(update_strings)
    if where_clause:
        return_string = return_string + "WHERE " + where_clause
    
    return return_string, return_values

def dict_to_insert(field_dict, table_name):
    return_values = []
    return_string = "INSERT INTO "+table_name+" "

    update_strings = []
    update_symbols = []
    for key, value in field_dict.iteritems():
        update_strings.append(key)
        update_symbols.append("%s")
        return_values.append(value)
    
    return_string = return_string + " ("+ ",".join(update_strings) + ")"
    return_string = return_string + " VALUES (" + ",".join(update_symbols) + ")"
    
    return return_string, return_values



class DBStore():
    def __init__(self, name, infos):
        self.name = name
        self.connec_func = None
        self.connect_infos = {}
         
        self.connect_infos['host'] = infos['host']
        self.connect_infos['user'] = infos['user']
        self.connect_infos['passwd'] = infos['passwd']
        if infos['port']:
            self.connect_infos['port'] = infos['port']
        if infos['db']:
            self.connect_infos['db'] = infos['db']
        
        if infos['driver_type'] == 'mysql':
            self.connec_func = MysqlDriver.connect
        elif infos['driver_type'] == 'postgres':
            self.connect_infos['password'] = infos['passwd']
            del(self.connect_infos['passwd'])
            self.connect_infos['database'] = infos['db']
            del(self.connect_infos['db'])
            self.connec_func = PgDriver.connect
            
        self._last_query_string = ""
        self._last_query_args = None
        self._last_executed = ""

        self.connected = False
        
    def connect(self):
        if self.connec_func:
            self.connection = self.connec_func(**self.connect_infos)
            self.connected = True
            
            
    def get_last_query(self):
        return self._last_executed, self._last_query_string, self._last_query_args
            
    def quick_query(self, query_string, *args):
        if not self.connected:
            self.connect()
        cursor = self.connection.cursor()
        self._last_query_string = query_string
        self._last_query_args = args
        cursor.execute(query_string, *args)
        res = cursor.fetchall()
        self._last_executed = cursor._last_executed
        cursor.close()
        return res
    
    def quick_query_dict(self, query_string, *args):
        if not self.connected:
            self.connect()
        cursor = self.connection.cursor()
        cursor.execute(query_string, *args)
        return_dict = []
        row = cursor.fetchone()
        while row :
            row_dict = {}
            for index, key  in enumerate(cursor.description):
                row_dict[key[0]] = row[index]
            return_dict.append(row_dict)
            row = cursor.fetchone()
        cursor.close()
        return return_dict
    
    
    def quick_commit_query(self, query_string, *args):
        if not self.connected:
            self.connect()
        cursor = self.connection.cursor()
        cursor.execute(query_string, *args)
        self.connection.commit()
        rowcount = cursor.rowcount
        cursor.close()
        return rowcount
    
    def query_insert_dict(self, field_dict, table_name):
        string_to_inserts, values_arg = dict_to_insert(field_dict, table_name)
        return self.quick_commit_query(string_to_inserts, values_arg)
    
    def query_update_dict(self, field_dict, table_name, where_clause):
        string_to_inserts, values_arg = dict_to_update(field_dict, table_name, where_clause)
        return self.quick_commit_query(string_to_inserts, values_arg)
    
    def query(self, query_string, *args):
        if not self.connected:
            self.connect()
        cursor = self.connection.cursor()
        cursor.execute(query_string, *args)
        res = Result(cursor)
        cursor.close()
        return res
    
    
    def query_yield(self, query_string, *args):
        if not self.connected:
            self.connect()
        cursor = self.connection.cursor()
        cursor.execute(query_string, *args)
        row = cursor.fetchone()
        while row:
            row = cursor.fetchone()
            yield row
        cursor.close()
        
            
class Result():
    def __init__(self, cursor):
        self.rows = cursor.fetchall()
        self.columns = [row[0] for row in cursor.description or [[]]]
        self.rowcount = cursor.rowcount

def DBM(store_name):
    '@return: DBStore'
    store = Stores().get_store(store_name)
    '@type store: DBStore'
    return store
