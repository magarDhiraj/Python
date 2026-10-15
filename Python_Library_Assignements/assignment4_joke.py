from tqdm import tqdm
import time

# Display progress for 20 tasks
for task in tqdm(range(20), desc="Completing study tasks"):
    time.sleep(0.1)

# Display completion message
print("All 20 study tasks completed!")
