from pyspark.sql.spark import col

data =[(1,"Venkat"),
        (2,"Divya")

]
schm=["id","Name"]

df=spark.createDataframe(schm,data)
df.show()
