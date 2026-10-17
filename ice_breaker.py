"""Small local Ollama summarisation exercise; importing does not call a model."""
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

information = """
Elon Reeve Musk FRS (/ˈiːlɒn/; born June 28, 1971) is a businessman and investor known for his key roles in the space company SpaceX and the automotive company Tesla, Inc. Other involvements include ownership of X Corp., the company that operates the social media platform X (formerly known as Twitter), and his role in the founding of The Boring Company, xAI, Neuralink, and OpenAI. He is one of the wealthiest individuals in the world; as of August 2024 Forbes estimates his net worth to be US$241 billion.[3]
"""

SUMMARY_TEMPLATE = """Given this information about a person:
{information}

Return:
1. A short summary.
2. Two interesting facts supported by the supplied text.
"""


def build_chain(model=None):
    """Allow a local model or a fake runnable for offline regression checks."""
    prompt = PromptTemplate.from_template(SUMMARY_TEMPLATE)
    if model is None:
        from langchain_ollama import ChatOllama

        model = ChatOllama(temperature=0, model="mistral")
    return prompt | model | StrOutputParser()


def main():
    load_dotenv()
    print(build_chain().invoke({"information": information}))


if __name__ == "__main__":
    main()
