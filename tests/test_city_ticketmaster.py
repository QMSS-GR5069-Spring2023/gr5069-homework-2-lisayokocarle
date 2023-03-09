from city_ticketmaster import city_ticketmaster

import pytest

# Test the request function
def test_for_api_get():
    with pytest.raises(TypeError):
        city_ticketmaster.apiget(city='Chicago')
    
def test_for_api_get2():
    with pytest.raises(TypeError):
        city_ticketmaster.apiget()

def test_apiget_with_only_one_value():
    with pytest.raises(TypeError):
        city_ticketmaster.apiget(city="Chicago")
        
# Test the City class
def test_class_city():
    with pytest.raises(ValueError):
        city_ticketmaster.City(cityname = "")

def test_class_city():
    with pytest.raises(ValueError):
        city_ticketmaster.City()
