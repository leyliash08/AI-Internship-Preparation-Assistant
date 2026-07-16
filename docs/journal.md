# Development Journal

## Day 1 – Project Setup

### Goal

Set up the project structure and prepare the frontend environment.

### Completed tasks

- Created the project repository
- Initialized Git
- Created the Vue project using Vite
- Installed project dependencies with npm
- Started the development server
- Learned the basic Vue project structure
- Replaced the default Vue page with a custom homepage
- Created the first textarea and Analyze button
- Added initial CSS styling
- Created the first Git commits

### Technologies

- Vue.js
- Vite
- HTML
- CSS
- JavaScript
- Git

### Learned and revised

- Vue project structure
- App.vue
- Template
- Style
- Running the development server
- Git commit workflow

## Day 2 – Frontend Development

### Goal

Redesign the project idea and build an interactive frontend for the AI Internship Preparation Assistant.

### Project Update

Originally, the project was planned as an **AI Business Requirements Assistant**.

The concept was changed to **AI Internship Preparation Assistant**, which analyzes a student's current skills and generates a personalized learning roadmap for internship preparation.

### Completed Tasks

- Renamed the project to **AI Internship Preparation Assistant**
- Updated the application title and description
- Redesigned the user interface for the new project idea
- Added an internship goal input form
- Implemented a textarea with a character counter
- Added form validation for empty input
- Created **Clear** and **Generate Learning Plan** buttons
- Implemented reactive data using `ref` and `computed`
- Added dynamic rendering with `v-for`
- Added conditional rendering with `v-if`
- Created reusable result cards
- Designed four preparation categories:
  - Required Skills
  - Learning Plan
  - Skill Gaps
  - Next Steps
- Added responsive CSS styling
- Created a new Git commit and pushed the changes to GitHub

### Vue Concepts Practiced

- `ref`
- `computed`
- `v-model`
- `v-for`
- `v-if`
- Event handling with `@click`
- Reactive state management
- Component styling with scoped CSS

### Current Status

The frontend interface is completed.

The application already supports:

- User input
- Character counting
- Form validation
- Dynamic result cards
- Responsive layout

The next step is to build the backend with FastAPI, connect the OpenAI API, and store generated learning plans in an SQLite database.

### Technologies Used

- Vue.js
- JavaScript
- HTML
- CSS
- Git

## Day 3 – Backend Development and AI Integration

### Goal

Connect the frontend to the backend and integrate the OpenAI API.

### Completed Tasks

- Created the FastAPI backend.
- Installed FastAPI, Uvicorn, OpenAI and python-dotenv.
- Created the POST /analyze endpoint.
- Connected the backend to the OpenAI API.
- Stored the API key in a .env file.
- Added .env to .gitignore.
- Configured CORS for frontend communication.
- Connected the Vue frontend to the backend using fetch().
- Parsed the AI response and displayed the generated learning plan in the interface.
- Tested the application using Swagger UI and the frontend.

### What I Learned

- How REST APIs work with FastAPI.
- How to use environment variables.
- How to connect a Vue frontend to a Python backend.
- How to send POST requests using fetch().
- How to process JSON responses from an AI API.

### Result

The application successfully generates an AI-powered internship preparation plan from the user's input.