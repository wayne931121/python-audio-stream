eval "$(conda shell.bash hook)"
conda activate /home/way/2
pulseaudio -D
python server.py
read -n1 -r -p "Press any key to continue..." key