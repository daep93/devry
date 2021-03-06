# Django convention

### 파이썬의 PEP-8 스타일 가이드를 기반으로 함.

- 공백
  - 들여쓰기는 4칸을 권장한다.
    - 탭보다는 스페이스를 권장한다. 한 프로젝트 내에서 탭과 스페이스를 혼용하는 일은 피해야 한다.
  - 한 줄의 문자 길이는 최대 79자 이하로 한다.
    - 코드의 길이가 길어지는 경우 `\`을 이용해 줄바꿈을 한다.
    - 연산자들로 코드가 길게 늘어지는 경우 연산자 이전에 줄바꿈을 한다.
  - 함수와 클래스는 두 개의 빈 줄로 구분한다.
  - 클래스 내부의 메서드는 하나의 빈 줄로 구분한다.
  - 한 줄이 길어져서 다음 줄으로 넘어갈 때에는 그 요소의 앞 부분에 맞추어 줄바꿈을 한다.
  - 예) `foo = bar(bar_one, bar_two,
                  bar_three, bar_four)`
  - 대괄호와 소괄호 안, 쉼표, 콜론과 세미콜론 앞과 같은 위치에 불필요한 공백을 넣지 않는다.
  - 트레일링 콤마는 선택적으로 사용할 수 있지만 요소 1개만을 가지는 튜플의 경우는 반드시 넣어야 한다.
  - 변수 선언, 할당 시 줄을 맞추기 위해 과도하게 공백을 넣지 않는다. 한 칸씩만 띄워주면 충분하다.
  - 우선순위가 다른 연산자들을 함께 쓸 때는 우선순위가 가장 낮은 연산자 주위로 공백을 주어 구분한다.
  - 키워드 인자와 인자의 기본값에서의 `=`는 붙여서 쓴다. 예) (`'user'=user`)
  - 변수 할당 전후에는 스페이스를 한 번만 사용한다.
  - 리스트 인덱스, 함수의 호출, 키워드 인수 할당에는 스페이스를 사용하지 않는다.
- 이름 지정
  - 함수, 변수, 속성에는 소문자를 사용하고, 두 단어 이상이면 `_`로 연결한다.
  - 상수는 모듈 레벨에서 정의되고, `_`로 구분해 대문자로 작성된다.  예) ` MAX_OVERFLOW`
  - `I`, `O`과 같이 `1`, `l`, `O`과 혼동될 우려가 있는 문자를 이름을 짓는 데에 사용하지 않는다.
  - 클래스명의 경우 글자 간 공백 없이, 두 단어 이상이라면 첫 글자를 대문자로 써 구분한다.
  - 클래스의 인스턴스 메서드에서는 첫 인자의 이름을 `self`로 한다.
  - 클래스 메서드의 첫 인자 이름은 `cls`로 한다.
  - 예외의 경우 클래스 형태이어야 하기에 클래스 이름의 작성 규칙이 여기에도 적용되지만 `Error`접미사를 예외의 이름으로 활용한다.
- 표현식, 문장
  - 비어 있는 값은 암시적으로 False가 된다 가정한다.
  - 한 줄의 코드에 여러 명령문을 넣지 않는다.
  - 한 줄로 된 제어문, 반복문 사용을 지양한다.
  - 여러 모듈을 import하는 경우 한 줄에 나열하지 않고 행으로 구분해 사용한다.
  - import문의 위치는 항상 문서의 최상단이 될 수 있도록 한다.
  - 패키지에서 모듈을 불러오고자 할 경우 항상 모듈의 절대 이름을 사용한다.
  - 상대적인 import인 경우 명시적 구문을 `from . import module`처럼 작성한다.
    - 위의 경우에서는 module을 여러 개 나열해도 좋다. 예) `from . import module1, module2`

- 주석
  - 코드가 갱신될 때마다 주석 역시 그에 맞게 갱신해야 한다.
  - 불필요한 주석은 달지 않아야 한다.
  - 주석의 첫 글자는 대문자로 시작하는 것이 좋다.
  - 비영어권 사용자만 읽는 코드가 아니라면 반드시 영어로 작성해야 한다.
  - 인라인 주석(코드의 바로 오른편에 다는 주석)은 지양해야 한다.
    - 인라인 주석을 사용하는 경우 구문으로부터 최소 2개 이상의 스페이스로 구분되어야 한다.



