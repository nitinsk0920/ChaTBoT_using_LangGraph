from langgraph.graph import StateGraph, START, END
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
from typing import TypedDict, Annotated
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.messages import BaseMessage,HumanMessage
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.prompts import PromptTemplate
from langgraph.graph.message import add_messages



load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="zai-org/GLM-5",
     task="text-generation",
)
model = ChatHuggingFace(llm=llm)

class Chatbotstate(TypedDict):

    messages:Annotated[list[BaseMessage], add_messages]


def chat_node(state:Chatbotstate):
     messages = state['messages']
     out=model.invoke(messages)
     return {"messages":[out]}

checkpnt=InMemorySaver()

graph=StateGraph(Chatbotstate)

graph.add_node("chat_node", chat_node)

graph.add_edge(START,"chat_node")
graph.add_edge("chat_node", END)

chatbot=graph.compile(checkpointer=checkpnt)
