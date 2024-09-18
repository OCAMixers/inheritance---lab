import random

class RandomList(list):
    def get_random_element(self):
        if not self:
            return None
        return random.choice(self)

List_rand = RandomList([1, 2, 3])
print("Random List: ", List_rand)

random_list = List_rand.get_random_element()
print("Phần tử random:", random_list)

if random_list:
    List_rand.remove(random_list)
    print("Phần tử sau khi xóa: ", List_rand)
else:
    print("Không có cái gì để xóa!")
