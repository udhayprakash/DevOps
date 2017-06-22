import boto3
from pprint import pprint
from subprocess import Popen, PIPE
client = boto3.client('s3')
response = client.list_buckets()
print "%51s %15s %21s %18s %11s %13s"%("BucketName", "Region", "Versioning", "S3Logging", "TotalSize", "TotalObjects")
for res in response["Buckets"]:
        try:
                print "%51s"%(res["Name"]),
                resLocation = client.get_bucket_location(
                Bucket=res["Name"])
                if resLocation['LocationConstraint']:
                        print "%15s"%(resLocation['LocationConstraint']),
                else:
                        print "%15s"%("us-east-1"),
                resVersioning = client.get_bucket_versioning(Bucket=res["Name"])
                if resVersioning.get('Status', None):
                    print "%21s"%("Versioning"+str(resVersioning['Status'])),
                else:
                    print "%21s"%("VersioningNotEnabled"),
                resBucktLogging = client.get_bucket_logging(Bucket=res["Name"])
                if resBucktLogging.get('LoggingEnabled', None):
                    print "%18s"%("LoggingEnabled"),
                else:
                    print "%18s"%("LoggingNotEnabled"),
                
                p = Popen("aws s3 ls s3://"+str(res["Name"])+" --recursive --human-readable --summarize", shell=True, stdout=PIPE)
                (pOut, pErr) = p.communicate()
                if pErr:
                    print "Unable to get bucket size", pErr
                else:
                    print "%11s %13s"%(pOut.strip().split('\n')[-1].strip().split(":")[1], pOut.strip().split('\n')[-2].strip().split(":")[1])
        except Exception as ex:
                print ex
