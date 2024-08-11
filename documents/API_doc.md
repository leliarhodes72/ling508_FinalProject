# API Documentation

The API in my project allows users to retrieve information about the 22 Major Arcana Tarot cards. Users can request detailed information about any specific card by selecting the card's name. The API will return details such as the card's description, meanings (upright and reversed), numerology, element, and astrological body.


## Retrieve Card Information

You can retrieve information about a specific Tarot card using the "Get Tarot Card by Name" endpoint. For example, to get information about "The Fool," you would make a GET request to the following endpoint:

```
GET http://localhost:5000/tarot_card/The Fool
```

### Example Response 

```
{
  "id": 1,
  "name": "The Fool",
  "description": "The Fool depicts a youth walking joyfully into the world...",
  "upright_meaning": "beginnings, freedom, innocence, originality, adventure, idealism, spontaneity",
  "reversed_meaning": "reckless, careless, distracted, naive, foolish, gullible, stale, dull",
  "keyword": "risk",
  "numerology": "Zero",
  "element": "Air",
  "astrological_body": "Uranus"
}
```
