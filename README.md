# Movie Management System (DDD Example in Python)

This project is a Python-based implementation of a **Domain-Driven Design (DDD)** approach for managing movies. It demonstrates how to separate domain logic from infrastructure concerns, focusing on clean architecture principles.

## What is Domain-Driven Design (DDD)?

DDD is a software design approach that emphasizes collaboration between domain experts and developers to create a model that reflects the business domain. It focuses on:

- **Entities**: Objects with a unique identity (e.g., `Movie`).
- **Value Objects**: Immutable objects that describe aspects of the domain (e.g., `MovieRating`).
- **Aggregates**: Groups of entities and value objects treated as a single unit.
- **Repositories**: Abstractions for accessing and storing aggregates.
- **Services**: Operations that don't naturally fit within entities or value objects.
- **Domain Events**: Notifications about something that happened in the domain.

## Project Structure

The project is organized into the following components:

### **Domain**
Contains the core business logic:
- [x] `entities/`: Defines the main entities (e.g., `Movie`).
- [x] `value_objects/`: Defines value objects (e.g., `MovieRating`).
- [ ] `services/`: Contains domain services for complex operations.
- [ ] `events/`: Defines domain events (future implementation).

### **Application**
Coordinates use cases and application logic:
- [ ] `commands/`: Handles user actions or requests (future implementation).
- [ ] `queries/`: Handles data retrieval (future implementation).

### **Infrastructure**
Handles technical concerns like persistence:
- [x] `repositories/`: Implements data storage for aggregates (e.g., `MovieRepository`).
- [x] `mappers/`: Maps domain models to database tables (e.g., `MovieMapper`, `MovieTable`).
- [x] `database.py`: Manages database initialization and session handling.

### **Interfaces**
Exposes the application to the outside world:
- [ ] `api/`: RESTful or CLI interfaces for interacting with the system (future implementation).

## Features

- **Movie Management**:
  - Manage movies using the `Movie` entity.
  - Encapsulate core business rules within the `Movie` entity.
- **Rating Management**:
  - Manage movie ratings using the `MovieRating` value object.
  - Ensure immutability and validation of ratings.
- **Persistence**:
  - Store and retrieve movies using a repository pattern.
  - Use `SQLModel` and SQLite for database persistence.
- **Separation of Concerns**:
  - Keep domain logic independent of infrastructure concerns using mappers.

## How to Run the Project

### **1. Set Up the Environment**
Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Run the Application
Execute the main script to add and retrieve movies:
```bash
python main.py
```

### Running Tests
Run the test suite to ensure everything is working:
```bash
pytest
```

