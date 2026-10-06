<p align="center">
  <img src="assets/architecture.svg" alt="Layered application architecture icon" width="170">
</p>

<h1 align="center">Architecture Lessons</h1>

<p align="center">
  <img alt="Python 3.12+" src="https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white">
  <img alt="FastAPI" src="https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi&logoColor=white">
  <img alt="Architecture study" src="https://img.shields.io/badge/focus-layered%20architecture-8250DF">
</p>

> A small FastAPI project for studying separation between routes, services, and repositories.

The project sketches an order flow and a health-check route. It is a learning example; the order implementation and database integration are still in progress.

## Usage

### Requirements

- Python 3.12 or newer
- uv
- PostgreSQL and a DATABASE_URL value

### Set up and run

From this directory, set DATABASE_URL to a PostgreSQL connection string, install dependencies, then start the development server:

<pre><code>export DATABASE_URL="postgresql://USER:PASSWORD@localhost:5432/DATABASE"
uv sync
uv run fastapi dev main.py</code></pre>

Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for the generated API docs.

## Routes

| Method | Route | Current behavior |
| --- | --- | --- |
| GET | /api/healthy | Returns a health status. |
| POST | /api/orders/ | Draft order route that delegates to the order service. The current flow still needs implementation and database validation. |

## Architecture

- app/healthy/routes.py contains the health-check endpoint.
- app/orders/routes.py defines the order endpoint.
- app/orders/service.py contains business-flow orchestration.
- app/orders/repository.py contains database-query code.
- app/core/connections/database.py creates PostgreSQL connections.

## Current limitations

- Order confirmation and repository code are not yet verified end to end.
- A database URL is read during application import, so configure it before starting the server.
- There is no migration or database schema included yet.
