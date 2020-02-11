class Linked_List:
  
  class __Node:

    # def __init__(self, val):
    # declares private variables for nodes
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

  # def __init__(self):
  # creates the attributes of the linked-list
  def __init__(self):
        self.__header = Linked_List.__Node(None)
        self.__trailer = Linked_List.__Node(None)
        self.__count = 0

  # def __len__(self):
  # returns the count/size of the linked list
  def __len__(self):
    return self.__count

  # def append_element(self, val):
  # Checks to see if the list is empty.
  # If yes creates new node and links to header and trailer
  # If no, it links to nodes in end of list.
  def append_element(self, val):
    new_node = Linked_List.__Node(val)    
    if (self.__header.next is None):
      self.__header.next = new_node 
      new_node.prev = self.__header
      self.__trailer.prev = new_node 
      new_node.next = self.__trailer

    else:
      self.__trailer.next = new_node
      new_node.prev = self.__trailer.prev
      new_node.next = self.__trailer
      self.__trailer.prev.next = new_node
      self.__trailer.prev = new_node 
      self.__trailer.next = None  
    self.__count = self.__count + 1

  # def insert_element_at(self, val, index):
  # Checks to see if the position is valid.
  # If not, raises an index error.
  # If yes, goes to the position and inserts the element.
  # Increments count.
  def insert_element_at(self, val, index):
    if (index > self.__count or index < 0):
        print( "Invalid position to insert")
        raise IndexError

    new_node = Linked_List.__Node(val)
    current = self.__header.next
    count = 0
    while (count < (index - 1)):
       current = current.next
       count = count + 1
    new_node.next = current.next
    new_node.prev = current
    current.next.prev = new_node
    current.next = new_node

    self.__count = self.__count + 1

  # def remove_element_at(self, index):
  # Checks to see if the index is valid to remove.
  # If no, raises an index error.
  # If yes, goes to position and removes index
  # returning the lement stored.
  def remove_element_at(self, index):
    if (index > self.__count or index < 0):
      print( "Invalid position to insert")
      raise IndexError
    current = self.__header.next
    count = 0
    while (count < (index - 1)):
       current = current.next
       count = count + 1
    current.next.prev = current.prev
    current.prev.next = current.next
    self.__count = self.__count - 1
    return current.val

  # def get_element_at(self, index):
  # Checks to see if the index is valid.
  # if not raises an index error.
  # If yes, it goes to position and returns
  # element stored at that position.
  def get_element_at(self, index):
      if (index > self.__count or index < 0):
          print("Out of list range")
          raise IndexError
      current = self.__header.next
      count = 0
      while (count < (index - 1)):
       current = current.next
       count = count + 1
      return current.val

  # def rotate_left(self):
  # This rotates the linked list data left
  def rotate_left(self):
    tempNode = self.__header.next
    self.__trailer.next = tempNode
    tempNode.prev = self.__trailer.prev
    self.__header.next = tempNode.next
    tempNode.next.prev = self.__header
    tempNode.next = self.__trailer

    self.__trailer.prev.next = tempNode
    self.__trailer.prev = tempNode
    self.__trailer.next = None
        
  # def __str__(self):
  # Goes through the linked list, concatenating the
  # data stored into a "string of nodes."
  # Once the current walk is done, it returns the string
  def __str__(self):
    current_node = self.__header.next
    stringNode = "[ "
    if (current_node.val == None):
        stringNode += "]"
        return stringNode
    while (current_node.next != None):
      stringNode += str(current_node.val)
      if (current_node.next != self.__trailer):
        stringNode += ", "
      current_node = current_node.next
    stringNode += " ]"
    return stringNode

  def __iter__(self):
    # initialize a new attribute for walking through your list
    # insert your initialization code before the return
    # statement. do not modify the return statement.

    self.__current = Linked_List.__Node(None)
    return self

  def __next__(self):
    # using the attribute that you initialized in __iter__(),
    # fetch the next value and return it. If there are no more 
    # values to fetch, raise a StopIteration exception.

    if (self.__current is None):
      self.__current = self.__header
      raise StopIteration
    else:
      tempNode = self.__current
      self.__current = self.__current.next
      return tempNode

if __name__ == '__main__':
  dllist = Linked_List()

  #Test cases for appending
  dllist.append_element(0)
  dllist.append_element(1)
  dllist.append_element(2)
  dllist.append_element(3)
  dllist.append_element(4)
  dllist.append_element(9)
  dllist.append_element(-83)
  dllist.append_element(-523)
  dllist.append_element(-73739)
  print(dllist)
  
  #Printing the list and testing element searching
  #print("Got element: " + str(dllist.get_element_at(-1)))
  print("Got element: " + str(dllist.get_element_at(1)))
  print("Got element: " + str(dllist.get_element_at(2)))
  print("Got element: " + str(dllist.get_element_at(3)))
  print("Got element: " + str(dllist.get_element_at(5)))
  print("Got element: " + str(dllist.get_element_at(9)))
  #print("Got element: " + str(dllist.get_element_at(1000)))
  print(dllist)

  #Inserting an element test cases
  #dllist.insert_element_at(5,-230)
  dllist.insert_element_at(0,2)
  dllist.insert_element_at(5,4)
  dllist.insert_element_at(6,2)
  dllist.insert_element_at(-755,7)
  dllist.insert_element_at(-62,4)
  dllist.insert_element_at(-8945,6)
  #dllist.insert_element_at(9,20)
  print(dllist)
  
  #Rotating list left
  dllist.rotate_left()
  dllist.rotate_left()
  dllist.rotate_left()
  print(dllist)

  #Removing from the list
  #print("Removed element: " + str(dllist.remove_element_at(1000)))
  print("Removed element: " + str(dllist.remove_element_at(len(dllist))))
  print("Removed element: " + str(dllist.remove_element_at(1)))
  print("Removed element: " + str(dllist.remove_element_at(3)))
  #print("Removed element: " + str(dllist.remove_element_at(-1)))
  print(dllist)

  #Printing length of list
  print("Length of list: " + str(dllist.__len__()))

  #Printing the entire list
  print(dllist)