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
                'review':result[4],
                'rating':result[5],
                'link':result[6],

            }
            payload.append(content)
            content={}
        return payload
    def createProduct(self,data):
        title=data['title']
        price=data['price']
        Description=data['Description']
        review=data['review']
        rating=data['rating']
        link=data['link']
        if(data['id']==''):
            sql="INSERT INTO `product`(`title`, `price`, `description`, `review`, `rating`, `link`) VALUES (%s,%s,%s,%s,%s,%s)"
            rez=self.cursor.execute(sql,(title,price,Description,review,rating,link))
            self.cursor.connection.commit()
        else:
            id=data['id']
            sql="INSERT INTO `product`(`id`,`title`, `price`, `description`, `review`, `rating`, `link`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            rez=self.cursor.execute(sql,(id,title,price,Description,review,rating,link))
            self.cursor.connection.commit()

        if(rez==1):
            return 200
        else:
            return 400
    def updateProduct(self,data,pid):
        #id=data['id']
        title=data['title']
        price=data['price']
        Description=data['Description']
        review=data['review']
        rating=data['rating']
        link=data['link']
        sql="UPDATE `product` SET `title`=%s, `price`=%s, `description`=%s, `review`=%s, `rating`=%s, `link`=%s WHERE `id`=%s"
        rez=self.cursor.execute(sql,(title,price,Description,review,rating,link,pid))
        self.cursor.connection.commit()

        if(rez==1):
            return 200
        else:
            return 400
    def deleteProduct(self,pid):
        sql="DELETE FROM `product` WHERE id=%s"
        rez=self.cursor.execute(sql,pid)
        self.cursor.connection.commit()
        if(rez==1):
            return 200
        else:
            return 400
