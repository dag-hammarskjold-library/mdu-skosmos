# metadata.un.org SKOSMOS
This repository contains SKOSMOS customizations and deployment tools for the SKOSMOS instance running at metadata.un.org

## Workflows and deployment


## File descriptions

### 000-default.conf

### config.ttl.*
Contains the configuration for the available vocabularies. Update the .dev version for prototyping.

### Dockerfile.*
Instructions to containerize the application. For deployment, use the .dev version for your prototyping and testing, 
and the .prod version to update the production site.

### model/sparql/GenericSparql.php
This file contains a fix for an error that prevented remote SPARQL searches against Ontotext GraphDB.

### resource/translations
These are all the translations and translation tools for the site.

#### compile-translations
This script is run inside the Docker container to compile all the translated message strings.

#### skosmos_*.po
These text files contain all of the message strings on the site, as well as their translations in the target language. Update these files and trigger a deploy process to see them live on either dev or prod.