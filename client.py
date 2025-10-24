

import socket
import sounddevice as sd
import numpy as np

# --- Audio and Network Configuration ---
# Standard audio settings for good quality and low latency
SAMPLE_RATE = 44100  # Samples per second (Hz)
CHANNELS = 1         # Mono audio
CHUNK_SIZE = 1024    # Number of frames per buffer
HOST = '192.168.1.105'     # Listen on all available interfaces
PORT = 12345         # The port to connect to

def start_server():
    """Starts the TCP server and handles audio playback."""
    print("Starting audio streaming server...")

    # Initialize PyAudio/PortAudio output stream
    sd.default.samplerate = SAMPLE_RATE
    sd.default.channels = CHANNELS
    
    # Create a TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    
    print(f"Server listening on {HOST}:{PORT}")
    
    conn, addr = s.accept()
    print(f"Connection established with {addr}")

    # Open the playback stream
    with sd.OutputStream(samplerate=SAMPLE_RATE, channels=CHANNELS) as stream:
        while True:
            try:
                # 1. Receive data
                # We need to receive the exact size of the chunk
                audio_data_bytes = conn.recv(CHUNK_SIZE * np.dtype('float32').itemsize * CHANNELS)
                
                if not audio_data_bytes:
                    break  # Connection closed by client

                # 2. Convert bytes back to a NumPy array (int16 is a common format for raw audio)
                audio_data = np.frombuffer(audio_data_bytes, dtype='float32')
                
                # 3. Play the audio chunk
                stream.write(audio_data)

            except ConnectionResetError:
                print("Client disconnected.")
                break
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"Server error: {e}")
                break

    conn.close()
    s.close()
    print("Server stopped.")

if __name__ == '__main__':
    start_server()