# crew.py
# PURPOSE: Assemble agents + tasks into a crew and run it

import os
from dotenv import load_dotenv
from crewai import Crew, Process

from agents import create_researcher, create_analyst, create_writer
from tasks import create_research_task, create_analysis_task, create_writing_task

# Load environment variables
load_dotenv(override=True)


def build_crew(topic: str, search_context: str) -> Crew:
    """
    Build and return a CrewAI crew for the given topic.

    Pipeline: Researcher → Analyst → Writer (sequential)
    """
    # Create agents
    researcher = create_researcher()
    analyst = create_analyst()
    writer = create_writer()

    # Create tasks (sequential pipeline with context chaining)
    research_task = create_research_task(researcher, topic, search_context)
    analysis_task = create_analysis_task(analyst, topic, context=[research_task])
    writing_task = create_writing_task(writer, topic, context=[research_task, analysis_task])

    # Assemble the crew
    crew = Crew(
        agents=[researcher, analyst, writer],
        tasks=[research_task, analysis_task, writing_task],
        process=Process.sequential,
        verbose=True,
    )

    return crew


def run_crew(topic: str, search_context: str) -> str:
    """Build and execute the crew for the given topic."""
    crew = build_crew(topic, search_context)
    result = crew.kickoff()
    return str(result)


# Quick terminal test
if __name__ == "__main__":
    from tools import perform_web_search, format_search_results
    topic = input("Enter research topic: ")
    print("🔍 Searching the web for live data...")
    raw_results = perform_web_search(topic)
    context = format_search_results(raw_results)
    report = run_crew(topic, context)
    print("\n" + "="*50)
    print("📄 FINAL REPORT")
    print("="*50)
    print(report)