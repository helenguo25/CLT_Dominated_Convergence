# Dominated Convergence Theorem

This Streamlit application illustrates the Dominated Convergence Theorem, a fundamental concept in mathematical analysis that concerns the interchangeability of taking limits and integration under certain conditions.

## Introduction

The Dominated Convergence Theorem is introduced as a mathematical principle that facilitates the swapping of two crucial mathematical operations: taking limits and performing integrals.

## Explanation

- **Overview:** The theorem is explained as a rule that governs how a sequence of functions can converge to another function under the supervision of a "dominating" function.
- **Pointwise Convergence:** It describes how, as we observe each function in the sequence individually, they progressively resemble the target function more closely.
- **Dominating Function:** A function is introduced as a "parent" function that acts as an upper bound for the absolute values of the sequence of functions. This function must also be integrable.
- **The Theorem's Assertion:** The theorem asserts that under these conditions, the order of taking limits and integration can be interchanged.

## Simple Example

- A simple example (of a bounded sequence of functions; a subset of types of functions that satisfy the dominated convergence theorem) involving \(f_n(x) = \frac{\cos(nx)}{n}\) on the interval \([0,3]\) is provided. 

## How to Launch:

1. **Install Streamlit:** If you haven't already, install Streamlit by running:

   pip install streamlit

3. **Download the Script:** Copy the provided code into a Python script file (e.g., `clt_proof_detail.py`).

4. **Launch the App:** Run the Streamlit app by executing the following commands in your terminal:

   streamlit run clt_proof_detail.py

## Screencast:
![](screencast.gif)
