# metadata.un.org SKOSMOS
This repository contains SKOSMOS customizations and deployment tools for the SKOSMOS instances running at metadata.un.org

To get started developing, you can:

`git clone https://github.com/dag-hammarskjold-library/mdu-skosmos.git`
`cd mdu-skosmos`
`docker compose -f compose.yaml.local watch`

You can then make changes to the files in the repository and view the result at http://localhost:9090/skosmos-dev/

When you want to deploy changes, create a branch, save your changes, and issue a PR that includes the changes. 

## Workflows and deployment

Merging to main will trigger a build of the Docker image, which will then be deployed to ECS as a dev/uat server.

Creating a release will build the image for that release tag and deploy it to ECS as a production server.

## File descriptions

### 000-default.conf

### config.ttl.*
Contains the configuration for the available vocabularies. Update the .local version for prototyping, .dev for the dev deployment, and .prod for production.

### Dockerfile.*
Instructions to containerize the application. For local development and prototyping, use the .local file. For deployment, use the .dev version for your cloud based prototyping and testing, and the .prod version to update the production site.

### docker-compose.yaml.local
Serves as the basis for a Docker Compose configuration that can be used in local development.

### .github/workflows/deploy-*.yml
Contains a set of workflows that are triggered when changes are made to the repository. These workflows will build a Docker image, push it to ECR, and deploy to ECS. The dev workflow is triggered when a PR is merged into main. The production workflow is triggered when a release tag is created.

### ecs/ecs-task-definition.json.template
Template file for ECS task definition. This is filled in by the GitHub Actions in .github/workflows/deploy-dev.yml and .github/workflows/deploy-prod.yml

### skosmos/custom-templates/
Contains custom templates for the SKOSMOS application according to what sections of the page are available for templating. The most pertinent are skosmos/custom-templates/about/about.twig, skosmos/custom-templates/footer/footer.twig, skosmos/html-head/html-head.twig and skosmos/library-header/library-header.twig. 

Note that library-header.twig is also part of a code customization made available via skosmos/src/view/base-template.twig and is not the out of the box configuration.

### skosmos/resource/css
Contains CSS files for SKOSMOS. custom.css can contain additional custom styling, while skosmos.css contains the global styling.

Note: both footer.twig and library-header.twig contain CSS for their own styling. The CSS is included in each to accommodate localization.

### skosmos/resource/fontawesome
Contains additional Font Awesome files that weren't included in the original SKOSMOS distribution.

### skosmos/resource/translations
Contains translation files for SKOSMOS, one per language. TO DO: develop a script to extract untranslated strings from the code and add them to these files, and to copy translation keys from the English file to the other languages.

### skosmos/src/view/base-template.twig
This is a customization of the SKOSMOS base template to accommodate the UN language switcher and Library header. When upgrading SKOSMOS to a new version, check to ensure this file's structure remains unchanged even if there are upstream changes from the base repository.

### skosmos/src/view/scripts.inc.twig
This file manages the script imports for SKOSMOS. Modify it if you need additional JS libraries.