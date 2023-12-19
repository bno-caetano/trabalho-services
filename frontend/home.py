
import streamlit as st
import requests

st.set_page_config(
    page_title="YouSum",
    page_icon=":movie_camera:",
    layout="centered",
    initial_sidebar_state="expanded"
)

api_url = 'http://yousum-backend:8080/'

st.title(':movie_camera: Youtube :red[Summarizer]', anchor=False)
# st.subheader('Seja muito bem-vindo ao trabalho de conclusão de curso de NLP do Instituo Mauá de Tecnologia.')
st.markdown('\n\n')

texto_abertura = """Seja muito bem-vindo ao youtube summarizer. 
                    \n Uma ferramenta que permite capturar as principais informações de seus videos preferidos do youtube.
                    Para utiliza-la é muito simples: copie a url do video desejado e cole no box abaixo, espere o video carregar, para confirmação de que se trata do video correto, e depois é só clicar em 'Resumir'.
                    """

st.write(texto_abertura)

url = st.text_input('Insira sua URL no box abaixo:')

if url:
    try:
        st.video(url)
    except:
        pass

key = st.text_input("Por favor, insira sua chave openai:")   

if st.button('Resumir', type='primary'):
    if key:
        print(key)
        params_transcript = {'url':url}
        formatted_output = requests.get(api_url + "yt_transcript/", params_transcript)

        params_tokens = {"txt":formatted_output.json()['message']}
        num_tokens = requests.get(api_url + "tokens/", params_tokens)

        params_comp = {"prompt":formatted_output.json()['message'], "num_token": num_tokens.json()['message'], "key":key}
        comp = requests.post(api_url + "response/", params = params_comp)

        st.divider()
        with st.chat_message('user'):
            message_placeholder = st.empty()
            message_placeholder.markdown("Aguarde um momento enquanto estou processando sua solicitação..")
    #        for r in comp:
    #            message_placeholder.markdown(str(r) + "▌")

            message_placeholder.markdown(comp.text)
    else:
        print('else')
        key = st.empty

