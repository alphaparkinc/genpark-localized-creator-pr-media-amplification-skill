from client import LocalizedCreatorPrMediaAmplificationClient

def main():
    client = LocalizedCreatorPrMediaAmplificationClient()
    res = client.amplify_announcement("Next-Gen Autonomous Agent Protocol Launch", ["North America", "APAC", "EMEA"])
    print(f"Outlets Reached: {res['media_outlets_reached']}")
    print(f"Press Kit: {res['influencer_press_kit_url']}")
    print(f"Syndication: {res['syndication_status']}")

if __name__ == "__main__":
    main()
