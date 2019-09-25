from aws import boto3
from file_uploader import S3FileUploader, AzureFileUploader

def save_user_details(user_details_dict):
    # .
    # .
    # Save first name, last name etc.

    dp = user_details_dict['dp']
    b = boto3()
    b.upload_file(dp)


def get_file_storage_service(name):
    service_to_obj_map = {
        'S3': S3FileUploader({}),
        'Azure': AzureFileUploader({}),
    }

    obj = service_to_obj_map.get(name)
    if not obj:
        raise Exception('Invalid Service {0}'.format(name))
    return obj


class StorageServiceFactory(object):
    def get_storage(name):
        service_to_obj_map = {
         'S3': S3FileUploader({}),
         'Azure': AzureFileUploader({}),
     }

     obj = service_to_obj_map.get(name)
     if not obj:
         raise Exception('Invalid Service {0}'.format(name))
     return obj

def save_user_details_interface(user_details_dict):
    d = user_details_dict['dp']
    storage_service = get_file_storage_service('S3')
    storage_service.upload(d)

if __name__ == '__main__':
    details = {'name': 'Ritesh', 'dp': '123'}
    save_user_details(details)

    save_user_details_interface(details)
