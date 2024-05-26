from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("#")

db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)

def list_videos():
    for video in video_collection.find():
        print(f"{video['_id']}, Name: {video['name']}, Time: {video['time']}")

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {"_id": ObjectId(video_id)}, {"$set": {"name": new_name, "time": new_time}})

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})

def main():
    while True:
        print("YouTube Manager app with MongoDB")
        print("1. List videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit app")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter video ID to update: ")
            name = input("Enter the new video name: ")
            time = input("Enter the new video time: ")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
