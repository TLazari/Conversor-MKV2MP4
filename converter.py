import os
from moviepy import VideoFileClip

def convert_mkv_to_mp4(input_folder, output_folder):
    # Verifica se a pasta de saída existe; caso contrário, cria.
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Percorre todos os arquivos na pasta de entrada.
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".mkv"):  # Filtra apenas arquivos MKV.
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + ".mp4")
            
            try:
                # Converte MKV para MP4.
                print(f"Convertendo: {input_path} -> {output_path}")
                clip = VideoFileClip(input_path)
                clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
                clip.close()
            except Exception as e:
                print(f"Erro ao converter {input_path}: {e}")

# Define as pastas de entrada e saída.
input_folder = "D:\RECURSOS DO SISTEMA"
output_folder = "D:\RECURSOS DO SISTEMA\MP4"

# Executa a conversão.
convert_mkv_to_mp4(input_folder, output_folder)
