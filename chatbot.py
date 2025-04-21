# Imports
from typing import Dict, TypedDict
from langgraph.graph import StateGraph, END
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.runnables.graph import MermaidDrawMethod
from IPython.display import display, Image

# Define the state structure
class State(TypedDict):
    query: str
    category: str
    sentiment: str
    response: str

# Use local Mistral model via Ollama
llm = ChatOllama(model="mistral", temperature=0)

# Node functions
def categorize(state: State) -> State:
    prompt = ChatPromptTemplate.from_template(
        "Categorize the following customer query into one of these categories: "
        "Technical, Billing, General. Query: {query}"
    )
    chain = prompt | llm
    category = chain.invoke({"query": state["query"]}).content.strip()
    return {**state, "category": category}

def analyze_sentiment(state: State) -> State:
    prompt = ChatPromptTemplate.from_template(
        "Analyze the sentiment of the following customer query. "
        "Respond with either 'Positive', 'Neutral', or 'Negative'. Query: {query}"
    )
    chain = prompt | llm
    sentiment = chain.invoke({"query": state["query"]}).content.strip()
    return {**state, "sentiment": sentiment}

def handle_technical(state: State) -> State:
    prompt = ChatPromptTemplate.from_template(
        "Provide a technical support response to the following query: {query}"
    )
    chain = prompt | llm
    response = chain.invoke({"query": state["query"]}).content.strip()
    return {**state, "response": response}

def handle_billing(state: State) -> State:
    prompt = ChatPromptTemplate.from_template(
        "Provide a billing support response to the following query: {query}"
    )
    chain = prompt | llm
    response = chain.invoke({"query": state["query"]}).content.strip()
    return {**state, "response": response}

def handle_general(state: State) -> State:
    prompt = ChatPromptTemplate.from_template(
        "Provide a general support response to the following query: {query}"
    )
    chain = prompt | llm
    response = chain.invoke({"query": state["query"]}).content.strip()
    return {**state, "response": response}

def escalate(state: State) -> State:
    return {**state, "response": "This query has been escalated to a human agent due to its negative sentiment."}

def route_query(state: State) -> str:
    if state["sentiment"] == "Negative":
        return "escalate"
    elif state["category"] == "Technical":
        return "handle_technical"
    elif state["category"] == "Billing":
        return "handle_billing"
    else:
        return "handle_general"

# Build the graph
graph_builder = StateGraph(State)

graph_builder.add_node("categorize", categorize)
graph_builder.add_node("analyze_sentiment", analyze_sentiment)
graph_builder.add_node("handle_technical", handle_technical)
graph_builder.add_node("handle_billing", handle_billing)
graph_builder.add_node("handle_general", handle_general)
graph_builder.add_node("escalate", escalate)

graph_builder.set_entry_point("categorize")
graph_builder.add_edge("categorize", "analyze_sentiment")
graph_builder.add_conditional_edges("analyze_sentiment", route_query, {
    "handle_technical": "handle_technical",
    "handle_billing": "handle_billing",
    "handle_general": "handle_general",
    "escalate": "escalate"
})
graph_builder.add_edge("handle_technical", END)
graph_builder.add_edge("handle_billing", END)
graph_builder.add_edge("handle_general", END)
graph_builder.add_edge("escalate", END)

app = graph_builder.compile()

def run_customer_support(query: str) -> Dict[str, str]:
    results = app.invoke({"query": query})
    return {
        "category": results["category"],
        "sentiment": results["sentiment"],
        "response": results["response"]
    }
