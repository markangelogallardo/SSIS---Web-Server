import cloudinary
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

# Configuration       
cloudinary.config( 
    cloud_name = "dbwqwl5ui", 
    api_key = "613699665316178", 
    api_secret = "2yAw39DikggsM0SnnAc5syzxhcM", # Click 'View API Keys' above to copy your API secret
    secure=True
)

# Upload an image
upload_result = upload("default_pic.jpg", asset_folder="/Student_Pictures", public_id="id_num", invalidate=True, overwrite=True, resource_type="image", format="png")
print(upload_result["secure_url"])

