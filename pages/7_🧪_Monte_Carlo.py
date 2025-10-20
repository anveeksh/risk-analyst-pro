
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🧪 Monte Carlo (Basic PML)")

st.write("Estimate distribution of annual loss by simulating many risk scenarios.")

n = st.number_input("Number of simulations", min_value=1000, max_value=200000, value=10000, step=1000)
prob_event = st.slider("Annual probability of event", 0.0, 1.0, 0.3, 0.01)
loss_low = st.number_input("Loss Min ($)", min_value=0, value=10000, step=1000)
loss_high = st.number_input("Loss Max ($)", min_value=1000, value=100000, step=1000)

if st.button("▶️ Run Simulation"):
    outcomes = []
    for _ in range(int(n)):
        if np.random.rand() < prob_event:
            loss = np.random.uniform(loss_low, loss_high)
        else:
            loss = 0.0
        outcomes.append(loss)
    outcomes = np.array(outcomes)
    st.metric("Expected Annual Loss", f"${outcomes.mean():,.0f}")
    st.metric("95th Percentile Loss (PML)", f"${np.percentile(outcomes,95):,.0f}")

    # Histogram (matplotlib, single plot, default colors)
    fig, ax = plt.subplots()
    ax.hist(outcomes, bins=50)
    ax.set_title("Distribution of Simulated Annual Loss")
    ax.set_xlabel("Loss ($)")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)
