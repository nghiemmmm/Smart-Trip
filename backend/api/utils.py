'''
Chức năng:
Nhận vào một địa chỉ email và kích thước avatar (mặc định 200).

Trả về một URL đến hình đại diện Gravatar tương ứng.

Mặc định kiểu ảnh nếu không có là retro (kiểu hoạt hình cổ điển).
'''
import hashlib
from urllib.parse import urlencode

def get_gravatar(email, size="200"):
    """Return Gravatar link from email"""

    gravatar_url = "//www.gravatar.com/avatar/" + \
        hashlib.md5(email.encode('utf-8')).hexdigest() + "?"
    gravatar_url += urlencode({'d': 'retro', 's': str(size)})

    print("Gravatar", gravatar_url)
    return gravatar_url