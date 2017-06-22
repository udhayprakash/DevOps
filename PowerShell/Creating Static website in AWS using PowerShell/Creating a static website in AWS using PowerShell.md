## Creating a Static Website in AWS Cloud 

Initially, set the AWS credentials using 
```bash
Set-AWSCredentials demoProfile
```
Then, set the default region using 
```bash
Set-DefaultAWSRegion
```

Now, Create a new AWS S3 bucket using
```bash
New-S3Bucket -BucketName demoBlog
```
Then, enable static website hosting by setting a default document using
```bash
 Write-S3BucketWebsite -BucketName demoBlog -WebsiteConfiguration_IndexDocumentSuffix index.html
```
**Ensure** that the _index.html_ is present in the directory from where this script is running. 
 
 As by default, the bucket is private, so add a policy allowing people to fetch the content.
 ```bash
Write-S3bucketPolicy -BucketName demoBlog -Policy (Get-Content ./bucketpolicy.json -Raw)
```
Similarly, **Ensure** that the _bucketpolicy.json_ is present in the directory from where this script is running.
 
 Finally, upload the generated content to the bucket
 ```bash
Write-S3Object -BucketName demoBlog -Folder . -KeyPrefix / -Recurse
```
