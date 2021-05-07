import json
from pyspark import SparkContext, SparkConf

conf = SparkConf()
conf.set('spark.executor.allowSparkContext', 'true')
sc = SparkContext.getOrCreate(conf=conf)
dataset_json = sc.textFile("dataset.json")
dataset = dataset_json.map(lambda x: json.loads(x))
dataset.persist()
def compare_elems(x):
    return True

filtered = dataset.filter(lambda x: compare_elems(x))
filtered.take(1)
