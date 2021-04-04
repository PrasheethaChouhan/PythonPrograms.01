import dropbox
class TransferData:
    def __init__ (self,access_token):
        self.access_token=access_token
    def upload_file  (self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token="AB7d8aQtkQ0AAAAAAAAAAckBg7WKvNcY9CZw_oE6kQ8wxvLwaPS342DNcgSHCo7z"
    transferdata = TransferData(access_token)
    file_from=input("enter the file to transfer")
    file_to = input("enter the full path to upload to dropbox")
    transferdata.upload_file(file_from,file_to)
main()