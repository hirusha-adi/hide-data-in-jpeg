# hide-data-in-jpeg
Hide data in jpeg + read hidden data easily with python3

### NOTE: This works only with `.jpeg` images

# Usage
```
from imghide import JPEG

# wiriting to a jpeg image
secret_data = b"Made by hirusha adikari"
write_status = JPEG.write(file_name="image.jpeg", secret=secret_data)
print(write_status)

# reading from a jpeg image
secret = JPEG.read(file_name="image.jpeg")
print(secret)
```
Make sure you have copied this `imghide` folder inside your project folder!

