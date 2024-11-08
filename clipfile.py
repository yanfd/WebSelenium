import cv2
import os

def split_video_into_frames(video_path, output_folder, frame_rate):
    # 创建输出文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 读取视频文件
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if frame_count % frame_rate == 0:
            frame_name = f"frame_{frame_count}.jpg"
            frame_path = os.path.join(output_folder, frame_name)
            cv2.imwrite(frame_path, frame)

        frame_count += 1

    cap.release()

video_path = "/Users/yanfengwu/Downloads/click.mov" # 视频文件路径
output_folder = "output_frames"  # 输出图片文件夹路径
frame_rate = 16  # 指定的帧数

split_video_into_frames(video_path, output_folder, frame_rate)
