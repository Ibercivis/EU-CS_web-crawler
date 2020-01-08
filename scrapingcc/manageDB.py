import mysql.connector
from mysql.connector import errorcode


def connectDB():
  try:
    cnx = mysql.connector.connect(user='user', password='pass',
										database='pruebasDB')
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
  return cnx

def closeDB(cnx):
  cnx.close()


######################################  USERS  ##########################################################  
def getUserID(cnx, email):
  userId = 0
  cursor = cnx.cursor()
  query = ("SELECT id FROM authtools_user where email=%s")
  cursor.execute(query, (email,))
  user = cursor.fetchone()
  if user != None:
    userId = user[0]
  cursor.close()
  return userId
################################################################################################################
######################################  END USERS  ##########################################################  
#############################################################################################################


######################################  PROJECTS  ##########################################################  
'''
def getAllProjects(cnx):
  cursor = cnx.cursor()
  query = ("SELECT * FROM projects_project")
  cursor.execute(query)
  for (project) in cursor:
     print(project)
  cursor.close()
 '''

def existProjectItem(cnx, url):
  cursor = cnx.cursor(buffered=True)
  query = ("SELECT * FROM projects_project WHERE url=%s") 
  cursor.execute(query, (url,))
  row_count = cursor.rowcount
  print(row_count)  
  cursor.close()
  return row_count != 0


def updateProjectItem(cnx, item):
  cursor = cnx.cursor()
  sentencia = ("UPDATE projects_project "
               "SET name=%s, start_date=%s, end_date=%s WHERE url=%s ")
  data = (item['name'], item['start_date'], item['end_date'], item['url'])
  cursor.execute(sentencia, data)
  cnx.commit()
  cursor.close()


def insertProjectItem(cnx, item, userID):
  cursor = cnx.cursor()
  sentencia = ("INSERT INTO projects_project "
               "(name, url, start_date, end_date, category, creator_id) "
               "VALUES (%s, %s, %s, %s, %s, %s)")
  data = (item['name'], item['url'], item['start_date'], item['end_date'], '', userID)
  cursor.execute(sentencia, data)
  cnx.commit()
  cursor.close()
  ################################################################################################################
  ######################################  END PROJECTS  ##########################################################  
  ################################################################################################################


######################################  IMAGES  ##########################################################  
def existDocumentItem(cnx, url):
  cursor = cnx.cursor(buffered=True)
  query = ("SELECT * FROM documents_document WHERE url=%s") 
  cursor.execute(query, (url,))
  row_count = cursor.rowcount
  print(row_count)  
  cursor.close()
  return row_count != 0


def updateDocumentItem(cnx, item):
  cursor = cnx.cursor()
  sentencia = ("UPDATE documents_document "
               "SET name=%s, author=%s, description=%s, datePublished=%s WHERE url=%s ")
  data = (item['name'], item['author'], item['description'], item['datePublished'], item['url'])
  cursor.execute(sentencia, data)
  cnx.commit()
  cursor.close()


def insertDocumentItem(cnx, item):
  cursor = cnx.cursor()
  sentencia = ("INSERT INTO documents_document "
               "(name, url, author, description, datePublished) "
               "VALUES (%s, %s, %s, %s, %s)")
  data = (item['name'], item['url'], item['author'], item['description'], item['datePublished'])
  cursor.execute(sentencia, data)
  cnx.commit()
  cursor.close()

  ################################################################################################################
  ######################################  END IMAGES  ##########################################################  
  ################################################################################################################