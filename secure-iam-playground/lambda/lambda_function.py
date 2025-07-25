import boto3

def lambda_handler(event, context):
    bucket = 'dev-bucket-lionel'
    key = 'test2.txt'
    
    s3 = boto3.client('s3')
    
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        content = response['Body'].read().decode('utf-8')
        print("Contenu du fichier :", content)
        return {
            'statusCode': 200,
            'body': content
        }
    except Exception as e:
        print("Erreur :", str(e))
        return {
            'statusCode': 500,
            'body': str(e)
        }

