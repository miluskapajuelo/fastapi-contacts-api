def test_root_ok(client):
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"ok":True}

def test_create_contact(client):
    payload = {
        "first_name" : "Ana",
        "last_name": "Perez",
        "email": "ana@test.com",
        "phone_number": "999111222"
    }

    r = client.post("/api/contacts", json=payload)
    assert r.status_code == 200

    data = r.json()
    assert isinstance(data["id"], int)
    assert data["email"] == "ana@test.com"
    assert "date_created" in data

def test_get_contacts_list(client):
    client.post("/api/contacts", json={
          "first_name" : "A",
        "last_name": "A",
        "email": "a@test.com",
        "phone_number": "111"
    })
    client.post("/api/contacts", json={
          "first_name" : "B",
        "last_name": "B",
        "email": "b@test.com",
        "phone_number": "444"
    })


    r = client.get("/api/contacts")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) >= 2


def test_get_contact_by_id(client):
    created = client.post("/api/contacts", json={
    "first_name" : "C",
        "last_name": "C",
        "email": "c@test.com",
        "phone_number": "333"
        }).json()

    cid = created["id"]
    r = client.get(f"/api/contacts/{cid}/")
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == cid
    assert data["email"]=="c@test.com"

def test_delete_contact( client):
    created = client.post("/api/contacts", json={
    "first_name" : "D",
    "last_name": "D",
    "email": "d@test.com",
    "phone_number": "999|"
    }).json()
    cid = created["id"]

    r=client.delete(f"/api/contacts/{cid}")
    assert r.status_code == 200
    assert r.json()["message"].lower().startswith("successfully")

        # intentar borrarlo otra vez → 404
    r2 = client.delete(f"/api/contacts/{cid}/")
    assert r2.status_code == 404
    assert r2.json()["detail"] == "user does not exist"

def test_update_contact(client):
    created = client.post("/api/contacts", json={
        "first_name": "E",
        "last_name": "E",
        "email": "e@test.com",
        "phone_number": "555"
    }).json()
    cid = created["id"]

    r = client.put(f"/api/contacts/{cid}/", json={"first_name": "Elena"})
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == cid
    assert data["first_name"] == "Elena"
    assert data["email"] == "e@test.com"