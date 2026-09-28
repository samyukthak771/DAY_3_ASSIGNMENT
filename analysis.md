# Day 1 Task – From Prompt to Action

## 1. Scenario

The scenario chosen for this task is a simple question-answering and calculation scenario.

The questions are given to an LLM. Some questions can be answered directly using the model's knowledge, while mathematical questions can be handled using an external calculator tool.

The purpose is to compare the behavior of a plain LLM with an LLM that has access to a single external tool.

---

## 2. What is an LLM?

A Large Language Model (LLM) is a model that can understand and generate human-like text.

In this task, the LLM receives a question from the user and produces an answer.

For example:

> What is the capital of France?

The LLM can answer this directly:

> Paris.

However, when a question requires a calculation, an external tool can be used instead of relying only on the model's internal knowledge.

---

## 3. What is an Agent?

An agent is a system that uses an LLM to decide what action should be taken to solve a task.

An agent can receive a user's request, decide whether a tool is required, call the appropriate tool, and use the tool's result.

In this task, the agent has access to one calculator tool.

---

## 4. What is a Tool?

A tool is an external function or capability that an LLM can use to perform a specific task.

The tool created for this project is a calculator function.

The calculator accepts a mathematical expression and returns the calculated result.

The tool is defined in:

`tools.py`

Example:

```text
calculator("15/100*18000")