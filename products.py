from connectdb import mysql
class Products:
    def __init__(self):
        self.cursor=mysql.connect().cursor()
    def getProducts(self):
        self.cursor.execute("SELECT * FROM product")
        aData=self.cursor.fetchall()
        payload=[]
        content={}
        for result in aData:
            content={
                'id':result[0],
                'title':result[1],
                'price':result[2],
                'Description':result[3],
            }
            payload.append(content)
            content={}
        return payload
