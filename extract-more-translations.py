import re
from pathlib import Path

html_file = Path('./skosmos/custom-templates/library-header/lh-all-lang.html')
content = html_file.read_text(encoding='utf-8')

# Extract title attributes which contain translations
translations = {
    'en': {},
    'fr': {},
    'es': {},
    'ru': {},
    'ar': {},
    'zh': {}
}

# Find navbar-brand text (top banner)
brand_matches = re.findall(r'<a class="navbar-brand"[^>]*>([^<]+)</a>', content)
print("Navbar Brand Translations:")
for i, match in enumerate(brand_matches):
    lang = ['en', 'fr', 'ru', 'es', 'ar', 'zh'][i % 6]
    print(f"{lang}: {match.strip()}")

print("\n" + "="*60)

# Find all menu link texts
menu_matches = re.findall(r'<a href="[^"]*"[^>]*>([^<]+)</a>', content)
print(f"\nFound {len(menu_matches)} menu items")

# Group them by detecting language context
sections = re.split(r'<header[^>]*id="navbar"', content)
for idx, section in enumerate(sections[1:]):
    # Try to detect language
    if '/en/' in section:
        lang = 'en'
    elif '/fr/' in section:
        lang = 'fr'
    elif '/ru/' in section:
        lang = 'ru'
    elif '/es/' in section:
        lang = 'es'
    elif '/ar/' in section:
        lang = 'ar'
    elif '/zh/' in section:
        lang = 'zh'
    else:
        continue
    
    items = re.findall(r'<a[^>]*>([^<]+)</a>', section)
    print(f"\n=== {lang.upper()} Menu Items ===")
    for item in items:
        text = item.strip()
        if text and len(text) > 3 and '»' not in text:
            print(f"  {text}")