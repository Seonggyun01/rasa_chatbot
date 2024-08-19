<h1>rasa - chatbot</h1>
<hr>
<h3>1. 가상환경 생성 (rasa_env)</h3>
<li>파이썬 3.8.10버전 다운로드</li>
<li>pip install virtualenv #가상환경 라이브러리 설치</li>
<li>virtualenv 가상환경이름 --python=3.8</li>
<hr>
<h3>2. 라사 오픈소스 설치</h3>
<li>vscode의 새 터미널 열고 gitbash창으로 변경 후 아래 코드 실행</li> 
<li>source 가상환경이름/Scripts/activate #가상환경 활성화</li>
<li>pip install rasa  #rasa 설치</li>
<li>pip install spacy  #패키지 설치</li>
<li>python -m spacy download ko_core_news_sm  #한국어 토큰화</li>
<hr>
<h3>3. rasa 모델 초기모델 생성하기</h3>
<li>rasa init (초기모델 생성 계속 yes 선택해주세요)</li>
<li>rasa train (모델 수정하면 실행하여 학습)</li>
<li>rasa shell (터미널에서 모델 응답생성)</li>
<li>rasa run --enable-api --cors "*" (서버를 통해 모델 응답을 로컬 웹페이지에서 생성)</li>
<hr>
<h3>4. rasa 한글사용</h3>
<li>config.yml 파일 수정하기</li>
<li>nlu.yml 파일에 인텐트 작성하기</li>
<li>domain.yml 인텐트별 모델 답변 작성하기</li>
<li>stories.yml 대화 스토리 작성하기</li>
<li>tests/test_stories.yml (잘 모르겠으나 위 파일과 같이 한글로 수정하니까 한글 사용 성공)</li>
