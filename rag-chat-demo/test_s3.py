import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def test_s3_connection():
    try:
        s3 = boto3.client('s3',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            region_name='eu-west-3'
        )
        
        bucket_name = os.getenv('AWS_BUCKET_NAME')
        print(f"\nTesting connection to bucket: {bucket_name}")
        print(f"AWS Access Key ID: {os.getenv('AWS_ACCESS_KEY_ID')}")
        print(f"Bucket name: {bucket_name}")
        
        response = s3.list_objects_v2(
            Bucket=bucket_name,
            Prefix='documents/'
        )
        
        if 'Contents' in response:
            print("\nDocuments trouvés:")
            for obj in response['Contents']:
                print(f"- {obj['Key']}")
                print(f"  Size: {obj['Size']} bytes")
                print(f"  Last modified: {obj['LastModified']}")
        else:
            print("\nAucun document trouvé dans le dossier 'documents/'")
            print("Assurez-vous que:")
            print("1. Le dossier 'documents/' existe dans votre bucket")
            print("2. Il contient au moins un fichier")
            print("3. Le chemin est exactement 'documents/' (attention aux majuscules)")
            
    except Exception as e:
        print(f"\nErreur: {str(e)}")

if __name__ == "__main__":
    test_s3_connection() 