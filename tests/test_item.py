import sys, os
# file_path = os.fspath(os.path.abspath(''))
# print(file_path)
import sys, os
myPath = os.path.dirname(os.path.dirname(__file__+ '/'))
print(myPath)

# def test_new_item():
#     print("Testing new item to be added to db")
#     new_item = Item(content="Item to test")
#     assert new_item.content == "Item to test"
#     assert new_item.content != None
