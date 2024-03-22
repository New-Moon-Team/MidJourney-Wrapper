import time

import requests
import json
import threading


class MyThread(threading.Thread):
    def __init__(self, thread_id, message):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.message = message

    def run(self):
        print(f"Thread {self.thread_id} is running")
        # Thiết lập URL webhook và tin nhắn
        webhook_url = "https://discord.com/api/webhooks/1099974705101942784/8oZSGWrrBldDmHxE5yDUdx9c8oUGbChigAuTxpstPeGwHA22v7L0A06pk3LXkI70Seg7"
        # message = "$coloring book page, filled with closed shapes, clear drawing, no background, siberian husky dog with glasses, abstract, artistic, pen outline, black and white, white background, very very very large shapes, full field of view, center, edge to edge 8k resolution"
        # message = "$coloring page for kids, simple, funny alligator, coloring style --q 2 --v 5 --v 5"
        # Tạo payload chứa tin nhắn
        payload = {
            "content": self.message
        }

        # Chuyển đổi payload thành định dạng JSON
        payload = json.dumps(payload)

        # Thiết lập header và gửi POST request
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(webhook_url, data=payload, headers=headers)

        # Kiểm tra kết quả gửi
        if response.status_code == 204:
            print("Tin nhắn đã được gửi thành công!")
        else:
            print("Có lỗi xảy ra khi gửi tin nhắn.")


threads = []

list_promt = [
    "$coloring page for kids, simple, funny alligator, coloring style --q 2 --v 5 --v 5",
    "$coloring page for kids, funny man in space, cartoon style, isolated --ar 4:5 --v 5",
    "$outline vector monochrome coloring page depicting bouquet coloring book, adult colouring book style, in thick line and straight picture, black and white, white background --ar 17:22 --v 5 --no grey",
    "$simple lilies in pond coloring page, black and white, white background --ar 17:22 --v 5 --no grey,gray,shadin",
    "$simple monochrome lineart vector outline of A detailed frog mandala, in cartoon coloring page style:: shading, gradient, hatching, stippling, grey, complex, details, text, black fill, grey fill, shadow, logo, points, signature::-0.3 --ar 11:14 --v 5 --q 2 --s 750",
    "$pixiebob cat breed, coloring book , black and white, mandala style, cartoon, comic book --q 2 --v 5",
    "$cute dragon and hearts coloring book black and white with crisp lines and white backroung ar 17:22",
    "$coloring page for preschooler, pixar style tiny joyful rabbit eating carrots, full body view, cartoon style, crisp lines, low detail, no shading, no pencil, art fades into white background --ar 17:22 --s 250 --v 5 --q 2",
    "$cute baby flower dragon, coloring pages, coloring book, black and white, high details, intricate details, cartoon style --ar 100:131 --q 2 --v 5",
    "$girl hugging a dragon, romance, many details, line style, for coloring book, clear image, 4k, line art, no color,",

]
for item in list_promt:
    thread = MyThread(list_promt.index(item), item)
    thread.start()
    threads.append(thread)
    time.sleep(3)
# for i in range(1):
#     thread = MyThread(i, list_promt[i])
#     thread.start()
#     threads.append(thread)

for thread in threads:
    thread.join()

print("All threads have finished")
