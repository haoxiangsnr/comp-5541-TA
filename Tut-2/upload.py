from dagshub import get_repo_bucket_client

# Get a boto3.client object
s3 = get_repo_bucket_client("haoxiangsnr/my-first-repo")

# Upload file
s3.upload_file(
    Bucket="my-first-repo",  # name of the repo
    Filename="Avaya Voice Record Sample 2.wav",  # local path of file to upload
    Key="Avaya Voice Record Sample 2.wav",  # remote path where to upload the file
)
