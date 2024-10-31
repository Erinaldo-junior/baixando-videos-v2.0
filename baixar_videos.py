import yt_dlp
import os
import subprocess
import re

# Define o caminho para a pasta 'baixados'
download_folder = 'baixados'

# Verifica se a pasta existe, e se não, cria a pasta
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Define o caminho para o executável FFmpeg na pasta 'ffmpeg_bin'
ffmpeg_path = os.path.join(os.path.dirname(__file__), 'ffmpeg_bin', 'bin', 'ffmpeg.exe')

# Função para limpar caracteres especiais do título
def sanitize_title(title):
    return re.sub(r'[\\/*?:"<>|]', "", title)

url = input('Cole aqui sua URL: ')

# Configurações para baixar o melhor vídeo sem áudio
ydl_video_opts = {
    'format': 'bestvideo',  # Baixa apenas o vídeo na melhor qualidade
    'outtmpl': f'{download_folder}/video.%(ext)s',  # Salva o vídeo como "video.ext"
}

# Configurações para baixar o melhor áudio
ydl_audio_opts = {
    'format': 'bestaudio',  # Baixa apenas o áudio na melhor qualidade
    'outtmpl': f'{download_folder}/audio.%(ext)s',  # Salva o áudio como "audio.ext"
}

# Baixa o vídeo e obtém o título
with yt_dlp.YoutubeDL(ydl_video_opts) as ydl:
    info_video = ydl.extract_info(url, download=True)
    video_ext = info_video['ext']  # Obtém a extensão do vídeo
    title = sanitize_title(info_video['title'])  # Limpa o título para usar como nome de arquivo
    video_path = f"{download_folder}/video.{video_ext}"  # Caminho completo para o arquivo de vídeo
    print("Download do vídeo concluído com sucesso!")

# Baixa o áudio
with yt_dlp.YoutubeDL(ydl_audio_opts) as ydl:
    info_audio = ydl.extract_info(url, download=True)
    audio_ext = info_audio['ext']  # Obtém a extensão do áudio
    audio_path = f"{download_folder}/audio.{audio_ext}"  # Caminho completo para o arquivo de áudio
    print("Download do áudio concluído com sucesso!")

# Define o caminho do arquivo final usando o título do vídeo
output_path = os.path.join(download_folder, f"{title}.mp4")

# Mescla o vídeo e o áudio usando o FFmpeg da pasta 'ffmpeg_bin'
ffmpeg_command = [
    ffmpeg_path, '-i', video_path, '-i', audio_path, '-c:v', 'copy', '-c:a', 'aac', '-strict', 'experimental', output_path
]

# Executa o comando FFmpeg para mesclar vídeo e áudio
try:
    subprocess.run(ffmpeg_command, check=True)
    print("Mesclagem de vídeo e áudio concluída com sucesso!")
    print("Arquivo final:", output_path)
    
    # Remove os arquivos de vídeo e áudio separados após a mesclagem
    os.remove(video_path)
    os.remove(audio_path)
except subprocess.CalledProcessError as e:
    print("Erro ao mesclar vídeo e áudio:", e)
