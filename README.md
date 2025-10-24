# python-audio-stream
write by gemini, modify by wayne931121.


Windows
```
pip install sounddevice numpy
python client.py
```

Linux - WSL
```
chmod +x Miniforge3-Linux-x86_64.sh
./Miniforge3-Linux-x86_64.sh
conda config --set auto_activate_base false
conda create --prefix /home/way/2
conda activate /home/way/2
conda install python=3.7
sudo apt-get install libportaudio2
pip install sounddevice numpy
sudo apt install pulseaudio
pulseaudio -D

python server.py
```

Network

in server and client .py modify

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/82633e49-6e35-4f80-99c2-5440a96caada" />

Allow find and share

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/80fc83eb-44c0-4b5e-bb27-6c58dcd52a7a" />

