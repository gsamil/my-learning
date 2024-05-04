- Print counts of a column in a pyspark dataframe

```python
from pyspark.sql.functions import count, col, desc
from pyspark.sql.dataframe import DataFrame

def print_label_counts(df: DataFrame, label: str) -> None:
    df.groupBy(label) \
        .count() \
        .orderBy(desc('count')) \
        .show(n=1000, truncate=False)
```

- Mount an S3 bucket in Databricks

```python
AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""

aws_bucket_name = ""
mount_name = ""

df = spark.read.load(f"s3a://{aws_bucket_name}")
dbutils.fs.ls(f"s3a://{aws_bucket_name}/")
```

- Load logistic regression model from a local file

```python
from pyspark.ml.classification import LogisticRegressionModel

local_path_to_model = ""
model = LogisticRegressionModel.load(f"file://{local_path_to_model}")
```