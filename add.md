# 프로그램 설치 방법

## 프로그램 다운로드
- 아래 링크에서 프로그램을 다운로드 받는다.  
[프로그램 다운로드](https://drive.google.com/file/d/1lKk5NDPP_T890f0dJTW6lMgdaqSoPFpP/view?usp=sharing)  
- 원하는 곳에 압축을 푼다. 
- 이 파일은 인공지능 학습을 위한 사진데이터를 모두 포함하고 있어 5기가 정도 용량이지만, 프로젝트를 위한 서버와 클라이언트는 부수적인 파일들은 필요하지 않다.  
- 서버 파일은 3.kiosk 폴더의 smartM_ai_server 폴더 안에 있는 smartM_ai_server_new.py 파일이다.  
- 클라이언트 파일은 3. kiosk 폴더에 kiosk.py 파일이다.  
- 전자제어 여닫이 문을 제어하는 파일은 3. kiosk 폴더의 doorOpenClose_python 폴더 안에 있는 doorOpenClose_python.ino 파일이다. 
- .py로 되어 있는 파일은 python으로 실행하고, .ino로 되어 있는 파일은 아두이노 IDE를 이용해 아두이노 우노보드에 업로드 하여 사용한다.  


## python 설치(3.8버전으로 설치할 것)
- 아래 링크를 클릭해 python 3.8.10 버전을 다운로드 받고 설치한다.  
[python 3.8.10 다운로드 링크](https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe)  
- 설치 화면 하단의 Add Python 3.8 to PATH를 반드시 체크하고 Install Now버튼을 눌러 설치한다.  
![image](https://user-images.githubusercontent.com/13882302/210344769-3c3108bf-fdfb-442d-9bef-95b968dac583.png)

## cmd를 통한 폴더 이동
![image](https://user-images.githubusercontent.com/13882302/210346348-55fc5098-b360-4945-b9ab-12275e734d1a.png)
- 탐색기를 열어 서버가 설치되어 있는 폴더로 이동 한 다음 위 그림처럼 주소창을 클릭하고 해당 폴더의 주소를 복사한다.  
![image](https://user-images.githubusercontent.com/13882302/210346494-8abfb3e2-b487-40a4-912f-c02180b50603.png)
- 윈도우 왼쪽 하단의 검색창을 열고 cmd를 입력한다음 엔터를 눌러 명령 프롬프트를 연다.  
![image](https://user-images.githubusercontent.com/13882302/210346603-1e19e823-5180-4676-90d8-e6c8a8135158.png)
- 명령 프롬프트가 열리면 아래 예시의 형태로 cd 명령어를 써서 서버 폴더로 이동한다. 위의 탐색기에서 복사한 주소를 붙여넣으면 된다.    
```cmd
cd C:\<압축을 푼 위치>\AI_seyong-main\3. kiosk\smartM_ai_server
```
- 폴더 이동이 잘 되면 아래 그림과 같은 형태로 폴더 위치를 확인할 수 있다.  
![image](https://user-images.githubusercontent.com/13882302/210348019-f4787201-9dd5-4488-901a-81316cc7a73f.png)
- dir명령어를 통해 해당 폴더에 들어있는 폴더와 파일을 볼 수 있다.  
![image](https://user-images.githubusercontent.com/13882302/210348135-770e05e1-9ef4-437f-b92d-a33aff55e673.png)


## 기본 라이브러리 설치  
- 아래 명령어를 순서대로 입력하여 모두 설치한다.  
- torch, torchvision을 최신 버전으로 설치하면 소스코드 일부를 수정해야 한다.  

```python
python.exe -m pip install --upgrade pip
pip install numpy
pip install opencv-python
pip install pillow
pip install matplotlib
pip install easydict
pip install flask
pip install torch
pip install torchvision
pip install pandas
pip install pyyaml
pip install tqdm
pip install seaborn
pip install wget
pip install pyserial
```
- 아래 그림처럼 전체를 드래그해서 복사하고, cmd 창에 넣으면 알아서 모두 설치한다.  
![image](https://user-images.githubusercontent.com/13882302/210348797-5281a6b5-26df-41de-8054-6fc0c4cb8235.png)
- 아래 그림은 설치 과정이다.  
![image](https://user-images.githubusercontent.com/13882302/210348914-3b50d176-34f9-430d-9baf-badddf51f52f.png)
- 각각의 라이브러리가 설치될 때마다 아래 그림처럼 Successfully installed ~~~ 라는 문구가 나온다.  
![image](https://user-images.githubusercontent.com/13882302/210349039-02f28f40-de65-4fdb-b11a-beeb30a5ea00.png)


## 옵션 라이브러리 설치(여기부터는 음성 추가용, 추후 옵션으로 사용할 예정, 설치하지 않아도 됨)
```python
pip install pip install speechrecognition
pip install pip install gtts
pip install pip install playsound
```

# 프로그램 사용 방법
## 오류메시지
### 파이썬을 이용해 사용하는 라이브러리들이 제대로 설치가 되어 있지 않아서 발생하는 오류가 가장 많음. 위에 제시한 모든 라이브러리들이 제대로 설치되어 있어야 함
### 자동문을 여닫는 용도의 아두이노 우노를 USB포트에 연결하지 않았을 경우 이런 오류가 발생함, 연결하면 해결됨
```python
serial.serialutil.SerialException: could not open port '': FileNotFoundError(2, '지정된 경로를 찾을 수 없습니다.', None, 3)
```

## 서버와 클라이언트 열기  
### 1. 윈도우 왼쪽 하단의 돋보기를 클릭하고 cmd를 쳐서 명령프롬프트를 연다.
### 2. 서버가 설치되어 있는 폴더로 이동한다. 
```cmd
cd C:\<시스템이 설치되어 있는 주소>\AI_seyong-main\3. kiosk\smartM_ai_server
```
### 3. 파이썬 프로그램으로 서버를 연다
```cmd
python smartM_ai_server_new.py
```
- 아래와 같은 화면이 되면 서버가 잘 열려서 구동하고 있는 상태이다. 
![image](https://user-images.githubusercontent.com/13882302/210349797-1ee05022-b02b-49d8-b396-c92cca10a5cb.png)

### 4. 다시 돋보기로 가서 cmd 명령어를 이용해 새로운 명령프롬프트를 연다.
### 5. 클라이언트가 설치되어 있는 폴더로 이동한다. 
```cmd
cd C:\<시스템이 설치되어 있는 주소>\AI_seyong-main\3. kiosk
```
### 5. 파이썬 프로그램으로 클라이언트를 연다
- 현재 자동으로 문이 열리는 부분은 주석처리 되어 있으므로, 이 기능을 살리려면 아래 파이썬 프로그램의 28~36번째 줄, 216번 줄을 주석해제하고 사용한다.  
- 다음 그림을 그 아래 그림의 형태로 주석 처리한 #을 삭제해주면 된다. 파이썬은 들여쓰기로 구문을 구분하므로 딱 #만 지워야 한다.  
![image](https://user-images.githubusercontent.com/13882302/210350792-4ed0632b-902f-40c9-b328-719350ac5a59.png)
![image](https://user-images.githubusercontent.com/13882302/210350848-57843563-208e-437b-ba4a-b0c3ef78376c.png)
- 216번줄도 다음 그림과 같이 바꿔주고 저장한다.(ser.write(val)부분)  
![image](https://user-images.githubusercontent.com/13882302/210351241-0f32afba-1ff2-4859-bed6-6b3da7de449b.png)
![image](https://user-images.githubusercontent.com/13882302/210351286-b64d5377-d68a-48ed-acf2-4979b00b1705.png)
- 아두이노를 연결하지 않은 상태에서 위와 같이 주석을 해제하면 프로그램이 오류가 나므로, 꼭 여닫이 문을 제어할 때만 주석을 해제하고 사용한다. 
- 코드 편집 프로그램은 다음 링크에서 다운로드 받은 atom 편집기를 사용하면 된다.  
[atom.io다운로드](https://sourceforge.net/projects/atom.mirror/)

- 문을 실제로 열기 위해서는 아두이노에 해당 프로그램을 업로드 하고, 릴레이를 설치해야 한다. 아두이노 부분은 아래에서 다시 설명한다.  
```cmd
python kiosk.py
```
- 풀 스크린으로 세팅이 된 키오스크 창을 적당한 크키로 조정한다.  
![image](https://user-images.githubusercontent.com/13882302/210353305-10b4750b-fc04-4f0c-a350-3b2afe40a5fc.png)
- '상품 인식하기'버튼을 누르면 서버와 클라이언트의 cmd 창에서 다음과 같은 오류가 발생한다. 
- 서버창  
![image](https://user-images.githubusercontent.com/13882302/210353677-e0bb5f6e-9f38-4853-b18e-ba951fa1e811.png)

- 클라이언트 창  
![image](https://user-images.githubusercontent.com/13882302/210353572-ab312c1a-0852-4639-bf38-ae8a7efe59c4.png)

- 아래의 오류를 해결해줘야 제대로 사용할 수 있는데, 이것은 torch라는 인공지능 라이브러리가 업데이트 되면서 입력해줘야 하는 파라메터 숫자가 달라졌기 때문이다. 
```
'Upsample' object has no attribute 'recompute_scale_factor'
```
- 아래 링크를 참고하여 라이브러리의 파라메터를 수정하고 다시 실행해본다. 
[참고자료 링크](https://iambeginnerdeveloper.tistory.com/183)  

- cmd에서 아래 명령어를 이용해 torch라이브러리가 설치되어 있는 폴더를 확인한다. Location이라고 써 있는 곳이 그 위치이다.  
```python 
pip show torch
```
![image](https://user-images.githubusercontent.com/13882302/210355097-3b71e89c-6172-44ef-b2a4-33df4cc738d8.png)

- 해당 주소를 복사하여 아래와 같이 탐색기를 열고 붙여넣은 다음 해당 폴더로 이동한다. 
![image](https://user-images.githubusercontent.com/13882302/210355315-903679cf-8723-4095-a536-546f46d8dbbf.png)

- 우리가 수정하려는 파일은 아래 그림의 위치에 있으므로 해당 폴더를 찾아가서 upsampling.py 파일을 찾아 atom 에디터로 연다.  
![image](https://user-images.githubusercontent.com/13882302/210355432-ae701fad-7e43-4f4c-adff-3e7b0559d5b6.png)

![image](https://user-images.githubusercontent.com/13882302/210355667-a1e41b29-d6a1-4435-9d6d-a53c3b172573.png)

![image](https://user-images.githubusercontent.com/13882302/210355744-6842c20d-19f0-4f50-a59b-63ebbcc739a9.png)

- 아래 그림의 하얀색 부분이 주석처리되면 정상적으로 동작하므로 atom에서 157번 줄을 찾아 해당 부분앞에 #을 붙여 주석처리하고 저장한다.  
![image](https://user-images.githubusercontent.com/13882302/210355814-696bc854-17f9-48fa-b8ea-0d1a883a201e.png)
![image](https://user-images.githubusercontent.com/13882302/210356168-f61c1810-d79f-440b-91db-a0bffe9b2334.png)

- 주석처리 전
![image](https://user-images.githubusercontent.com/13882302/210356251-46ee8eb7-18f3-4fa7-a7fb-ee4ac36a862f.png)
- 주석처리 후(주석처리 한 행의 마지막에 있는 괄호를 꼭 다음줄로 넘겨놓을 것. 그렇지 않으면 함께 주석처리되어 오류가 발생함)  
![image](https://user-images.githubusercontent.com/13882302/210357409-084a5472-dd92-4d37-b743-f27758f5abca.png)

- 서버와 클라이언트를 다시 실행하면 정상 동작 하는 것을 확인할 수 있다.  


### 6. 명령프롬프트 창의 위치를 적당히 조정하고, 클라이언트 프로그램에서 결제하기 버튼을 눌러 결과를 확인함
#### 주의사항
- 하드웨어 세팅이 잘 되어 있지 않으면 결과물을 확인할 수 없음
- 카메라 두 대의 위치와 각도, 결과물로 보여지는 y축의 정렬이 정확해야 원하는 값을 얻을 수 있으므로, 하드웨어 세팅이 매우 중요함  
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/291fadee-88fa-448d-81c6-3d0405172606/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221230T014219Z&X-Amz-Expires=86400&X-Amz-Signature=a01cffc8f29b469da1c4f5dbd32311665ec0ded8f508949243672b91bd600f84&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/1bf48fc7-5f63-4960-a798-1828c5b08f25/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221230T014756Z&X-Amz-Expires=86400&X-Amz-Signature=d76a2add47bc6cae78b0245c384120880aaacfee179adcf92df487b3af76543f&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a1a7d405-68f6-46df-9c02-ad75a7cc343a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221230T014817Z&X-Amz-Expires=86400&X-Amz-Signature=3bae274c20341c3e33a7c50702ef1aa548ce1e7d7c0eef3249aa360ed33c161d&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/977ab77d-9819-4727-9c4d-c43986b7acc8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221230T014904Z&X-Amz-Expires=86400&X-Amz-Signature=3a89834013ac13c7bf48bb215d71407ed46567bb3e9237e88f8c610e5e991400&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)
- 서버에 표현되는 결과 로그에서 추정된 결과값 bpred의 값 아래쪽에 같은 상품명이 2개가 모두 찍혀야 해당 상품이 키오스크의 값으로 들어가게 설정되어 있음. 이는 오작동을 줄이기 위해 카메라를 2대를 세팅해서 각각 해당 카메라에 들어온 값이 온전하느냐를 판별하기 위함임  
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d6790a11-7093-40cd-b9a1-53511324cce9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221230T015000Z&X-Amz-Expires=86400&X-Amz-Signature=4bc4f4616b9dc902eb665384c9e6cd44193fb8ff8969484c319386a35d43b3ee&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/67a8385e-1776-437d-aeb3-a867167b340c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221230T014925Z&X-Amz-Expires=86400&X-Amz-Signature=c01a2070607bcfe8681bc45a5861b6e20e8e4cb5cf5b269d2580b4f8a2e404b3&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)


### 7. 여닫이 문을 자동제어 하려면, 아두이노 코드가 설치되어 있는 폴더로 이동한다. 
- 현재 자동으로 문이 열리는 부분은 주석처리 되어 있으므로, 이 기능을 살리려면 kiosk.py 파이썬 프로그램의 28~36번째 줄, 216번 줄을 주석해제하고 사용할 것
```cmd
cd C:\<시스템이 설치되어 있는 주소>\AI_seyong-main\3. kiosk\doorOpenClose_python
```
- 아래 링크에서 아두이노 IDE를 다운로드 받는다.  
[아두이노 IDE 다운로드](https://downloads.arduino.cc/arduino-1.8.19-windows.exe)  
- 아두이노 코드가 들어 있는 폴더의 doorOpenClose_python.ino 파일을 아두이노 IDE를 이용해 연다. 잘 안될 경우 아두이노 IDE를 열고 아래 코드를 복사해서 붙여넣고 활용한다.  
```arduino
int input_data;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  digitalWrite(13,LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    input_data = Serial.read();
    if(input_data == '1'){
      Serial.println(input_data);
      digitalWrite(13, HIGH); // led_on
      delay(3000);
      digitalWrite(13, LOW); // led_off
    }
  }
}
```

- IDE의 툴 탭에서 보드를 아두이노 우노로, 포트를 아두이노 우노가 연결되어 있는 포트를 선택한다.  
- 아두이노 우노보드에 업로드 하고, 인공지능 키오스크 클라이언트가 구동되는 컴퓨터에 USB케이블로 연결해 놓는다. 
- 아두이노의 13번 핀을 이용해 여닫이 문에 설치된 릴레이를 제어하도록 코딩되어 있으므로 아래 그림의 제어선이라고 되어 있는 부분과 아두이노의 13번 핀을 연결한다.  
- 아래 이미지를 참고하면 좋지만, 릴레이 제작 회사마다 약간씩 다를 수 있으니 릴레이 보드 하단에 있는 핀 이름을 꼭 확인하고 연결한다.  
![image](https://user-images.githubusercontent.com/13882302/210350335-ede46b4e-0cc3-45fa-9cec-aab8f24f69ad.png)
- 여닫이 문에 전원이 공급되면 문에 달려 있는 스위치를 통해서도 문이 열리고 잠기지만, 그 옆에 있는 날 선 두개를 합선시켜도 문이 열리게 된다. 이 원리를 이용해 날 선 두개 중 하나를 릴레이의 가운데에, 나머지 하나를 output1 또는 output2에 연결하면 된다. 가운데는 꼭 두 선 중 하나를 끼워야 하지만, 아웃푼 쪽은 문 열림이 동작하는 결과를 보고 내가 원하는 것과 달리 거꾸로 동작한다면 다른 output으로 옮겨서 사용하면 정상작동한다.  
