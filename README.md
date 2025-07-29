# AI-Powered Content Generation

This project is a content generation system that creates posts based on deep research of a given topic.

## 1. The Problem

Manually creating high-quality, well-researched content is a time-consuming process. It involves gathering information from multiple sources, synthesizing it, and then writing a coherent post. This project aims to automate this process.

## 2. The Solution

This application uses a combination of AI agents and a modern tech stack to automate content creation.

### Tech Stack

*   **Backend:** Python, FastAPI, LangGraph
*   **Frontend:** React, TypeScript, Vite
*   **Search:** Tavily AI
*   **Database:** MongoDB
*   **Containerization:** Docker

### Workflow

1.  **User Input:** The user provides a topic for the post.
2.  **User Clarification:** If the system needs more information or the user's request is ambiguous, it will ask for clarification.
3.  **Research Orchestration:** A set of AI agents using LangGraph plans and executes research on the topic.
    *   It breaks down the main topic into sub-topics.
    *   It uses a search engine (Tavily) to find relevant information for each sub-topic.
    *   It reads and compresses the content from search results.
4.  **Content Generation:** The system uses the research to generate a draft of the post.
5.  **Final Post:** A final post is generated based on the research and any clarifications.

## 3. Setup

To run this project locally, follow these steps:

1.  **Environment Variables:**
    *   There is a `.env.example` file in the `deep-scribe` directory. Copy it to a new file named `.env`.
    *   Adjust the environment variables in the `.env` file as needed for your setup (e.g., API keys for Tavily and OpenRouter).

2.  **Run the application:**
    *   Make sure you have Docker installed and running.
    *   Open your terminal in the project root and run the following command:
        ```bash
        make run
        ```
    This command will build and start all the necessary services using `docker-compose`.

## 4. Access

Once the application is running, you can access the web interface at:

[http://localhost:3000](http://localhost:3000)
