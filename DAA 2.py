import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(page_title="Bank Fraud Monitoring", layout="wide")

st.title("🏦 Bank Transaction Fraud Monitoring")
st.write("### Demonstration of Three Nested Loops")

# -----------------------------------
# Sidebar
# -----------------------------------
st.sidebar.header("Simulation Settings")

customers = st.sidebar.slider("Customers", 2, 20, 5)
transactions = st.sidebar.slider("Transactions per Customer", 2, 20, 5)
checks = st.sidebar.slider("Security Checks", 2, 20, 5)

# -----------------------------------
# Run Button
# -----------------------------------
if st.button("Run Monitoring"):

    st.subheader("Customer Database")

    customer_data = []

    for i in range(customers):
        customer_data.append({
            "Customer ID": f"CUST-{1001+i}",
            "Account Balance": np.random.randint(5000, 100000),
            "Account Type": np.random.choice(["Savings", "Current"])
        })

    df = pd.DataFrame(customer_data)

    st.dataframe(df, use_container_width=True)

    progress = st.progress(0)

    report = []

    operations = 0

    fraud_count = 0

    start = time.time()

    # -------------------------------
    # Three Nested Loops
    # -------------------------------
    for i in range(customers):

        customer = df.iloc[i]

        suspicious = False

        for j in range(transactions):

            amount = np.random.randint(100, 100000)

            for k in range(checks):

                score = np.random.randint(1, 100)

                operations += 1

                if amount > 80000 and score > 70:
                    suspicious = True

        if suspicious:
            fraud_count += 1

        report.append({
            "Customer": customer["Customer ID"],
            "Balance": customer["Account Balance"],
            "Result": "⚠ Fraud Alert" if suspicious else "✅ Safe"
        })

        progress.progress((i + 1) / customers)

    end = time.time()

    result = pd.DataFrame(report)

    st.subheader("Fraud Detection Result")

    st.dataframe(result, use_container_width=True)

    # -----------------------------------
    # Metrics
    # -----------------------------------
    st.subheader("Performance Analysis")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Operations", operations)
    col2.metric("Fraud Alerts", fraud_count)
    col3.metric("Execution Time", f"{end-start:.6f} sec")
    col4.metric("Space Used", customers + transactions + checks)

    st.success("Fraud Monitoring Completed Successfully!")

    st.divider()

    # -----------------------------------
    # Graph
    # -----------------------------------
    st.subheader("Operations Growth")

    x = []
    y = []

    for n in range(1, customers + 1):
        x.append(n)
        y.append(n * transactions * checks)

    graph = pd.DataFrame({
        "Customers": x,
        "Operations": y
    })

    fig = px.bar(
        graph,
        x="Customers",
        y="Operations",
        color="Operations",
        title="Growth of Three Nested Loops"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # -----------------------------------
    # Pie Chart
    # -----------------------------------
    safe = customers - fraud_count

    pie = pd.DataFrame({
        "Status": ["Safe", "Fraud"],
        "Count": [safe, fraud_count]
    })

    fig2 = px.pie(
        pie,
        values="Count",
        names="Status",
        title="Fraud Distribution"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.divider()

    # -----------------------------------
    # Complexity
    # -----------------------------------
    st.subheader("Algorithm Complexity")

    st.code("""
for each Customer:
    for each Transaction:
        for each Security Check:
            Analyze Transaction
""")

    st.markdown("""
### Time Complexity

**O(Customers × Transactions × Security Checks)**

The algorithm visits every customer.

For every customer it checks every transaction.

For every transaction it performs all security checks.

Therefore,

**Time Complexity = O(n³)** (when all three inputs grow together)

---

### Space Complexity

The program stores only customer information and final results.

**Space Complexity = O(n)**

---

### Total Operations

Operations = Customers × Transactions × Security Checks
""")