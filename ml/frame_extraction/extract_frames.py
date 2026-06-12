import cv2
import os

# Paths
DATASET_PATH = "ml/dataset"
OUTPUT_PATH = "ml/extracted_frames"

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_PATH, exist_ok=True)

# Process both real and fake videos
for category in ["real", "fake"]:
    video_folder = os.path.join(DATASET_PATH, category)
    output_category = os.path.join(OUTPUT_PATH, category)

    os.makedirs(output_category, exist_ok=True)

    for video_file in os.listdir(video_folder):
        video_path = os.path.join(video_folder, video_file)

        # Skip non-video files
        if not video_file.endswith((".mp4", ".avi", ".mov")):
            continue

        video_name = os.path.splitext(video_file)[0]
        video_output = os.path.join(output_category, video_name)

        os.makedirs(video_output, exist_ok=True)

        cap = cv2.VideoCapture(video_path)

        frame_count = 0

        while True:
            success, frame = cap.read()

            if not success:
                break

            frame_filename = os.path.join(
                video_output,
                f"frame_{frame_count:04d}.jpg"
            )

            cv2.imwrite(frame_filename, frame)

            frame_count += 1

        cap.release()

        print(f"{video_file}: {frame_count} frames extracted")

print("Frame extraction completed!")