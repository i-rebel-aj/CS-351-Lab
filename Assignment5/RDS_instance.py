import boto3
client=boto3.client('rds')
response = client.create_db_instance(
    DBName='TestDB',
    #Specifies the name of the database that you want to create when the instance is launched (MySQL) 
    DBInstanceIdentifier='CloudLab5',
    AllocatedStorage=20,
    DBInstanceClass='db.t2.micro',
    Engine='mysql',
    MasterUsername='admin',
    MasterUserPassword='akshay123',
    VpcSecurityGroupIds=[
        'sg-0e01f8abae0cdd559',
    ],
    Port=3306,
    AvailabilityZone="us-east-2a",
    #MultiAZ=True,
    EngineVersion='8.0.20',
    AutoMinorVersionUpgrade=True,
    LicenseModel='general-public-license',
    PubliclyAccessible=True,
    MonitoringInterval=0,
    DomainIAMRoleName='AWSServiceRoleForRDS',
    MaxAllocatedStorage=21
)
print("RDS Instance created success")
#


