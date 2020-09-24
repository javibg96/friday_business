import pyspark
import os

os.environ["HADOOP_HOME"] = "C:/Program Files/winutils"
os.environ["JAVA_HOME"] = "C:/Program Files/Java/jdk1.8.0_261"

sc = pyspark.SparkContext()
# nums = sc.parallelize([1, 2, 3, 4])
# print(nums.take(2))  # coge los dos primeros numeros output: [1, 2]

# ejemplo de funcion lambda
# squared = nums.map(lambda x: x*x).collect()
# for num in squared:
#     print('%i ' % num)


sqlContext = pyspark.SQLContext(sc)
# list_p = [('John', 19), ('Smith', 29), ('Adam', 35), ('Henry', 50)]
# rdd = sc.parallelize(list_p)
# ppl = rdd.map(lambda x: pyspark.sql.Row(name=x[0], age=int(x[1])))
# DF_ppl = sqlContext.createDataFrame(ppl)
# DF_ppl.printSchema()
# OUTPUT:
# root
# |-- name: string (nullable = true)
# |-- age: long (nullable = true)


url = "https://raw.githubusercontent.com/guru99-edu/R-Programming/master/adult_data.csv"
sc.addFile(url)
df = sqlContext.read.csv(pyspark.SparkFiles.get("adult_data.csv"), header=True, inferSchema=True)
# print(df.head()) # NO HACER CON CSV LEIDOS POR SQL, no se ve nada
df.printSchema()
df.show(5, truncate=False)  # es un print(df.head(5)) bien hecho
df.select('age', 'fnlwgt').show(5)  # solo te muestra esas 2 columnas y los 5 primeros resultados
df.groupBy("education").count().sort("count", ascending=True).show()  # cuenta num filas por nv educativo
df.describe().show()  # descripcion de datos, conteo, media, desviacion media, min, max
df.describe('capital_gain').show()  # solo de una columna

df.crosstab('age', 'label').sort("age_label").show()
# tabulacion cruzada, número de personas con ingresos inferiores o superiores a 50k por nivel educativo.

df.drop('education_num')  # eliminar columna
df.filter(df.age > 40).count()  # filtrar por año y conteo total
df.groupby('marital').agg({'capital_gain': 'mean'}).show()  # filtrar por columna y obtener la media de ingresos

df.filter(df.native_country == 'Holand-Netherlands').count()
df.groupby('native_country').agg({'native_country': 'count'}).sort(asc("count(native_country)")).show()
df_remove = df.filter(df.native_country != 'Holand-Netherlands')    # un drop mas tecnico
