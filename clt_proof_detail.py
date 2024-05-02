import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def dominated_convergence_theorem():
    st.title("Dominated Convergence Theorem")

    st.write(
        "The Dominated Convergence Theorem is like a special rule in math that helps us understand "
        "how we can switch the order of two important operations: taking limits and doing integrals."
    )

    st.subheader("Explanation:")
    st.write(
        "Imagine we have a bunch of functions, $f_n(x)$, and they're all kind of jumbled up. "
        "But as we look at them one by one (for each $n$), they start to look more and more like "
        "another function, $f(x)$. This is what we call 'converging pointwise.'"
    )
    st.write(
        "Now, imagine there's another function, $g(x)$, that's a bit like a parent keeping our functions in check. "
        "It's always bigger or equal to the absolute value of any of our $f_n(x)$ functions at any point. This $g(x)$ function "
        "is also something we can find the area under, or 'integrate.'"
    )
    st.write(
        "If we have all these conditions, then the Dominated Convergence Theorem tells us something cool: "
        "if our $f_n(x)$ functions are 'pointwise' getting closer to $f(x)$, and they're always "
        "'dominated' by $g(x)$, then we can switch the order of two actions:"
    )
    st.markdown("1. We can first take the limit of these functions $f_n(x)$ as $n$ goes to infinity.")
    st.markdown("2. Then, we can do the integral of this limit function $f(x)$.")

    st.subheader("Simple Example of a Sequence Bounded Above and Below:")
    st.write(
        "Let's consider the example of the sequence of functions $f_n(x) = \\frac{{\cos(nx)}}{{n}}$ on the interval [0,3]. "
        "Notice 1 is always bigger or equal to the absolute value of any of our functions at any point. "
        "Hence, our sequence of functions is dominated by the function 1 which is integrable in [0,3]."
    )
    st.write(
        "As you can see in the plot below, each function $f_n(x)$ oscillates around the x-axis, with the "
        "amplitude decreasing as $n$ increases. As we look at them one by one (for each $n$) "
        "they get closer and closer to the zero function. Hence, the limit of the integral of the sequence "
        "is the integral of the zero function which is 0.")

    st.subheader("Visualization:")
    x = np.linspace(0, 3, 400)
    f_n = lambda n: np.sin(n*x) / n
    f = np.zeros_like(x)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, f, label=r'$f(x) = 0$', color='blue')
    for n in range(1, 6):
        ax.plot(x, f_n(n), label=f'$f_{n}(x) = \\frac{{\cos({n}x)}}{{{n}}}$', linestyle='--')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title('Sequence of Functions Converging to f(x)')
    ax.legend()
    st.pyplot(fig)

dominated_convergence_theorem()
