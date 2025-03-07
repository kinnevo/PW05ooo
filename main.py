import requests
import streamlit as st


BASE_API_URL = "http://34.59.108.214:7860/"
FLOW_ID = "840c44d6-52c2-4371-ac95-356dd8703e06"
ENDPOINT = "PW05" # The endpoint name of the flow


def run_flow(message: str) -> dict:
    api_url = f"{BASE_API_URL}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }

    headers = None
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def main():
    st.title("Chat Interface")
    
    message = st.text_area("Message", placeholder="Ask something...")
    
    if st.button("Run Flow"):
        if not message.strip():
            st.error("Please enter a message")
            return
    
        try:
            with st.spinner("Running flow..."):
                response = run_flow(message)
            
            response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(response)
        except Exception as e:
            st.error(str(e))

if __name__ == "__main__":
    main()