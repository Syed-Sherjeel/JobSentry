import json
from fastapi import status


def test_create_job_1(client):
    data = {
        "title": "Sr. SWE",
        "company": "AWS",
        "company_url": "aws.zone.com/doan",
        "description": "Lead team",
        "location": "NY,BK",
    }
    response = client.post("/jobs/create-job/", content=json.dumps(data))
    assert response.status_code == 200
    assert response.json()["title"] == "Sr. SWE"
    assert response.json()["company"] == "AWS"
    assert response.json()["company_url"] == "aws.zone.com/doan"
    assert response.json()["description"] == "Lead team"
    assert response.json()["location"] == "NY,BK"


def test_create_job_2(client):
    data = {"title": "Jr. MLE", "company": "Azure"}
    response = client.post("/jobs/create-job/", content=json.dumps(data))
    assert response.status_code == 200
    assert response.json()["title"] == "Jr. MLE"
    assert response.json()["company"] == "Azure"
    assert response.json()["company_url"] is None
    assert response.json()["description"] is None
    assert response.json()["location"] == "Remote"


def test_read_job(client):
    data = {"title": "Jr. SRE", "company": "zone"}
    _ = client.post("/jobs/create-job/", content=json.dumps(data))
    response = client.get("/jobs/get/1/")
    assert response.status_code == 200
    assert response.json()["title"] == "Jr. SRE"


def test_read_all_jobs(client):
    data = {"title": "PSE AI", "company": "DOT", "location": "Islamabad"}

    client.post("/jobs/create-job/", content=json.dumps(data))
    client.post("/jobs/create-job/", content=json.dumps(data))

    response = client.get("/jobs/all/")
    print(response.json())
    assert response.status_code == 200
    assert response.json()[0]
    assert response.json()[1]


def test_update_one_job(client):
    data = {
        "title": "Jr. MLE",
        "company": "NoobSlayer",
        "description": "fastapi",
    }
    client.post("/jobs/create-job/", content=json.dumps(data))
    data["title"] = "Sr. MLE"
    data["location"] = "NY,BK"
    _ = client.put("/jobs/update/1", content=json.dumps(data))
    response = client.get("/jobs/get/1")
    print(response.json())
    assert response.json()["title"] == "Sr. MLE"
    assert response.json()["location"] == "NY,BK"


def test_delete_one_jobs(client):
    data = {
        "title": "PSE",
        "company": "NoobHunter",
        "description": "call kids git gud on fortnite",
    }
    _ = client.post("/jobs/create-job/", content=json.dumps(data))
    _ = client.delete("/jobs/delete/1")
    response = client.get("/jobs/get/1")
    assert response.status_code == status.HTTP_404_NOT_FOUND
