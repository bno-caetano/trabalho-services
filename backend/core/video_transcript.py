from ast import Try
from urllib.parse import urlparse, parse_qs
from contextlib import suppress
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from utils.exceptions import DurationTime
import streamlit as st

class Transcript:

    def __init__(self):
        pass

    def get_yt_id(self, url, ignore_playlist=False):
        query = urlparse(url)
        if query.hostname == 'youtu.be': return query.path[1:]
        if query.hostname in {'www.youtube.com', 'youtube.com', 'music.youtube.com'}:
            if not ignore_playlist:
                with suppress(KeyError):
                    return parse_qs(query.query)['list'][0]
            if query.path == '/watch': return parse_qs(query.query)['v'][0]
            if query.path[:7] == '/watch/': return query.path.split('/')[1]
            if query.path[:7] == '/embed/': return query.path.split('/')[2]
            if query.path[:3] == '/v/': return query.path.split('/')[2]

    def transcript_from_id(self, id, language=['pt', 'en', 'es', 'de', 'fr']):
        try:
            transcript = YouTubeTranscriptApi.get_transcript(id, language)
        except:
            st.error('Url invalida ou idioma não suportado. Por favor valide o link inserido.')
            exit()

        return transcript

    def format_transcript(self, transcript):
        formatter = TextFormatter()
        try:
            if transcript[-1]['start'] > 600:
                raise Exception
            else:
                txt = formatter.format_transcript(transcript)
        except Exception:
            st.error('Video muito grande. Por favor, mantenha seus videos em até 10 minutos.')
            exit()

        return txt
    



