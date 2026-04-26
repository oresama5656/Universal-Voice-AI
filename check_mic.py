import pyaudio

def list_microphones():
    pa = pyaudio.PyAudio()
    print("=== Available Audio Input Devices ===")
    info = pa.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    
    found = False
    for i in range(0, numdevices):
        if (pa.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            dev_info = pa.get_device_info_by_host_api_device_index(0, i)
            print(f"Index {i}: {dev_info.get('name')}")
            print(f"  Default Sample Rate: {dev_info.get('defaultSampleRate')}")
            found = True
            
    if not found:
        print("No input devices found.")
    
    pa.terminate()

if __name__ == "__main__":
    try:
        list_microphones()
    except Exception as e:
        print(f"Error listing devices: {e}")
    input("\nPress Enter to exit...")
