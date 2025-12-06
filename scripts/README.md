# Google Images Scraper

⚠️ **ATTENTION : Ce script est obsolète et ne fonctionne plus avec la version actuelle de Google Images.**

## Problèmes connus

1. Les classes CSS ont changé (`rg_i Q4LuWd` n'existe plus)
2. Google a modifié la structure HTML de son interface
3. Selenium 3.x est obsolète (utiliser Selenium 4.x)

## Alternatives recommandées

### API gratuites/open-source
- **Unsplash API** : https://unsplash.com/developers
- **Flickr API** : https://www.flickr.com/services/api/
- **Bing Image Search API** : https://www.microsoft.com/en-us/bing/apis/bing-image-search-api

### Outils modernes
- **google-images-download** : package Python alternatif
- **icrawler** : framework de scraping d'images

## Usage historique (ne fonctionne plus)

```bash
python scraper.py "wolf" 100
```

Arguments :
- `searchterm` : terme de recherche
- `scroll_nums` : nombre de scrolls pour charger plus d'images

## Migration vers Selenium 4.x

Si vous souhaitez adapter ce scraper :

1. Installer Selenium 4.x : `pip install selenium>=4.15.0`
2. Utiliser WebDriver Manager : `pip install webdriver-manager`
3. Mettre à jour le code :

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
```

4. Inspecter la nouvelle structure HTML de Google Images pour trouver les nouveaux sélecteurs
