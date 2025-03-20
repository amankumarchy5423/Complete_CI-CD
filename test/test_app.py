from src.app import app

def test_home():
    response = app.test_client().get()

    assert response.status_code == 200
<<<<<<< HEAD
    
=======
>>>>>>> a26e73c (some changeg)
