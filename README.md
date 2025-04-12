# Movie Management System (Very simple example of DDD with Python)

This project is a Python-based implementation of a **Domain-Driven Design (DDD)** approach for managing movies. The system is designed to demonstrate the principles of DDD, focusing on separating the domain logic from infrastructure concerns.

## What is Domain-Driven Design (DDD)?

DDD is a software design approach that emphasizes collaboration between domain experts and developers to create a model that reflects the business domain. It focuses on:

- **Entities**: Objects with a unique identity.
- **Value Objects**: Immutable objects that describe aspects of the domain.
- **Aggregates**: Groups of entities and value objects treated as a single unit.
- **Repositories**: Abstractions for accessing and storing aggregates.
- **Services**: Operations that don't naturally fit within entities or value objects.
- **Domain Events**: Notifications about something that happened in the domain.

## Project Structure (DRAFT)

The project is organized into the following components:

- **Domain**: Contains the core business logic.
    - `entities/`: Defines the main entities (e.g., `Movie`).
    - `value_objects/`: Defines value objects (e.g., `Genre`, `Rating`).
    - `services/`: Contains domain services for complex operations.
    - `events/`: Defines domain events.
- **Application**: Coordinates use cases and application logic.
    - `commands/`: Handles user actions or requests.
    - `queries/`: Handles data retrieval.
- **Infrastructure**: Handles technical concerns like persistence.
    - `repositories/`: Implements data storage for aggregates.
    - `adapters/`: Integrates with external systems (e.g., databases, APIs).
- **Interfaces**: Exposes the application to the outside world.
    - `api/`: RESTful or CLI interfaces for interacting with the system.

## Features

- Manage movie rating using the `MovieRating` value object.
- Manage movies using `Movie` entity
- Encapsulated core business rules by defining `Movie` as an entity and `MovieRating` as value objects, ensuring a clear separation of concerns


## Running Tests

Run the test suite to ensure everything is working:
```bash
pytest
```

