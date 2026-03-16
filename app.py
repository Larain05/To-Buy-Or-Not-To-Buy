import streamlit as st

st.set_page_config(page_title="To Buy or Not To Buy", page_icon="🍛", layout="wide")

# Frequency Data
stats = {
    "Hunger Level": {
        "1": ["Not Hungry", 3/15, 10/15],
        "2": ["Moderately Hungry", 6/15, 2/15],
        "3": ["Starving", 6/15, 3/15]
    },
    "Home Food Availability": {
        "1": ["Yes", 8/15, 10/15],
        "2": ["No", 7/15, 5/15]
    },
    "Allowance Status": {
        "1": ["Just Received Allowance", 6/15, 8/15],
        "2": ["Running Low / Almost no allowance left", 9/15, 7/15]
    },
    "Price Affordability": {
        "1": ["Very Affordable", 3/15, 2/15],
        "2": ["Just Right", 11/15, 9/15],
        "3": ["Expensive", 1/15, 4/15]
    },
    "Queue Length": {
        "1": ["Short", 11/15, 6/15],
        "2": ["Long", 4/15, 9/15]
    }
}

def get_probs(category, selection_text):
    for key, val in stats[category].items():
        if val[0] == selection_text:
            return val[1], val[2]
    return 1, 1 

st.title("🍛 To Buy or Not To Buy: Decision Analyzer")
st.markdown("Select the current conditions below to calculate the probability of a student purchasing viand.")
st.divider()

col_input, col_output = st.columns([1, 1], gap="large")

with col_input:
    with st.container(border=True):
        st.subheader("📝 Environmental Factors")
        hunger = st.selectbox("Hunger Level", [val[0] for val in stats["Hunger Level"].values()])
        home_food = st.selectbox("Home Food Availability", [val[0] for val in stats["Home Food Availability"].values()])
        allowance = st.selectbox("Allowance Status", [val[0] for val in stats["Allowance Status"].values()])
        price = st.selectbox("Price Affordability", [val[0] for val in stats["Price Affordability"].values()])
        queue = st.selectbox("Queue Length", [val[0] for val in stats["Queue Length"].values()])
        
        st.write("")
        run_prediction = st.button("Calculate Probability", type="primary", use_container_width=True)

with col_output:
    with st.container(border=True):
        st.subheader("📊 Model Prediction")
        
        if run_prediction:
            prob_yes = 15/30
            prob_no = 15/30
            
            factors = [
                ("Hunger Level", hunger),
                ("Home Food Availability", home_food),
                ("Allowance Status", allowance),
                ("Price Affordability", price),
                ("Queue Length", queue)
            ]
            
            for category, selection in factors:
                p_y, p_n = get_probs(category, selection)
                prob_yes *= p_y
                prob_no *= p_n

            total_prob = prob_yes + prob_no
            perc_yes = (prob_yes / total_prob) * 100
            perc_no = (prob_no / total_prob) * 100
            
            # Display metrics
            metric_col1, metric_col2 = st.columns(2)
            metric_col1.metric("Likelihood of YES", f"{perc_yes:.2f}%", f"Raw: {prob_yes:.4f}")
            metric_col2.metric("Likelihood of NO", f"{perc_no:.2f}%", f"Raw: {prob_no:.4f}")
            
            st.divider()
            if prob_yes > prob_no:
                st.success("### 🎯 Decision: BUY VIAND")
                st.markdown("The model predicts that under these conditions, the student is more likely to make a purchase.")
            else:
                st.error("### 🛑 Decision: DO NOT BUY")
                st.markdown("The model predicts that under these conditions, the student will likely walk away.")
        else:
            st.info("Waiting for input. Adjust the environmental factors on the left and click 'Calculate Probability' to see the results.")