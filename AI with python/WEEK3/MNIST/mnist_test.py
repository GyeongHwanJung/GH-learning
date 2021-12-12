# -----------------------------------------------
# 모델을 활용한 손글씨 이미지 테스트
# 새롭게 생성한 손글씨 이미지 데이터를 전달하여
# 숫자 확인하기
# -----------------------------------------------
import joblib, struct
import os.path

# 변수 선언 ---------------------------------------
IMAGE_PATH  = "../Data/MNIST/PGM/"
MODEL_FILE  = "../Data/MNIST/handdigit.pkl"
DEBUG = True

# 함수 선언 ----------------------------------------
# https://convertio.co/kr/jpg-pgm/
# 이미지 파일에 적힌 숫자 검출함수 --------------------
def detect_number(digit_file):
    img_data=[]
    with open(digit_file, mode='rb') as fp:
        # pgm header 건너띄기
        fp.seek(len("P2 28 28 255\n"))

        # raw image data 가져오기
        while True:
            data=fp.read(1)
            if not data: break

            # unpack() 반환값이 tuple 타입
            img_data.append(struct.unpack('>B', data)[0])
            if DEBUG:
                print(f"data => {data}")
                print(f"img_data => {img_data}")
           # predict( 2차원데이터 )
    return clf.predict( [ [n / 256 for n in img_data] ] )

# 기능 구현 ----------------------------------------
if not os.path.exists(MODEL_FILE):
    print("Model File Not Found! Bye~^^")
else:
    # 모델 로딩
    clf=joblib.load(MODEL_FILE)

    # 새로운 데이터 테스트
    file_name=input("Enter pgm image file name : ")
    result = detect_number(IMAGE_PATH+file_name+".pgm")
    print(f"Image File - {file_name} \n> RESULT : {result}")


