import socket
import struct
import io
from google.cloud import vision
from PIL import Image, ImageFile
import os
import numpy as np
import sys


def send_text_array(sock, text_array):
    sock.send(str(text_array).encode("utf-8"))
    print('send : ', text_array)


def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)

    return buf

def calculate_expression(expression_list):
    result = None
    operator = None
    for char in expression_list:
        if char.isdigit():
            if result is None:
                result = int(char)
            else:
                if operator == '+':
                    result += int(char)
                elif operator == '-':
                    result -= int(char)
                elif operator == 'x':
                    result *= int(char)
                elif operator == '/':
                    result /= int(char)
            operator = None
        elif char in ['+', '-', 'x', '/']:
            operator = char
    return result

def recognize_text(image_path):
    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if texts:
        return texts[0].description
    else:
        return None

def main():
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    host = '' 
    port = 7777 

    while(1):
        print("meaning")
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))

        s.listen(True)

        conn, addr = s.accept()
        print('Connected by', addr)
        length = recvall(conn, 4)
        length = struct.unpack('!i', length)[0]

        stringData = recvall(conn, int(length))
        data = io.BytesIO(stringData)
        im = Image.open(data)


        im.save('/root/Desktop/sevc/received_image.png','PNG')



        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/root/Desktop/sevc/proven-country-388105-2b1fa1639dd9.json'
        image_path = r"/root/Desktop/sevc/received_image.png"



        # 이미지에서 텍스트 인식
        recognized_text = recognize_text(image_path)


        if recognized_text:
        # 추출된 텍스트에서 숫자와 연산자 추출
            expression_list = []
            for char in recognized_text:
                if char.isdigit() or char in ['+', '-', 'x', '/']:
                    expression_list.append(char)

        # 추출한 문자열 리스트를 결합하여 수식 문자열 생성
            expression_str = ''.join(expression_list)
            send_text_array(conn, expression_str)
            print(expression_str)
        else:
            print("텍스트를 인식할 수 없습니다.")
    conn.close()
    

if __name__ == "__main__":
	main()
	os.execl(sys.executable, sys.executable, *sys.argv)
    
