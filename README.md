<h1>rasa - chatbot</h1>

rasa env
- python3.8

vscode의 gitbash창에서 아래 코드 실행 
pip install rasa  #rasa 설치
pip install spacy  #패키지 설치
python -m spacy download ko_core_news_sm  #한국어 토큰화

rasa 모델 초기모델 생성하기
rasa init (초기모델 생성 계속 yes 선택해주세요)
rasa train (모델 수정하면 실행하여 학습)
rasa shell (터미널에서 모델 응답생성)
rasa run (서버를 통해 모델 응답생성)

rasa 한글사용
- config.yml 파일 수정하기
- nlu.yml 파일에 인텐트 작성하기
- domain.yml 인텐트별 모델 답변 작성하기
- stories.yml 대화 스토리 작성하기
- tests/test_stories.yml (잘 모르겠으나 위 파일과 같이 한글로 수정하니까 한글 사용 성공)
