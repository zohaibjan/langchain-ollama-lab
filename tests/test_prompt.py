import unittest

from langchain_core.runnables import RunnableLambda

from ice_breaker import build_chain


class PromptTests(unittest.TestCase):
    def test_prompt_and_parser_without_ollama(self):
        received = []
        def respond(prompt):
            received.append(prompt.to_string())
            return "A synthetic summary."
        answer = build_chain(RunnableLambda(respond)).invoke({"information": "A fictional engineer builds sensors."})
        self.assertEqual(answer, "A synthetic summary.")
        self.assertIn("A fictional engineer builds sensors.", received[0])
        self.assertIn("supported by the supplied text", received[0])

    def test_missing_required_information(self):
        chain = build_chain(RunnableLambda(lambda prompt: "unused"))
        with self.assertRaises(KeyError):
            chain.invoke({})
