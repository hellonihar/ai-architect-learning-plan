"""
Tests for capstone orchestrator.
"""

import pytest
from src.orchestrator import SupervisorAgent


class TestSupervisor:
    def setup_method(self):
        self.supervisor = SupervisorAgent()

    def test_classify_rag_query(self):
        result = self.supervisor.classify("What is the company policy on remote work?")
        assert result == "rag"

    def test_classify_code_query(self):
        result = self.supervisor.classify("Write a Python function to sort a list")
        assert result == "code"

    def test_classify_general_query(self):
        result = self.supervisor.classify("Hello, how are you?")
        assert result == "general"

    def test_run_returns_string(self):
        result = self.supervisor.run("What is RAG?")
        assert isinstance(result, str)
        assert len(result) > 0
