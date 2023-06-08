import json


def test_create_job_1(client):
    data = {'title': 'Sr. SWE',
            'company': 'AWS',
            'company_url': 'aws.zome.com/doan',
            'description': 'Lead team',
            'location': 'NY,BK'}
    response = client.post('/jobs/create-job/', content=json.dumps(data))
    assert response.status_code == 200
    assert response.json()['title'] == 'Sr. SWE'
    assert response.json()['company'] == 'AWS'
    assert response.json()['company_url'] == 'aws.zome.com/doan'
    assert response.json()['description'] == 'Lead team'
    assert response.json()['location'] == 'NY,BK'


def test_create_job_2(client):
    data = {'title': 'Jr. MLE', 'company': 'Azure'}
    response = client.post('/jobs/create-job/', content=json.dumps(data))
    assert response.status_code == 200
    assert response.json()['title'] == 'Jr. MLE'
    assert response.json()['company'] == 'Azure'
    assert response.json()['company_url'] is None
    assert response.json()['description'] is None
    assert response.json()['location'] == 'Remote'


def test_read_job(client):
    data = {'title': 'Jr. SRE', 'company': 'zone'}
    _ = client.post('/jobs/create-job/', content=json.dumps(data))
    response = client.get('/jobs/get/1/')
    assert response.status_code == 200
    assert response.json()['title'] == 'Jr. SRE'
