from abc import ABC, abstractmethod

class S3Connection(object):
    def __init__(self, config):
        print('Connection Established')

    NAME = 'S3'

    def upload(self, data):
        print('File uploaded to {0}'.format(self.NAME))


class AzureConnection(object):
    NAME = 'Azure'
    def __init__(self, config):
        print('Success')

    def put(self, data):
        print('File uploaded to {0}'.format(self.NAME))


class FileUploader(ABC):
    def __init__(self, config_dict):
        self.config = config_dict

    @abstractmethod
    def _connect(self):
        pass

    @abstractmethod
    def upload(self, data):
        pass

class S3FileUploader(FileUploader):
    def _connect(self):
        # Can use boto3 api here
        return S3Connection(self.config)

    def upload(self, data):
        c = self._connect()
        c.upload(data)


class AzureFileUploader(FileUploader):
    def _connect(self):
        return AzureConnection(self.config)

    def upload(self, data):
        c = self._connect()
        c.put(data)


if __name__ == '__main__':
    print('\n========== UPLOAD to S3 ===================')
    s3_uploader =  S3FileUploader({'username': '', 'password': ''})
    f = open('test.txt')
    s3_uploader.upload(f)

    print('\n========= UPLOAD to AZURE ================')
    azure_uploader = AzureFileUploader({'access_id': '', 'secret_key': ''})
    azure_uploader.upload(f)
