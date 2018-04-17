import urllib.request
import json
document_list_url = 'https://api.data.gov:443/regulations/v3/documents.json?api_key=5fPcNxPyfzoIa0e2LXP315n7Uo18fQPLxLrrBwJz&dktid=BIS-2018-0006'
base_doc_url = 'https://api.data.gov:443/regulations/v3/document.json?api_key=5fPcNxPyfzoIa0e2LXP315n7Uo18fQPLxLrrBwJz&documentId='
api_key = '5fPcNxPyfzoIa0e2LXP315n7Uo18fQPLxLrrBwJz'
base_url = 'https://api.data.gov:443/regulations/v3/'
docket_id = 'BIS-2018-0006'

# Returns url for regulations.gov api call
def create_url(subpath, key=api_key, dktid=None, document_id=None, attach_num=None, content_type=None):
    ret = base_url
    ret += subpath
    ret += '?api_key='; ret += key
    if subpath == 'documents.json':
        ret += '&dktid='; ret += dktid
        return ret
    elif subpath == 'document.json':
        ret += '&documentId='; ret += document_id
        return ret
    elif subpath == 'download':
        ret += '&documentId='; ret += document_id
        ret += '&attachmentNumber='; ret += str(attach_num)
        ret += '&contentType='; ret += content_type
        return ret
    else:
        print("Bad url call")
        return None

# Get response from url as dict
def get_json(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    return json.loads(response.read().decode('utf-8'))

def main():
    # Get response for all documents for docket given url
    doc_list_response = get_json(create_url('documents.json', dktid=docket_id))
    # Create list of document ID's from response
    doc_ids = [x['documentId'] for x in doc_list_response['documents']]

    for doc_id in doc_ids:
        # Get document info
        doc_response = get_json(create_url('document.json', document_id=doc_id))
        
        # If document has attachments
        if 'attachments' in doc_response:
            for a in doc_response['attachments']:
                file_url = a['fileFormats'][0]
                attach_num = a['attachmentOrderNumber']
                if file_url.endswith('excel12book'):
                    tmp_url = create_url('download', document_id=doc_id, attach_num=attach_num, content_type='excel12book')
                    urllib.request.urlretrieve(tmp_url, doc_id + '.xlsx')
                
if __name__ == '__main__':
    main()
