from aws import S3Manager

s3_manager = S3Manager(access_key="[ACCESS_KEY]", 
                       secret="ACCESS_SECRET")

bucket_name = "study-market-mining"

# criando bucket
s3_manager.create_bucket(bucket_name)

# enviando imagem/arquivo/objeto
s3_manager.upload_object("images/sao-paulo.png", bucket_name, "sao-paulo.png")

# listando buckets
buckets = s3_manager.list_buckets()

for bucket in buckets["Buckets"]:
    print(bucket["Name"])

# listando objetos de bucket
buckets = s3_manager.list_objects(bucket_name)

for bucket in buckets["Contents"]:
    print(bucket["Key"])

# download object
s3_manager.download_object(bucket_name, "sao-paulo.png", "downloads/tricolor.png")
