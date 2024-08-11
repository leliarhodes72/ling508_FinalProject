# Tarot Cards

Tarot Cards is a project that allows a user to select one of the 22 Major Arcana tarot cards and will return information regarding said card. The retruns will be as follows: 

 - A description of the card
 - The upright meaning
 - The reversed meaning
 - A related keyword
 - The related astrological body
 - The related numerology
 - The related element

## Example

The user has requested information on the first card in the deck, **The Fool**. 

The API response will be as follows: 

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

The user will see: 

**The Fool**
![The standard Rider-Waite tarot deck 'The Fool' card; it depicts a young man in lavish robes with a bindle (a bag on a stick) in one hand and a flower in the other. He is looking up, ready to depart on a new journey. However, he doesn't see that he is about to walk off a cliff, nor does he heed the dog is at his feet trying to warn him.](https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/RWS_Tarot_00_Fool.jpg/800px-RWS_Tarot_00_Fool.jpg)

- Description: The Fool depicts a youth walking joyfully into the world. He is taking his first steps, and he is exuberant, joyful, excited. He carries nothing with him except a small sack, caring nothing for the possible dangers that lie in his path. Indeed, he is soon to encounter the first of these possible dangers, for if he takes just a step more, he will topple over the cliff that he is reaching. But this doesn't seem to concern him - we are unsure whether he is just naive or simply unaware. The dog at his heels barks at him in warning, and if he does not become more aware of his surroundings soon, he may never see all the adventures that he dreams of encountering.
- Upright Meaning: beginnings, freedom, innocence, originality, adventure, idealism, spontaneity
- Reversed Meaning: reckless, careless, distracted, naive, foolish, gullible, stale, dull
- keyword: risk
- Numerology: 0
- Element: Air
- Astrological Body: Uranus