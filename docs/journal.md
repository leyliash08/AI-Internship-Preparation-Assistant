# Development Journal

## Day 1 – Project Setup

I studied the system provided by the professor and tried to understand how the frontend, backend, OpenAI API, database, and Git repository should work together.

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

## Day 4 – Database Integration and Analysis History API

### Goal

Add persistent data storage to the backend and create an API endpoint for retrieving previous analyses.

### Completed Tasks

- Installed and configured SQLAlchemy.
- Created an SQLite database for storing internship analyses.
- Created the database connection and session configuration.
- Created a database model for saved analyses.
- Updated the POST `/analyze` endpoint.
- Added automatic saving of generated AI responses to the database.
- Created the GET `/analyses` endpoint.
- Configured the endpoint to return saved analyses ordered from newest to oldest.
- Tested the database integration using Swagger UI.
- Verified that generated analyses were successfully stored in SQLite.
- Fixed backend import and indentation errors.

### What I Learned

- How to connect FastAPI to an SQLite database.
- How SQLAlchemy models work.
- How to create and manage database sessions.
- How to save API results in a database.
- How to retrieve database records through a GET endpoint.
- How to debug backend import and indentation errors.

### Result

The backend can now permanently store every generated internship preparation analysis.

Saved analyses can also be retrieved through the `/analyses` endpoint, which makes it possible to build a history feature in the frontend.

## Day 5 – Frontend History Feature and Final Testing

### Goal

Display saved analyses in the frontend and allow users to reopen previous learning plans.

### Completed Tasks

- Added the `loadHistory()` function to the Vue frontend.
- Connected the frontend to the GET `/analyses` endpoint.
- Loaded saved analyses automatically using `onMounted()`.
- Created the **Previous Analyses** section.
- Displayed saved internship goals in the history list.
- Added a **Refresh History** button.
- Created the `openAnalysis()` function.
- Added functionality for reopening a saved analysis.
- Restored saved result cards when a history item was selected.
- Added automatic history updates after generating a new analysis.
- Added smooth scrolling to the result section.
- Added CSS styling for the history cards.
- Tested the **Clear** button.
- Verified that the form and result cards are cleared correctly.
- Checked the `requirements.txt` file.
- Performed final frontend and backend testing.

### What I Learned

- How to fetch saved data from a backend API.
- How to use `onMounted()` in Vue.
- How to update reactive arrays with API data.
- How to restore previously saved content in the interface.
- How to refresh frontend data after a new database record is created.
- How to test a complete full-stack application.

### Result

The application now provides a complete analysis history feature.

Users can generate new internship preparation plans, save them in the SQLite database, view previous analyses, refresh the history, and reopen saved learning plans without generating them again.