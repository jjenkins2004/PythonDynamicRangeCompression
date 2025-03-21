from dynamic_range_compression import compress_audio
import os
import time

# Define file paths.
input_folder = "in"
output_folder = "out"
input_file = os.path.join(input_folder, "test.m4a")
output_file = os.path.join(output_folder, "test_compressed.m4a")

# Ensure the output folder exists.
os.makedirs(output_folder, exist_ok=True)

# Define compressor settings (example values).
threshold = -20         # Compression threshold in dB
makeupGain = 5          # Makeup gain in dB
kneeWidth = 5           # Knee width in dB
compressionRatio = 2.0  # Compression ratio
lookAhead = 10          # Lookahead time in ms
attack = 5              # Attack time in ms
release = 50            # Release time in ms

# Start timer.
start_time = time.time()

# Call compress_audio to process the file.
compress_audio(input_file, output_file, threshold, makeupGain, kneeWidth, compressionRatio, lookAhead, attack, release)

# Stop timer.
elapsed_time = time.time() - start_time

print("Compression complete. File saved to:", output_file)
print("Time taken: {:.2f} seconds".format(elapsed_time))