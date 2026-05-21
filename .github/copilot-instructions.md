# Copilot instructions

## Build and run
- Local dev: `docker compose -f compose.yaml.local watch` (serves http://localhost:9090/skosmos-dev/)
- Build images: `docker build -f Dockerfile.local .`, `docker build -f Dockerfile.dev .`, `docker build -f Dockerfile.prod .`

## High-level architecture
- Docker builds clone upstream `NatLibFi/Skosmos` (v3.0), install composer/npm deps, then overlay this repo’s customizations from `./skosmos/` and a `config.ttl.*` file.
- Environment configuration lives in `config.ttl.{local,dev,prod}` and is copied into the container as `config.ttl` to drive SPARQL endpoints, baseHref, languages, and vocabularies.
- UI customizations are Twig overrides and assets under `skosmos/`, with `skosmos/src/view/base-template.twig` and `scripts.inc.twig` overriding upstream view behavior.
- Deployments are GitHub Actions workflows that build Docker images and deploy to ECS on pushes to `main` (dev) or release tags (prod).

## Key conventions
- Use `config.ttl.local` for prototyping, `config.ttl.dev` for dev deployment, and `config.ttl.prod` for production; keep `skosmos:baseHref` aligned with the target instance.
- Template overrides live in `skosmos/custom-templates/` (notably `about/`, `footer/`, `html-head/`, and `library-header/`). `library-header.twig` is also wired via `skosmos/src/view/base-template.twig`.
- `footer.twig` and `library-header.twig` include their own CSS to support localization.
- CSS lives in `skosmos/resource/css/` (`custom.css` for local overrides, `skosmos.css` for global styling).
