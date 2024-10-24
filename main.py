import ffmpeg
from pathlib import Path
import os
import random

# Указание пути к с исходным файлам
input_folder = Path("input")
# Допустимые расширения видео
video_extensions = ['.mp4', '.avi', '.wmv', '.mov', '.flv', '.mkv']

# Количество уникализаций
n = 15

''' contrast_min = -1000
contrast_max = 1000
contrast_default = 1
contrast_deviation = 0.0001

brightness_min = -1
brightness_max = 1
brightness_default = 0
brightness_deviation = 0.1 '''

def main():
    
    video_list = get_video_list(input_folder, video_extensions)
    for video_name in video_list:
        for run in range(n):
            print(f"\Итерация = {run}\n")
            unify_video_object(video_name, run)

    print(f"Готово!")

def get_video_list(input_folder, video_extensions):
    
    try:
        video_list = [video_name for video_name in os.listdir(input_folder) if os.path.splitext(video_name)[1].lower() in video_extensions]
        return video_list

    except Exception as e:
        print(e)
        raise(e)

def unify_video_object(video_name, run):

    input_video_path = os.path.join(input_folder, video_name)
    short_video_name, video_extension = os.path.splitext(video_name)
    output_video_name = f"{short_video_name}_output_{run}{video_extension}"

    input_video = ffmpeg.input(input_video_path)

    # Изменение контрастности
    input_video = edit_contrast(input_video)
    # Изменение яркости
    input_video = edit_brightness(input_video)
    # Изменение сатурации
    input_video = edit_saturation(input_video)
    # Изменение гаммы
    input_video = edit_gamma(input_video)
    # Изменение гаммы красного
    input_video = edit_gamma_r(input_video)
    # Изменение гаммы зеленого
    input_video = edit_gamma_g(input_video)
    # Изменение гаммы синего
    input_video = edit_gamma_b(input_video)
    ''' # Изменение гамма-веса
    input_video = edit_gamma_weight(input_video) '''

    # Сохранение
    output_video = ffmpeg.output(input_video, output_video_name)
    ffmpeg.run(output_video)

def edit_contrast(input_video):
    value = random.uniform(0.8, 1.1)
    print(f"\nКонтраст = {value}\n")
    output_video = input_video.filter('eq', contrast = value) # По умолчанию: 1 (-1000 до 1000)
    return output_video

def edit_brightness(input_video):
    value = random.uniform(-0.07, 0.07)
    print(f"\nЯркость = {value}\n")
    output_video = input_video.filter('eq', brightness = value) # По умолчанию: 0 (-1 до 1)
    return output_video

def edit_saturation(input_video):
    value = random.uniform(0.6, 1.5)
    print(f"\nЯркость = {value}\n")
    output_video = input_video.filter('eq', saturation = value) # По умолчанию: 1 (0 до 3)
    return output_video

def edit_gamma(input_video):
    value = random.uniform(0.9, 1.4)
    print(f"\nЯркость = {value}\n")
    output_video = input_video.filter('eq', gamma = value) # По умолчанию: 1 (0.1 до 10)
    return output_video

def edit_gamma_r(input_video):
    value = random.uniform(0.8, 1.3)
    print(f"\nЯркость = {value}\n")
    output_video = input_video.filter('eq', gamma_r = value) # По умолчанию: 1 (0.1 до 10)
    return output_video

def edit_gamma_g(input_video):
    value = random.uniform(0.8, 1.3)
    print(f"\nЯркость = {value}\n")
    output_video = input_video.filter('eq', gamma_g = value) # По умолчанию: 1 (0.1 до 10)
    return output_video

def edit_gamma_b(input_video):
    value = random.uniform(0.8, 1.3)
    print(f"\nЯркость = {value}\n")
    output_video = input_video.filter('eq', gamma_b = value) # По умолчанию: 1 (0.1 до 10)
    return output_video

def edit_gamma_weight(input_video):
    output_video = input_video.filter('eq', gamma_b = 0) # По умолчанию: 1 (0 до 1)
    return output_video

if __name__ == "__main__":
    main()
