Here’s a detailed README with comprehensive explanations for the `anime`, `character`, `manga`, and `studio` commands:

```markdown
# Anime/Manga Search Query Generator

This project provides a simple function to generate a GraphQL query for searching anime, manga, characters, or studios using the Anilist API.

## Usage

The main function `search_by_title(command)` returns a GraphQL query string based on the provided command. Here's how to use it:

```
from your_module import search_by_title

# Example command can be 'anime', 'manga', 'character', or 'studio'
query = search_by_title('anime')
```

This query can be used with GraphQL requests to the Anilist API. Example usage:

```python
import requests

url = 'https://graphql.anilist.co'
variables = {
    'search': 'Your search title',
    'type': 'ANIME'  # or 'MANGA', 'CHARACTER', 'STUDIO'
}

response = requests.post(url, json={'query': query, 'variables': variables})
data = response.json()
```


## Command Details

### Anime

Generates a query to fetch information about anime titles. The query retrieves:

- **Title**: Romaji and English versions of the title.
- **Site URL**: URL to the anime's page on Anilist.
- **Type and Format**: Information about whether it is a TV series, movie, OVA, etc.
- **Genres**: List of genres the anime belongs to.
- **Status**: Current status (e.g., airing, completed).
- **Episodes Count**: Total number of episodes.
- **Duration**: Duration of each episode.
- **Description**: Synopsis of the anime.
- **Cover Image URL**: URL to the cover image.
- **Season and Year**: Season and year of release.
- **Start Date**: Date the anime started airing.
- **Average Score and Favorites Count**: Community ratings and the number of users who favorited it.
- **Studios**: Studios involved in production.
- **Hashtag**: Official or popular hashtag.

### Manga

Generates a query to fetch information about manga titles. The query retrieves:

- **Title**: Romaji and English versions of the title.
- **Site URL**: URL to the manga's page on Anilist.
- **Type and Format**: Information about whether it is a manga, novel, etc.
- **Genres**: List of genres the manga belongs to.
- **Status**: Current status (e.g., publishing, completed).
- **Chapters Count**: Total number of chapters.
- **Volumes**: Total number of volumes.
- **Description**: Synopsis of the manga.
- **Cover Image URL**: URL to the cover image.
- **Start Date**: Date the manga started publishing.
- **Average Score and Favorites Count**: Community ratings and the number of users who favorited it.

### Character

Generates a query to fetch information about characters. The query retrieves:

- **Name**: Full and native names of the character.
- **Image URL**: URL to the character's image.
- **Description**: Detailed description of the character.
- **Site URL**: URL to the character's page on Anilist.
- **Media Appearances**: List of anime and manga where the character appears.
- **Favorites Count**: Number of users who favorited the character.

### Studio

Generates a query to fetch information about studios. The query retrieves:

- **Name**: Name of the studio.
- **Site URL**: URL to the studio's page on Anilist.
- **Media Produced**: List of anime titles produced by the studio.
- **Favorites Count**: Number of users who favorited the studio.

## API Response

The Anilist API will return a JSON response containing detailed information about the searched media based on the query structure.

## Example Code

Here's a complete example demonstrating how to use the `search_by_title` function and handle the API response:

```python
import requests

from your_module import search_by_title

# Define the search type and term
search_type = 'anime'  # or 'manga', 'character', 'studio'
search_term = 'Naruto'

# Generate the query
query = search_by_title(search_type)

# Define the request URL and variables
url = 'https://graphql.anilist.co'
variables = {
    'search': search_term,
    'type': search_type.upper()
}

# Send the request to the Anilist API
response = requests.post(url, json={'query': query, 'variables': variables})

# Handle the API response
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")

```

## Note

This function generates a query string only. You need to use it with appropriate GraphQL request handling to fetch data from the Anilist API.
```

This README provides detailed information about how to use the `search_by_title` function, what data each command retrieves, and includes a complete example of making a request and handling the response.
