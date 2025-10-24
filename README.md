# python-audio-stream
write by gemini, modify by wayne931121.

Stream Audio from Linux WSL Xcef to Windows

server.py: audio server, websocket client, run second

client.py: audio client, websocket "server", run "first"!!!

Windows
```
pip install sounddevice numpy
python client.py
```

Linux - WSL
```
wsl
#connect to remote desktop..
#open terminal
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh -O Miniforge3-Linux-x86_64.sh
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

# Network

in server and client .py modify

<img alt="image" src="https://github.com/user-attachments/assets/82633e49-6e35-4f80-99c2-5440a96caada" />

<img alt="image" src="https://github.com/user-attachments/assets/5ca54c29-6da1-411a-b23c-25e987149d18" />

<img alt="image" src="https://github.com/user-attachments/assets/50978f65-f7c7-484f-8da2-b10d54d86097" />

<img alt="image" src="https://github.com/user-attachments/assets/5e34019d-0ece-4324-9859-288b7fba7569" />




## Allow find and share

<img alt="image" src="https://github.com/user-attachments/assets/80fc83eb-44c0-4b5e-bb27-6c58dcd52a7a" />

(https://www.youtube.com/watch?v=v0Zp-VdzXOY)
<img alt="image" src="https://github.com/user-attachments/assets/3626a836-8869-47e3-8dc1-82ea730221d8" />


## Test in Linux - WSL
```
ping your-ip
```

# DEMO
https://youtu.be/hNG5jj2Quy8

# ALSO SEE
https://github.com/wayne931121/GUI-to-WSL
