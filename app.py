import time
import lmstudio as lms

print("Waiting for LM Studio daemon to initialize...")
time.sleep(5) # Give the lms server a moment to spin up

# Download a small test model via CLI command if not already bundled
# e.g., lms download <model-id>

try:
    with lms.Client() as client:
        print("Connected to LM Studio Core successfully!")
        # Your custom application logic goes here
except Exception as e:
    print(f"Error connecting: {e}")

# Keep the container alive if this is a worker
while True:
    time.sleep(3600)

