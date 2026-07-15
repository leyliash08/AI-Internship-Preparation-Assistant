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