import urllib.request
import json
document_list_url = 'https://api.data.gov:443/regulations/v3/documents.json?api_key=5fPcNxPyfzoIa0e2LXP315n7Uo18fQPLxLrrBwJz&dktid=BIS-2018-0006'
base_doc_url = 'https://api.data.gov:443/regulations/v3/document.json?api_key=5fPcNxPyfzoIa0e2LXP315n7Uo18fQPLxLrrBwJz&documentId='
api_key = '5fPcNxPyfzoIa0e2LXP315n7Uo18fQPLxLrrBwJz'

# Get response from url as dict
def get_json(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    return json.loads(response.read().decode('utf-8'))

def main():
    # Get response for all documents for docket given url
    doc_list_response = get_json(document_list_url)
    # Create list of document ID's from response
    doc_ids = [x['documentId'] for x in doc_list_response['documents']]

    for doc_id in doc_ids:
        # Create URL for document info
        doc_url = base_doc_url + doc_id
        # Get document info
        doc_response = get_json(doc_url)
        
        # If document has attachments
        if 'attachments' in doc_response:
            for a in doc_response['attachments']:
                file_url = a['fileFormats'][0]
                if file_url.endswith('excel12book'):
                    tmp = file_url.split('download?', 1)
                    f_req_url = tmp[0] + 'download?' + 'api_key=' + api_key + '&' + tmp[1]
                    print(f_req_url)
                    urllib.request.urlretrieve(f_req_url, doc_id + '.xlsx')
                
if __name__ == '__main__':
    main()
