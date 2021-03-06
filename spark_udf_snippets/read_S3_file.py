
# Code snippet to read file from s3 on PySpark 

#create the spark context sc and use hadoopFile api or newAPIHadoopFile

rdd = sc.hadoopFile('s3n://<path to the file>',

		'org.apache.hadoop.mapred.TextInputFormat',
                    'org.apache.hadoop.io.Text',
                    'org.apache.hadoop.io.LongWritable',
                     conf = {
  'fs.s3n.awsAccessKeyId': 'xxxxxxxx',
  'fs.s3n.awsSecretAccessKey': 'xxxxxxxxx',
})