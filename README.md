# BERT-model-Q-A
A machine learning model pre-trained to answer question from a provided essay or article. The web app to display the model's action in the browser was deployed using Streamlit python library.

## TODO

- Deploy the model to a cloud backend
- Improve the UI of the Streamlit frontend
- Add event handler to prevent the model triggering until all text field is completed.

## Credits
- This starter code for the model is obtained from [Chris McCormick](https://mccormickml.com/2020/03/10/question-answering-with-a-fine-tuned-BERT/).
- The model uses pretrained BERT imported from [huggingface website](https://huggingface.co/bert-large-uncased-whole-word-masking-finetuned-squad?text=Where+do+I+live%3F)
- The frontend to display the model in action was built with [Streamlit](https://www.streamlit.io/)