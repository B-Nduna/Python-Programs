import speedtest

def test_internet_speed():
    # Create a Speedtest object
    st = speedtest.Speedtest()

    print("Finding the best server...")
    st.get_best_server()  

    print("Testing download speed...")
    download_speed = st.download() 

    print("Testing upload speed...")
    upload_speed = st.upload()  
    print("Testing ping...")
    ping = st.results.ping 

    # Convert speeds from bits per second to megabits per second (Mbps)
    download_speed_mbps = download_speed / 1_000_000
    upload_speed_mbps = upload_speed / 1_000_000

    # Display the results
    print(f"\nDownload Speed: {download_speed_mbps:.2f} Mbps")
    print(f"Upload Speed: {upload_speed_mbps:.2f} Mbps")
    print(f"Ping: {ping:.2f} ms")

if __name__ == "__main__":
    test_internet_speed()
