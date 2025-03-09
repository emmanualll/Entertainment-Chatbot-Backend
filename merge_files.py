import os
import json

stories_dir = "stories"
merged_stories = []

# Loop through all JSON files in "stories/" directory
for filename in os.listdir(stories_dir):
    if filename.endswith(".json"):
        file_path = os.path.join(stories_dir, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            story_data = json.load(f)
            merged_stories.append(story_data)  # Add each story to the list

# Save all stories into one file
with open(os.path.join(stories_dir, "stories.json"), "w", encoding="utf-8") as f:
    json.dump(merged_stories, f, indent=4)

print("Merged all stories into stories/stories.json")
