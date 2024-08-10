import spacy

# SpaCy 한국어 모델 로드
nlp = spacy.load("ko_core_news_sm")

# 예제 문장
doc = nlp("안녕하세요. 저는 Rasa를 사용하고 있습니다.")

for token in doc:
    print(token.text, token.pos_)
